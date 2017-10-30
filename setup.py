from distutils.core import setup
from setuptools import find_packages

VERSION = '0.0.1'

CLASSIFIERS = [
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Topic :: Software Development',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Environment :: Web Environment',
    'Development Status :: 5 - Production/Stable',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='dj_ajax_raw_id_fields',
    description='raw_id_fields widget replacement',
    version=VERSION,
    author='Alexandre Busquets Triola',
    author_email='abusquets@gmail.com',
    license='MIT License',
    platforms=['OS Independent'],
    url='https://github.com/Microdisseny/django-ajax-raw-id-fields',
    packages=find_packages(exclude=['__pycache__']),
    include_package_data=True,
    classifiers=CLASSIFIERS,
    zip_safe=False,
)
