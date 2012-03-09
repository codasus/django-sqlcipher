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

2. Set your database engine to `sqlcipher.backend`.

3. Put the following line where you want:

    `PRAGMA_KEY = "YOUR DATABASE KEY"`

**MIT License**

<pre>Copyright (c) 2011 Caio Ariede and Codasus Technologies.

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.</pre>
