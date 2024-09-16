import requests
import networkx as nx
import matplotlib.pyplot as plt

# OpenDayLight RESTCONF API settings
odl_url = 'http://18.224.172.254:8181/restconf/operational/network-topology:network-topology'
odl_username = 'admin'
odl_password = 'admin'

def fetch_topology():
    response = requests.get(odl_url, auth=(odl_username, odl_password))
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from OpenDayLight. Status code: {response.status_code}")
        return None

def visualize_topology(data):
    G = nx.Graph()
    for topology in data['network-topology']['topology']:
        for node in topology['node']:
            G.add_node(node['node-id'])
        for link in topology['link']:
            G.add_edge(link['source']['source-node'], link['destination']['dest-node'])
    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    data = fetch_topology()
    if data:
        visualize_topology(data)
