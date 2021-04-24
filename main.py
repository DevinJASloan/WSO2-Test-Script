import threading
import requests

count = input("How many threads would you like to use?")

url = 'https://172.16.20.200:9443/api/identity/auth/v1.1/authenticate'

data = {
    'Authorization': 'Basic <Base64Encoded[admin:admin]>',
    'Content-Type': 'application/json',
    'username': 'admin',
    'password': 'admin'
}


def do_request():
    response = requests.post(url, data=data)
    print(response)


threads = []

for i in range(int(count)):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(int(count)):
    threads[i].start()

for i in range(int(count)):
    threads[i].join()
