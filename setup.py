try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A template package with py.test testing',
    'author': 'Danny Lynch',
    'url': 'https://github.com/danny31415/py3template',
    'download_url': 'https://github.com/danny31415/py3template',
    'author_email': 'danny31415@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['py3template'],
    'scripts': [],
    'name': 'py3template',
}

setup(**config)

