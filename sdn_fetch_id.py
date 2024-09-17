import requests

# OpenDaylight RESTCONF API settings
url = 'http://192.168.0.105:8181/restconf/operational/opendaylight-inventory:nodes'
username = 'admin'
password = 'admin'

response = requests.get(url, auth=(username, password))
if response.status_code == 200:
    nodes = response.json().get('nodes', {}).get('node', [])
    for node in nodes:
        if node['id'] == 'openflow:1':
            print(f"ID for s1: {node['id']}")
else:
    print(f"Failed to retrieve nodes. Status code: {response.status_code}")
