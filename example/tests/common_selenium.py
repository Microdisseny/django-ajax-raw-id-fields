from importlib import import_module

from django.conf import settings
from django.contrib.auth import (BACKEND_SESSION_KEY, HASH_SESSION_KEY,
                                 SESSION_KEY)
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver


def force_login(user, driver, base_url):
    SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
    driver.get('{}{}'.format(base_url, '/admin/'))

    session = SessionStore()
    session[SESSION_KEY] = user.id
    session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
    session[HASH_SESSION_KEY] = user.get_session_auth_hash()
    session.save()

    domain = base_url.split(':')[-2].split('/')[-1]
    cookie = {
        'name': settings.SESSION_COOKIE_NAME,
        'value': session.session_key,
        'path': '/',
        'domain': domain
    }

    driver.add_cookie(cookie)
    driver.refresh()


class TestWithSelenium(StaticLiveServerTestCase):
    def setUp(self):
        super().setUp()
        self.admin_user = User.objects.create_superuser(
            'admin', 'admin@example.com', 'admin'
        )

        self.staff_user = User.objects.create_user(
            'pepito', 'pepito@example.com', 'pepito'
        )
        self.staff_user.is_staff = True
        self.staff_user.save()

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        cls.browser = webdriver.Chrome(chrome_options=options)
        cls.browser.set_window_position(0, 0)
        cls.browser.set_window_size(1280, 2560)
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.browser.quit()

    def login(self):
        force_login(self.admin_user, self.browser, self.live_server_url)
