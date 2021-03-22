import requests
return_json = {'username':'leoamber', 'password':'amberlab'}
req = requests.post('http://192.168.1.9:5000/login', json=return_json)
print('Response: {}\n'.format(req.text))
print('json: {}\n'.format(req.json))