import requests
import json

# OpenDayLight RESTCONF API settings
base_odl_url = 'http://13.201.123.107:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow'
odl_username = 'admin'
odl_password = 'admin'


def delete_flow_rule(flow_id):
    """Delete a specific flow rule by ID."""
    delete_url = f"{base_odl_url}/{flow_id}"
    headers = {'Content-Type': 'application/json'}
    
    response = requests.delete(delete_url, auth=(odl_username, odl_password), headers=headers)
    
    if response.status_code in [200, 204]:
        print(f"Flow rule {flow_id} deleted successfully.")
    else:
        print(f"Failed to delete flow rule {flow_id}. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":

    
    flow_id_to_delete = "1"  # Change this ID as needed
    print(f"\nDeleting flow rule with ID {flow_id_to_delete}:")
    delete_flow_rule(flow_id_to_delete)
