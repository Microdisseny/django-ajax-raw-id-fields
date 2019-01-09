from django.conf import settings
from django.contrib.admin.widgets import ForeignKeyRawIdWidget


class AjaxForeignKeyRawIdWidget(ForeignKeyRawIdWidget):
    template_name = ('dj_ajax_raw_id_fields/widgets/'
                     'ajax_foreign_key_raw_id.html')

    def get_context(self, name, value, attrs):
        context = super(AjaxForeignKeyRawIdWidget, self).get_context(
            name, value, attrs)
        context['widget']['type'] = 'hidden'

        app_name = self.rel.model._meta.app_label.strip()
        model_name = self.rel.model._meta.object_name.lower().strip()

        context.update({
            'name': name,
            'app_name': app_name,
            'model_name': model_name
        })

        return context

    class Media:
        js = (settings.STATIC_URL + 'dj_ajax_raw_id_fields/js/'
              'dj_ajax_raw_id_fields.js',)
