from ../model import *
import json

class Connections:
    def __init__(self):
        self.db = Database('pongo.db')

    def validate(self, data):
        if not data.get('name') || not data.get('type'):
            return False

        if get.get('isSSH'):
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
        if date.get('id'):
            connection.update({'name': data.get('name'), 'type': data.get('type')})
            id = data.get('id')
        else:
            id = connection.create({'name': data.get('name'), 'type': data.get('type')})

        if data.get('ssh'):
            self.handleSSH(data.get('sshCredential'), id);

        if data.get('hosts'):
            self.handleHosts(data.get('hosts'), id)

    def handleSSH(self, data, id):
        ssh = SshCredential(self.db)

        details = {}
        if id:
            details = ssh.getByConnection(id)

        keys = ['host', 'user', 'pass', 'type', 'port', 'connectId', 'key']
        data = {k: v for k,v in data.items()}

        if len(a) > 0:
            detials.update(data);
            ssh.update(data)
        else:
            ssh.create(data)

    def handleHost(self, data, id):
        replicaSet = new ReplicaSet(self.db)
        replicaSet.removeConnectionHosts(id)

        for host in data:
            host.delete('id')
            replicaSet.create(host)


