from sqlite_orm.field import IntegerField, BooleanField, TextField
from sqlite_orm.table import BaseTable

class Connection(BaseTable):
    __table_name__ = 'connections'

    # general connection info
    ID = IntegerField(primary_key=True, auto_increment=True)
    name = TextField(not_null=True)
    active = BooleanField(not_null=True, default_value=1)
    type = TextField(not_null=True)

    # db credentials
    dbuser = TextField(not_null=True)
    dbpass = TextField(not_null=True)
    dbname = TextField(not_null=True)

    # ssh credentials
    ssh = BooleanField(not_null=True, default_value=0)

    # ssl
    ssl = BooleanField(not_null=True, default_value=0)



