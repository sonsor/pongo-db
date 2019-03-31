import ReplicaSet as ReplicaSetTable from ../table

class ReplicaSet:
    def __init__(self, db):
        self.db = db

    def findById(self, id):
        result = self.db.query(ReplicaSetTable).filter(ReplicaSetTable.ID == id).select().execute()

    def update(self, id, date):
        self.db.query(ReplicaSetTable).update(data).filter(ReplicaSetTable.ID == id).execute()

    def create(self, data):
        replicaSet = ReplicaSetTable(data)
        cursor = self.db.query().insert(replicaSet).execute()
        return cursor.lastrowid

    def remove(self, id):
        db.query().delete().filter(ReplicaSetTable.ID ==     id).execute()

    def removeConnectionHosts(self, id)
        db.query().delete().filter(ReplicaSetTable.connectionId == id).execute()