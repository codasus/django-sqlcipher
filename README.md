**django-sqlcipher**

SQLCipher is an SQLite extension that provides transparent 256-bit AES encryption of database files.

In order to encrypt a new database or query existing data you must key it before using it.

This app does it for you. You only need to specify the database key in your project's `settings.py` file.

For more about SQLCipher take a look at [http://sqlcipher.net/](http://sqlcipher.net/).

**Requirements**

* python-sqlcipher (Python compiled with SQLCipher support)

For more about python-sqlcipher take a look at:

[https://code.launchpad.net/~jplacerda/+junk/python-sqlcipher](https://code.launchpad.net/~jplacerda/+junk/python-sqlcipher)

**Installation**

`pip install git+http://github.com/codasus/django-sqlcipher#egg=sqlcipher`

Or manually place it on your `PYTHON_PATH`.

**Configuration**

Open your project's `settings.py` file and:

1. Append `sqlcipher` to your `INSTALLED_APPS`.

2. Put the following line where you want:

    `PRAGMA_KEY = "YOUR DATABASE KEY"`

**License**

django-sqlcipher by [Codasus Technologies](http://codasus.com) is licensed under a [Creative Commons Attribution-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-sa/3.0/).

You are free:

* to Share - to copy, distribute and transmit the work
* to Remix - to adapt the work
* to make commercial use of the work
