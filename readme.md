## NAC for ExtremeCloud
This python script gets you a list of information about clients, such as their ID, what device they are connected to, et cetera.

## Program in Curl
- `curl -X POST -H 'Content-Type: application/json' -d '{"username": "insert username here", "password": "insert password here"}' https://api.extremecloudiq.com/login`
- Output:`{"access_token":"Very long key"}`
- This gets us the api key that we will use throughout the rest of the program
- However, any time we use it later, I will simply replace it should have `Bearer ` added before it any time it is used
- `curl -X GET -H 'Authorization: Bearer XXXXXXXXXXX' 'https://api.extremecloudiq.com/devices?page=1&limit=100'`
- Output:`{"page":1,"count":100,"data":[{"id":XXXXX,"hostname":"XXXXX","connected":true,"create_time":"XXXXX","update_time":"XXXXX","org_id":X,"serial_number":"XXXXX","service_tag":"","mac_address":"XXXXX","device_function":"DEVICE_FUNCTION_AP","product_type":"XXXXX","ip_address":"XXX.XXX.XXX.XXX","software_version":"X.X.X.X","device_admin_state":"DEVICE_ADMIN_STATE_MANAGED","last_connect_time":"XXXXX"}],"total_pages":1,"total_count":1}`
	- It will output more data if there are more devices connected
	- This command will get us the list of devices, though it can only get 100 at a time
- `curl -X GET -H 'Authorization: Bearer XXXXXXXXXXX' https://api.extremecloudiq.com/clients/active'`
	- This command gets a list of all active clients in 1 go
- Both of these lists give us detailed information about the client or device, however the client only details what the ID of the device it is connecting to, and not any more information, to get that information, you need to create a ID to Device table
### Banning Devices
- To ban a device, you must first get what SSID it is on, and what the ID sof the device it is connecting to is, and what the client's MAC address is, which are both on the client list
- `curl -X POST -H 'Authorization: XXXXXXXXXXX' -H 'Content-Type: application/json' -d '{"devices": {"ids": [XXXXXX]}, "clis": ["security mac-filter SSID address MAC_ADDRESS deny"]}' https://api.extremecloudiq.com/devices/:cli`
	- Replace SSID with the ssid you want to ban the client from, replace the MAC_ADDRESS with the mac address of the client you want to ban and replace IDS with the IDs of the devices you want to ban the client from, it should be a list
	- This command allows you to ban a specific client by sending a CLI command
