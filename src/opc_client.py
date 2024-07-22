from opcua import Client

# OPC server connection details
# Modify with your OPC server, ensure port access is allowed, especially if traversing networks.
server_url = "opc.tcp://localhost:4840"
client = Client(server_url)

try:
    client.connect()

    # Example: Read data from OPC server
    # This is a base read call
    node = client.get_node("ns=2;i=2")
    value = node.get_value()
    print("OPC value:", value)

finally:
    client.disconnect()
