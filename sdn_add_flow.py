import requests
import json

# OpenDayLight RESTCONF API settings
odl_url = 'http://18.224.172.254:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow/1'
odl_username = 'admin'
odl_password = 'admin'

# Flow rule to add
flow_rule = {
    "flow": [
        {
            "id": "1",
            "match": {
                "ethernet-match": {
                    "ethernet-type": {
                        "type": "0x0800"
                    }
                }
            },
            "instructions": {
                "instruction": [
                    {
                        "order": "0",
                        "apply-actions": {
                            "action": [
                                {
                                    "order": "0",
                                    "output-action": {
                                        "output-node-connector": "2"
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "priority": "1000",
            "table_id": "0"
        }
    ]
}

def add_flow_rule():
    headers = {'Content-Type': 'application/json'}
    response = requests.put(odl_url, auth=(odl_username, odl_password), headers=headers, data=json.dumps(flow_rule))
    if response.status_code in [200, 201]:
        print("Flow rule added successfully.")
    else:
        print(f"Failed to add flow rule. Status code: {response.status_code}")

if __name__ == "__main__":
    add_flow_rule()
