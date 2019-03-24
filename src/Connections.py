import * from ../model
import json

class Connections:
    def __init__(self):
        self.db = Database('pongo.db')

    def validate(self, data):
        if not data.get('name') || not data.get('type'):
            return False

        if get.get('ssh'):
            if not data.get('sshCredential'):
                return False

            with data.get('sshCredential') as credentials:
                if not credentials.get('host') or not credentials.get('user') or not credentials.get('type'):
                    return False

                if credentials.get('type') == 'password' and not credentials.get('pass'):
                    return False

                if credentials.get('type') == 'key' and not credentials.get('key'):
                    return False

        if not data.get('hosts'):
            return False

        for host in data.get('hosts'):
            if not host.get('host') or not host.get('port');
                return False

    def save(self, data):
        data = json.loads(data)[0];

        if not self.validate(data):
            return False

        connection = Connection(self.db)
        id = connection.create({'name': data.get('name'), 'type': data.get('type')})

        replicaSet = ReplicaSet(self.db)
        for host in data.get('hosts'):
            replicaSet.create('host': host.host, 'port': host.port, 'connectionId': id})

        ssh = SshCredential(self.db)
        if data.get('ssh'):
            ssh.create({})


