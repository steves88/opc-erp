from pyrfc import Connection
from sqlalchemy import create_engine, MetaData, Table, select

# SAP connection parameters
conn = Connection(user='USERNAME',
                  passwd='PASSWORD',
                  ashost='SAP-SYSTEM-HOST',
                  sysnr='SYS-NUMBER',
                  client='CLIENT',
                  lang='EN')

# OPC data to SAP function
def send_to_sap(data):
    try:
        conn.open()
        # Example: Insert data into SAP using RFC function
        # Ensure you update the RFC function name below as per your SAP instance
        result = conn.call('RFC_FUNCTION_NAME', PARAM1=data['param1'], PARAM2=data['param2'])
        print("Data sent to SAP:", result)
    finally:
        conn.close()

if __name__ == "__main__":
    # Example usage
    data_to_send = {"param1": "value1", "param2": "value2"}
    send_to_sap(data_to_send)
