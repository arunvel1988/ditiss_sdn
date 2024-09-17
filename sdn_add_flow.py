import requests
import json

# OpenDayLight RESTCONF API settings
base_odl_url = 'http://192.168.0.105:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow'
odl_username = 'admin'
odl_password = 'admin'

def add_flow_rule():
    # Flow rule to drop traffic from port 1
    flow_rule = {
        "flow": [
            {
                "id": "1",  # Flow ID for addition
                "match": {
                    "in-port": "1"  # Matches packets coming from port 1
                },
                "instructions": {
                    "instruction": [
                        {
                            "order": "0",
                            "apply-actions": {
                                "action": []  # No actions -> drop the packet
                            }
                        }
                    ]
                },
                "priority": "1000",  # Set a high priority for this rule
                "table_id": "0"
            }
        ]
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{base_odl_url}/1", auth=(odl_username, odl_password), headers=headers, data=json.dumps(flow_rule))
    
    if response.status_code in [200, 201]:
        print("Flow rule added successfully.")
    else:
        print(f"Failed to add flow rule. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    add_flow_rule()
