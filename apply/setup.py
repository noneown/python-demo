try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
'description': 'setuptools project',
'author': 'windwant',
'url': 'URL to get it at.',
'download_url': 'Where to download it.',
'author_email': 'email.',
'version': '0.1',
'install_requires': ['nose'],
'packages': find_packages(),
'scripts': [],
'name': 'apply'
 }

setup(**config)
