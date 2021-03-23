import requests
import os

user = os.getlogin()
file = open('/home/{}/Desktop/ContratoMouser/papelada'.format(user), 'rb')
files = {'file': ('papelada', file)}
req = requests.post('http://192.168.1.9:5000/upload', files=files)
print("\nstatus:",req.text)
print("\njson:", req.json)