import requests
import json

print ("enter ip address of switch")
ip = input ()

#get the interface to be configured
print ("what interface would you like to configure, e.g interface 'eth 1/1'")
int_id = input ()

#print ("is this interface: 'routed' or an 'access' port?")
#port_type = ()

#if port_type = "routed"
#   port = "no switchport" 

#get ip address of interface
print ("enter ip of the interface, e.g. 'A.B.C.D/SM'")
int_ip = input()

myheaders = {'content-type': 'application/json-rpc'}
url = ("http://"+ip+"/ins")
username = ("admin")
password = ("Cisco321")

payload = [
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "conf t",
      "version": 1
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "interface "+int_id,
      "version": 1
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "no switchport",
      "version": 1
    },
    "id": 3
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "ip address "+int_ip,
      "version": 1
    },
    "id": 4
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "no shut",
      "version": 1
    },
    "id": 5
  },
]


response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(username,password)).json()