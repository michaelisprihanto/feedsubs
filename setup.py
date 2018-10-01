from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'LICENSE'), encoding='utf-8') as f:
    long_description += f.read()

setup(
    name='feedsubs',
    version='0.0.1',
    description='RSS and Atom feeds reader for Python 3',
    long_description=long_description,
    url='https://github.com/NicolasLM/feedsubs',
    author='Nicolas Le Manchet',
    author_email='nicolas@lemanchet.fr',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Framework :: Django',
    ],
    keywords='rss atom feed feeds reader',

    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'manage.py = feedsubs.manage:main'
        ]
    },

    install_requires=[
        'boto3',
        'django',
        'django-allauth',
        'django-bulma',
        'django-storages',
        'atoma',
        'bleach',
        'beautifulsoup4',
        'psycopg2',
        'requests',
        'spinach',
        'Pillow',
        'python-decouple',
    ],

    extras_require={
        'prod': [
            'django-xff',
            'django-redis',
            'waitress',
            'raven',
        ],
        'dev': [
            'django-debug-toolbar',
        ],
    },

)
