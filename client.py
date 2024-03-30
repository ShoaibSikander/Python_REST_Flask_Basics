print('I am Client .....')

import json
import requests

client_username = 'user'
client_password = '123'

IP = 'localhost'
port = '5000'
connect = IP+':'+port

headers = {'Content-Type': 'application/json'}

data_dict = {'first_name':'Muhammad Shoaib', 'last_name':'Sikander', 'age':32, 'height':177.8}
data_person = json.dumps(data_dict)

response = requests.post('http://'+connect+'/Person_Detail', headers=headers, data=data_person, auth=(client_username, client_password))
response = response.json()
full_name = response['full_name']
print('Full Name: ', full_name)