# Django ajax_raw_id_fields

Based on [Django-salmonella](https://github.com/lincolnloop/django-salmonella)


## Usage

There is an example project.

Add **dj\_ajax\_raw_id\_fields** to **INSTALLED\_APPS**

Add **TabsMixin** in your **ModelAdmin**

```python
from dj_ajax_raw_id_fields.admin import AjaxRawIdFieldsMixin

class QuestionAdmin(AjaxRawIdFieldsMixin, admin.ModelAdmin):
```

Define raw_id_fields and dj_raw_id_fields fields

```python
    raw_id_fields = ('author',)
    dj_raw_id_fields = ('author',)
```


Example image:

![](example.png?raw=true)

## Credits

- Alexandre Busquets Triola

This package uses code from **Lincoln Loop** [django-salmonella](https://github.com/lincolnloop/django-salmonella).


## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
