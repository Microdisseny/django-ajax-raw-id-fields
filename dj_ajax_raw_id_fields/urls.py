# With modifications from
# https://github.com/lincolnloop/django-salmonella/blob/master/salmonella/urls.py
#

from django.conf.urls import url
from dj_ajax_raw_id_fields.views import label_view

urlpatterns = [
    url(r'^(?P<app_name>[\w-]+)/(?P<model_name>[\w-]+)/$',
        label_view,
        {
            'template_name': 'dj_ajax_raw_id_fields/label.html'
        },
        name="dj_ajax_raw_id_fields_label"),
]
