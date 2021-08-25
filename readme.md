## NAC for ExtremeCloud
This python script gets you a list of information about clients, such as their ID, what device they are connected to, et cetera.

## Program in Curl
- `curl -XPOST -H "Content-type: application/json" -d '{'username': 'insert username here', 'password': 'insert password here'}' 'https://api.extremecloudiq.com/login'`
- This gets us the api key that we will use throughout the rest of the program
- However, any time we use it later, I will simply replace it with `api_key`, and it should have `Bearer ` added before it any time it is used
- `curl -XGET -H 'Authorization: auth_key' -H "Content-type: application/json" -d '{'username': 'insert username here', 'password': 'insert password here'}' 'https://api.extremecloudiq.com/devices?page=1&limit=100'`
- This command will get us the list of devices, though it can only get 100 at a time
- `curl -XGET -H 'Authorization: auth_key' -H "Content-type: application/json" -d '{'username': 'insert username here', 'password': 'insert password here'}' 'https://api.extremecloudiq.com/clients/active'`
- This command gets a list of all active clients in 1 go
- Both of these lists give us detailed information about the client or device, however the client only details what the ID of the device it is connecting to, and not any more information, to get that information, you need to create a ID to Device table
### Banning Devices
- To ban a device, you must first get what SSID it is on, and what the ID of the device it is connecting to is, and what the client's MAC address is, which are both on the client list
- `curl -XPOST -H 'Authorization: auth_key' -H "Content-type: application/json" -d '{"devices" : { "ids" : ["insert ID of device here"] }, "clis" : ["security mac-filter [insert SSID] address [insert MAC of client here] deny' 'https://api.extremecloudiq.com/devices/:cli'`
- This command allows you to ban a specific client by sending a CLI command to the device it is connected to