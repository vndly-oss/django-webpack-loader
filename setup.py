import os
import re

from setuptools import setup


def rel(*parts):
    '''returns the relative path to a file wrt to the current directory'''
    return os.path.abspath(os.path.join(os.path.dirname(__file__), *parts))

README = open('README.md', 'r').read()

with open(rel('webpack_loader', '__init__.py')) as handler:
    INIT_PY = handler.read()


def get_version(filename):
  path = os.path.join(os.path.dirname(__file__), filename)
  with open(path, encoding="utf-8") as handle:
    content = handle.read()
  return re.search(r'__version__ = "([^"]+)"', content).group(1)


VERSION = get_version('webpack_loader/__init__.py')


setup(
  name = 'django-webpack-loader',
  packages = ['webpack_loader', 'webpack_loader/templatetags', 'webpack_loader/contrib'],
  version = VERSION,
  description = 'Transparently use webpack with django',
  long_description=README,
  long_description_content_type="text/markdown",
  author = 'Owais Lone',
  author_email = 'hello@owaislone.org',
  download_url = 'https://github.com/owais/django-webpack-loader/tarball/{0}'.format(VERSION),
  url = 'https://github.com/owais/django-webpack-loader', # use the URL to the github repo
  keywords = ['django', 'webpack', 'assets'], # arbitrary keywords
  classifiers = [
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Framework :: Django',
    'Environment :: Web Environment',
    'License :: OSI Approved :: MIT License',
  ],
)
