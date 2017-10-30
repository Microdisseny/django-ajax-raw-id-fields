from django.conf.urls import (
    url, include
)
from django.contrib import admin

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/dj_ajax_raw_id_fields/', include(
        'dj_ajax_raw_id_fields.urls')),
]
