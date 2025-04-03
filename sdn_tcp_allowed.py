import requests
import json

# OpenDayLight RESTCONF API settings
base_odl_url = 'http://13.201.123.107:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/table/0/flow'
odl_username = 'admin'
odl_password = 'admin'

def add_flow_rule(flow_id, flow_rule):
    """Push a flow rule to OpenDaylight."""
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f"{base_odl_url}/{flow_id}", auth=(odl_username, odl_password), headers=headers, data=json.dumps(flow_rule))
    
    if response.status_code in [200, 201]:
        print(f"Flow rule {flow_id} added successfully.")
    else:
        print(f"Failed to add flow rule {flow_id}. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    # Rule to allow TCP traffic on port 80
    allow_rule = {
        "flow": [
            {
                "id": "10",
                "priority": "2000",
                "table_id": "0",
                "match": {
                    "ethernet-match": {
                        "ethernet-type": {
                            "type": 2048
                        }
                    },
                    "ipv4-source": "10.0.0.1/32",
                    "ipv4-destination": "10.0.0.3/32",
                    "ip-match": {
                        "ip-protocol": 6
                    },
                    "tcp-destination-port": 80
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
                                            "output-node-connector": "NORMAL"
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    }

    # Rule to drop all other traffic from h1 to h3
    drop_rule = {
        "flow": [
            {
                "id": "11",
                "priority": "1000",
                "table_id": "0",
                "match": {
                    "ethernet-match": {
                        "ethernet-type": {
                            "type": 2048
                        }
                    },
                    "ipv4-source": "10.0.0.1/32",
                    "ipv4-destination": "10.0.0.3/32"
                },
                "instructions": {
                    "instruction": [
                        {
                            "order": "0",
                            "apply-actions": {
                                "action": []
                            }
                        }
                    ]
                }
            }
        ]
    }

    print("Adding flow rule to allow HTTP traffic from h1 to h3:")
    add_flow_rule("10", allow_rule)

    print("Adding flow rule to block all other traffic from h1 to h3:")
    add_flow_rule("11", drop_rule)
