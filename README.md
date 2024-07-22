# OPC Server to SAP ERP Integration

## Overview
This project aims to integrate data from an OPC server into SAP ERP system using Python. The OPC server provides real-time data which is then processed and imported into SAP ERP through RFC (Remote Function Call) functions.

## Requirements
- Python 3.x
- OPC UA server (e.g., Prosys OPC UA Simulation Server)
- SAP ERP system with RFC enabled

## Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/opc-erp-integration.git
   cd opc-erp-integration

2. **Install Dependencies**
	'''python
	pip install -r requirements.txt

3. **Configuration**
Update opc_client.py with your OPC server connection details.
Update sap_erp_integration.py with your SAP ERP connection parameters and RFC function names.

Usage
Run opc_client.py to connect to the OPC server, retrieve data, and send it to SAP ERP using sap_erp_integration.py.

Files
opc_client.py: Python script to connect to OPC UA server and retrieve data.
sap_erp_integration.py: Python script to integrate data into SAP ERP using SAP RFC functions.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License. See the LICENSE file for more details.