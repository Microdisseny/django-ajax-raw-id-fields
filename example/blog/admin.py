from django.contrib import admin
from dj_ajax_raw_id_fields.admin import AjaxRawIdFieldsMixin
from .models import (
    Post, Author
)


class PostAdmin(AjaxRawIdFieldsMixin, admin.ModelAdmin):
    raw_id_fields = ('author',)
    dj_raw_id_fields = ('author',)


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
