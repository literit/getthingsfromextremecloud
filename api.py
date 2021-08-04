import requests
import json
from pprint import pprint as pp
from secret import *
#the variable pwd requires a seperate file named secret.py with the variable pwd = {'username': 'insert username here', 'password': 'insert password here'} with the two fields being filed in

login = requests.post("https://api.extremecloudiq.com/login", json=pwd)
#print(login.text)
login_text = json.loads(login.text)
#print(login_text)
authkey = {}
authkey["Authorization"] = "Bearer " + login_text["access_token"]
#print(authkey["Authorization"])
#print(type(authkey))
clients = requests.get("https://api.extremecloudiq.com/clients/active", headers = authkey)
#pp(json.loads(clients.text))
pp(clients.json())
print("\n\n\n")
devices = requests.get("https://api.extremecloudiq.com/devices?page=1&limit=100", headers = authkey)
pp(devices.json())
print("\n\n\n")
network_policies = requests.get("https://api.extremecloudiq.com/network-policies?page=1&limit=100", headers = authkey)
pp(network_policies.json())
print("\n\n\n")
ssids = requests.get("https://api.extremecloudiq.com/ssids?page=1&limit=100", headers = authkey)
pp(ssids.json())