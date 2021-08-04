import requests
import json
from pprint import pprint as pp
from tabulate import tabulate
from secret import *
#the variable pwd requires a seperate file named secret.py with the variable pwd = {'username': 'insert username here', 'password': 'insert password here'} with the two fields being filed in

login = requests.post("https://api.extremecloudiq.com/login", json=pwd)
login_text = json.loads(login.text)
authkey = {}
authkey["Authorization"] = "Bearer " + login_text["access_token"]
devices = requests.get("https://api.extremecloudiq.com/devices?page=1&limit=100", headers = authkey)
devlist = devices.json()
id2device = {}
for device in devlist['data']:
    id2device[device['id']] = device
clients = requests.get("https://api.extremecloudiq.com/clients/active", headers = authkey)
clientlist = []
for client in clients.json()['data']:
    clientlist.append([client['id'], client['hostname'], client['ip_address'], client['mac_address'], client['ssid'], client['device_id'], id2device[client['device_id']]['hostname'], id2device[client['device_id']]['ip_address']])
print(tabulate(clientlist, headers=['CL_ID', 'CL_Name', 'CL_IP', 'CL_MAC', 'CL_SSID', 'Dev_ID', 'Dev_Name', 'Dev_IP']))