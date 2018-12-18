import requests

url = 'http://192.168.1.97:8072/parse'

params = {'sentence':"我想知道你是谁？",'returnType':'text'}
r = requests.post(url,data=params,  headers={'content-type':'application/x-www-form-urlencoded'})
print(r.status_code)
print(r.content.decode())

