import requests

# OpenDayLight RESTCONF API settings.
odl_url = 'http://18.224.172.254:8181/restconf/operational/network-topology:network-topology'
odl_username = 'admin'
odl_password = 'admin'

# Fetch information from API.
response = requests.get(odl_url, auth=(odl_username, odl_password))

# Check if the request was successful
if response.status_code == 200:
    # Find information about nodes in retrieved JSON file.
    for nodes in response.json()['network-topology']['topology']:

        # Walk through all node information.
        node_info = nodes['node']

        # Look for MAC and IP addresses in node information.
        for node in node_info:
            try:
                ip_address = node['host-tracker-service:addresses'][0]['ip']
                mac_address = node['host-tracker-service:addresses'][0]['mac']
                print(f'Found host with MAC address {mac_address} and IP address {ip_address}')
            except KeyError:
                pass
else:
    print(f"Failed to fetch data from OpenDayLight. Status code: {response.status_code}")
(venv) ubuntu@ip-172-31-27-55:~/arun$ python3 sdn_test.py 
(venv) ubuntu@ip-172-31-27-55:~/arun$ cat sdn_test.py 
import requests

# OpenDayLight RESTCONF API settings.
odl_url = 'http://18.224.172.254:8181/restconf/operational/network-topology:network-topology'
odl_username = 'admin'
odl_password = 'admin'

# Fetch information from API.
response = requests.get(odl_url, auth=(odl_username, odl_password))

# Check if the request was successful
if response.status_code == 200:
    # Find information about nodes in retrieved JSON file.
    for nodes in response.json()['network-topology']['topology']:

        # Walk through all node information.
        node_info = nodes['node']

        # Look for MAC and IP addresses in node information.
        for node in node_info:
            try:
                ip_address = node['host-tracker-service:addresses'][0]['ip']
                mac_address = node['host-tracker-service:addresses'][0]['mac']
                print(f'Found host with MAC address {mac_address} and IP address {ip_address}')
            except KeyError:
                pass
else:
    print(f"Failed to fetch data from OpenDayLight. Status code: {response.status_code}")
