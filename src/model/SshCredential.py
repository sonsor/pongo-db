import SshCredential as SshCredentialTable from ../table

class SshCredential:
    def __init__(self, db):
        self.db = db

    def findById(self, id):
        return self.db.query(SshCredentialTable).filter(SshCredentialTable.ID == id).select().execute()

    def update(self, id, date):
        self.db.query(SshCredentialTable).update(data).filter(SshCredentialTable.ID == id).execute()
        return True

    def create(self, data):
        sshCredential = SshCredentialTable(data)
        cursor = self.db.query().insert(sshCredential).execute()
        return cursor.lastrowid

    def remove(self, id):
        db.query().delete().filter(SshCredentialTable.ID == id).execute()

    def getByConnection(self, id):
        return db.query(SshCredentialTable).filter(SshCredentialTable.connectionId == id).execute()