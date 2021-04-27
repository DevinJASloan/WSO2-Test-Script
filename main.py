import threading
import requests

count = input("How many threads would you like to use?")

url = 'https://172.16.20.100:9443/samlsso?spEntityID=travelocity.com'

user = {
    'Authorization': 'Basic <Base64Encoded[admin:admin]>',
}


def do_request():
    response = requests.post(url, data=user, verify=False)
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
