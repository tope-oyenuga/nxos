#Show interfaces from a switch
import json
import requests

print ("enter ip address of the switch")
ip=input ()

print ('what interface do you want to check? e.g. eth 1/1')
interface = input ()

my_headers = {'content-type': 'application/json-rpc'}
url = "http://"+ip+"/ins"
username = "admin"
password = "Cisco321"

#Json-rpc payload
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "sh ip int "+interface,
      "version": 1
    },
    "id": 1
  }
]

#Post the payload to the switch in a json-rpc format to get a response and save it
response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()

#Now Process the response
#First check if the interface is disabled/unconfigured
if response['result']['body']['TABLE_intf']['ROW_intf']['ip-disabled'] == 'TRUE':
	print ('This interface is disabled')
#If it isn't disabled, then go ahead to search for its details
else:
	Int1 = response['result']['body']['TABLE_intf']['ROW_intf']['intf-name']
	link_state = response['result']['body']['TABLE_intf']['ROW_intf']['link-state']
	intf_ip = response['result']['body']['TABLE_intf']['ROW_intf']['prefix']
	mask = response['result']['body']['TABLE_intf']['ROW_intf']['masklen']
#chassis_id = response['result']['body']['chassis_id']
#hostname =  response['result']['body']['host_name']

	print ("The interface is : {0} it has an ip of {2}/{3} and it is {1}".format(Int1, link_state, intf_ip, mask))
#print ("ip : {0} is a \"{1}\" with hostname: {2} running software version : {3}".format(ip , chassis_id, hostname, kick_start_image))