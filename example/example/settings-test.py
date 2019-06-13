import os
import tempfile

DEBUG = True

DATABASES['default'] = {  # noqa
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory',
}

MEDIA_ROOT = os.path.join(tempfile.TemporaryDirectory().name, 'media')
MEDIA_URL = '/media/'

FIELD_FILEMANAGER_STORAGE_CONFIG = [
    {
        'storage': 'django.core.files.storage.FileSystemStorage',
        'code': 'test',
        'path': os.path.join(MEDIA_ROOT, 'storage_file_example'),
        'url': os.path.join(MEDIA_URL, 'storage_file_example'),
        'thumbnail': {
            'path': os.path.join(MEDIA_ROOT, 'storage_file_thumbnails_example'),
            'url': os.path.join(MEDIA_URL, 'storage_file_thumbnails_example'),
            'width': 250,
            'height': 250
        }
    }
]
