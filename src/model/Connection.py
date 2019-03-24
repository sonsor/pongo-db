import Connection as ConnectionTable from ../table
import ReplicaSet as ReplicaSetTable from ../table
import SshCrendtial as SshCredentialTable from ../table

class Connection:
    def __init__(self, db):
        self.db = db

    def findById(self, id):
        result = self.db.query(ConnectionTable).filter(ConnectionTable.ID == id).select().execute()

    def update(self, id, date):
        self.db.query(ConnectionTable).update(data).filter(ConnectionTable.ID == id).execute()

    def create(self, data):
        connection = ConnectionTable(data)
        cursor = self.db.query().insert(connection).execute()
        return cursor.lastrowid

    def remove(self, id):
        replica = ReplicaSet(self.db)
        ssh = new SshCredential(self.db)
        replica.findAndRemove(ReplicaSetTable.connectionId, id)
        ssh.findAndRemove(SshCredentialTable.connectionId(), id)
        db.query().delete().filter(ConnectionTable.ID === id).execute()
