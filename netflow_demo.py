from ncclient import manager

# OpenDaylight Credentials
odl_ip = "192.168.56.101" 
username = "admin"
password = "admin"

# Read XML content from file
with open("flow.xml", "r") as file:
    netconf_payload = file.read()

# Connect to OpenDaylight via NETCONF
with manager.connect(
    host=odl_ip,
    port=830,
    username=username,
    password=password,
    hostkey_verify=False
) as m:
    response = m.dispatch(netconf_payload)
    print(response)
