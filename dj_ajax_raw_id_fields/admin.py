from . import widgets


class AjaxRawIdFieldsMixin(object):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        db = kwargs.get('using')
        if db_field.name in self.dj_raw_id_fields:
            kwargs['widget'] = widgets.AjaxForeignKeyRawIdWidget(
                db_field.remote_field, self.admin_site, using=db)
            return db_field.formfield(**kwargs)

        return super(AjaxRawIdFieldsMixin, self).formfield_for_foreignkey(
            db_field, request, **kwargs)
