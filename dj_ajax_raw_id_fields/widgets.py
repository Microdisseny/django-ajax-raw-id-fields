from django import forms
from django.conf import settings
from django.contrib.admin.widgets import ForeignKeyRawIdWidget


class AjaxForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
    template_name = ('dj_ajax_raw_id_fields/widgets/'
                     'ajax_foreign_key_raw_id.html')
    hidden = True

    def get_context(self, name, value, attrs):
        context = super(AjaxForeignKeyRawIdWidget, self).get_context(
            name, value, attrs)
        context['widget']['attrs']['class'] = 'vForeignKeyRawIdAdminField vAjaxForeignKeyRawIdAdminField'
        if self.hidden:
            context['widget']['type'] = 'hidden'
        app_name = self.rel.model._meta.app_label.strip()
        model_name = self.rel.model._meta.object_name.lower().strip()

        context.update({
            'name': name,
            'app_name': app_name,
            'model_name': model_name
        })

        return context

    @property
    def media(self):
        extra = '' if settings.DEBUG else '.min'
        return forms.Media(
            js=[
                'admin/js/vendor/jquery/jquery{0}.js'.format(extra),
                'admin/js/jquery.init.js',
                'admin/js/core.js',
                "dj_ajax_raw_id_fields/js/dj_ajax_raw_id_fields.js",
            ]
        )

class VisibleAjaxForeignKeyRawIdWidget(AjaxForeignKeyRawIdWidget):
    hidden = False
