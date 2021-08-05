import requests
import json
from pprint import pprint as pp
from tabulate import tabulate
from secret import *
#The variable pwd requires a seperate file named secret.py with the variable pwd = {'username': 'insert username here', 'password': 'insert password here'}

LIMIT_OF_DATA_SENT = '2'

#Login to api
login = requests.post("https://api.extremecloudiq.com/login", json=pwd)

#Create authentication key from the given access token
login_text = login.json()
authkey = {}
authkey["Authorization"] = "Bearer " + login_text["access_token"]

#Gets list of devices and their data
devices = requests.get("https://api.extremecloudiq.com/devices?page=1&limit=" + LIMIT_OF_DATA_SENT, headers = authkey)

#Bypasses pagination of the device list, also creates a translation table for device IDs to actual device data
id2device = {}
for i in range(devices.json()['total_pages']):
    currentdevices = requests.get("https://api.extremecloudiq.com/devices?page=" + str(i + 1) +"&limit=" + LIMIT_OF_DATA_SENT, headers = authkey)
    for device in currentdevices.json()['data']:
        id2device[device['id']] = device

#Gets list of clients and their data
clients = requests.get("https://api.extremecloudiq.com/clients/active", headers = authkey)

#creates a list of client and device data
clientlist = []
for client in clients.json()['data']:
    clientlist.append([client['id'], client['hostname'], client['ip_address'], client['mac_address'], client['ssid'], client['device_id'], id2device[client['device_id']]['hostname'], id2device[client['device_id']]['ip_address']])
print(tabulate(clientlist, headers=['CL_ID', 'CL_Name', 'CL_IP', 'CL_MAC', 'CL_SSID', 'Dev_ID', 'Dev_Name', 'Dev_IP']))