from sqlite_orm.field import IntegerField, BooleanField, TextField
from sqlite_orm.table import BaseTable
import Connection from .

class ReplicaSet(BaseTable):
    __table_name__ = 'replica_set'

    ID = IntegerField(primary_key=True, auto_increment=True)
    host = TextField(not_null=True)
    port = IntegerField(not_null=True)
    connectionId = IntegerField(foreign_key=Connection.ID)