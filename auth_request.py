import requests
import json

api_url = '<zabbix URL>/zabbix/api_jsonrpc.php'

headers = {'content-type': 'application/json'}

auth_data = {"jsonrpc": "2.0","method": "user.login","params": {"user": "USERNAME","password": "PASSWORD"},"id":1,"auth": None}

connect = requests.post(api_url, data=json.dumps(auth_data), headers=headers, verify=False)

reply = connect.json()

print(reply['result'])