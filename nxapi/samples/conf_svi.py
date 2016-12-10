import requests
import json

print ("enter ip address of switch")
ip = input ()

print ("enter vlan for which svi has to be configured")
vlanId = input ()

print ("enter ip of the svi")
ip_vlanId = input()

myheaders = {'content-type': 'application/json-rpc'}
url = ("http://"+ip+"/ins")
username = ("admin")
password = ("Cisco321")

payload=[
   {"jsonrpc": "2.0","method": "cli","params": {"cmd": "conf t","version": 1},"id": 1},
   {"jsonrpc": "2.0","method": "cli","params": {"cmd": "feature interface-vlan","version": 1},"id": 2},
   {"jsonrpc": "2.0","method": "cli","params": {"cmd": "interface vlan "+str(vlanId),"version": 1},"id": 3},
   {"jsonrpc": "2.0","method": "cli","params": {"cmd": "ip address "+str(ip_vlanId )+"/24","version": 1},"id": 4},
   {"jsonrpc": "2.0","method": "cli","params": {"cmd": "no shut","version": 1},"id": 5},
]

response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()
