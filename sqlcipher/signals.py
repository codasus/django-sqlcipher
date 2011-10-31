from django.conf import settings
from django.db.backends.signals import connection_created


def sqlite_set_pragma(connection, **kwargs):
    pragma_sql = "PRAGMA key='%s';" % (settings.PRAGMA_KEY,)
    cursor = connection.cursor()
    cursor.execute(pragma_sql)
    cursor.close()


def setup():
    connection_created.connect(sqlite_set_pragma)


setup()
