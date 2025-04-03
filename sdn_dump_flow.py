import requests
import json

# OpenDayLight RESTCONF API settings
base_odl_url = 'http://13.201.123.107:8181/restconf/operational/opendaylight-inventory:nodes/node/openflow:1/table/0'
odl_username = 'admin'
odl_password = 'admin'

def dump_flow_rules():
    """Fetch and print all flow rules from OpenDaylight."""
    headers = {'Accept': 'application/json'}
    response = requests.get(base_odl_url, auth=(odl_username, odl_password), headers=headers)
    
    if response.status_code == 200:
        flows = response.json()
        print("Flow Rules:")
        print(json.dumps(flows, indent=4))
    else:
        print(f"Failed to retrieve flow rules. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    print("Dumping flow rules:")
    dump_flow_rules()
