import SshCredential as SshCredentialTable from ../table

class SshCredential:
    def __init__(self, db):
        self.db = db

    def findById(self, id):
        return self.db.query(ReplicaSetTable).filter(SshCredentialTable.ID == id).select().execute()

    def update(self, id, date):
        self.db.query(ReplicaSetTable).update(data).filter(SshCredentialTable.ID == id).execute()
        return True

    def create(self, data):
        replicaSet = SshCredentialTable(data)
        cursor = self.db.query().insert(replicaSet).execute()
        return cursor.lastrowid

    def remove(self, id):
        db.query().delete().filter(SshCredentialTable.ID == id).execute()