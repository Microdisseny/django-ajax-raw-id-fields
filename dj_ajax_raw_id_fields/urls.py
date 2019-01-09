# With modifications from
# https://github.com/lincolnloop/django-salmonella/blob/master/salmonella/urls.py

from django.urls import re_path
from dj_ajax_raw_id_fields.views import label_view

urlpatterns = [
    re_path(r'^(?P<app_name>[\w-]+)/(?P<model_name>[\w-]+)/$', label_view,
            name="dj_ajax_raw_id_fields_label"),
]
