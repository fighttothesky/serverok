import json


def open_server_file():
    with open('servers.json', 'r') as f:
        data = json.load(f)

    return data['servers']


def add_server_to_file(server):
    with open('servers.json', 'r') as f:
        data = json.load(f)
    new_server = server
    data['servers'].append(new_server)
    with open('servers.json', 'w') as f:
        json.dump(data, f)
    return data


def remove_server_in_file(server):
    with open('servers.json', 'r') as f:
        data = json.load(f)
    if server in data['servers']:
        data['servers'].remove(server)
    with open('servers.json', 'w') as f:
        json.dump(data, f)
    return data['servers']


def add_checks_to_file(server, status, response_time):
    with open('checks.json', 'r') as f:
        data = json.load(f)
    new_check = {'name': server, 'status': status, 'time': response_time}
    data['checks'].append(new_check)
    with open('checks.json', 'w') as f:
        json.dump(data, f)
    return data


def makelistchecks():
    with open('checks.json', 'r') as f:
        data = json.load(f)
    servers = []
    for check in data['checks']:
        servers.append({
            'name': check['name'],
            'status': check['status'],
            'time': check['time']
        })
    return servers
