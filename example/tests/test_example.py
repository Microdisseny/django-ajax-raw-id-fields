from urllib.parse import urljoin

from blog.models import Author, Post

from .common_selenium import TestWithSelenium


class ExampleTest(TestWithSelenium):
    def test_exemple(self):
        self.login()
        Author.objects.create(**{'name': 'Pepito', 'email': 'pepito@example.com', 'city': 'Girona'})
        manel = Author.objects.create(**{'name': 'Manel', 'email': 'manel@example.com', 'city': 'Barcelona'})

        url = urljoin(self.live_server_url, '/admin/blog/post/add/')
        self.browser.get(url)

        self.browser.find_element_by_id('id_slug').send_keys('example')
        self.browser.find_element_by_id('id_title').send_keys('Post Example')

        # Click on the Glass icon with the id <lookup_id>.
        self.browser.find_element_by_id('lookup_id_author').click()

        #  Activate the popup window with the `window.name = <window_id>`
        self.browser.switch_to.window(self.browser.window_handles[1])

        # Click on item with the link text <link_text>.
        self.browser.find_element_by_link_text('Manel').click()
        # Activate default window
        self.browser.switch_to.window(self.browser.window_handles[0])

        # Check Glass icon text
        element = self.browser.find_element_by_css_selector('#author_dj_ajax_raw_id_fields_label')

        self.assertEqual(element.text, str(manel))

        # Check input value
        element = self.browser.find_element_by_css_selector('#id_author')
        self.assertEqual(element.get_attribute('value'), str(manel.pk))

        self.browser.find_element_by_css_selector('input[name=_continue]').click()

        # Check model
        self.assertEqual(Post.objects.get(slug='example').author, manel)
