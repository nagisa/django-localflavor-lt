import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name = 'django-localflavor-lt',
    version = '1.0',
    description = 'Country-specific Django helpers for Lithuania.',
    long_description = README,
    author = 'Simonas Kazlauskas',
    author_email = 'simonas@kazlauskas.me',
    license='BSD',
    url = 'https://github.com/simukis/django-localflavor-lt',
    packages = ['django_localflavor_lt'],
    include_package_data = True,
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'Django>=1.4',
    ]
)
