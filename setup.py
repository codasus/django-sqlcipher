from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

VERSION = '0.1'

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']


setup(
    name='django-sqlcipher',
    version=VERSION,
    description="SQLCipher support for Django",
    long_description="This module allows your Django project to work with SQLCipher.",
    author="Codasus Technologies",
    author_email="contact@codasus.com",
    url="http://github.com/codasus/django-sqlcipher",
    license="Creative Commons Attribution-ShareAlike 3.0 Unported License",
    platforms=["any"],
    packages=['sqlcipher'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Security :: Cryptography",
    ],
    include_package_data=True,
)
