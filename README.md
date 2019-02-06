# Django ajax_raw_id_fields

Based on [Django-salmonella](https://github.com/lincolnloop/django-salmonella)

## Install

```
pip install -e git+https://github.com/Microdisseny/django-ajax-raw-id-fields.git#egg=dj_ajax_raw_id_fields
```
or

```
pip install dj-ajax-raw-id-fields
```

## Usage

There is an example project.

Add **dj\_ajax\_raw_id\_fields** to **INSTALLED\_APPS**

Add **AjaxRawIdFieldsMixin** in your **ModelAdmin**

```python
from dj_ajax_raw_id_fields.admin import AjaxRawIdFieldsMixin

class QuestionAdmin(AjaxRawIdFieldsMixin, admin.ModelAdmin):
```

Define raw_id_fields and dj_raw_id_fields fields

```python
    raw_id_fields = ('author',)
    dj_raw_id_fields = ('author',)
```


Add **dj_ajax_raw_id_fields.urls** in your **project.urls.py**

```python
urlpatterns = [
    ...
    url(r'^admin/dj_ajax_raw_id_fields/', include(
        'dj_ajax_raw_id_fields.urls')),
]
```

Example image:

![](example.png?raw=true)

## Credits

- Alexandre Busquets Triola

This package uses code from **Lincoln Loop** [django-salmonella](https://github.com/lincolnloop/django-salmonella).


## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
