from django.db.backends.sqlite3.base import DatabaseWrapper as BaseDatabaseWrapper

from ..signals import setup


class DatabaseWrapper(BaseDatabaseWrapper):
    def _cursor(self):
        if self.connection is None:
            setup()
        return super(DatabaseWrapper, self)._cursor()
