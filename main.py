import threading
import requests
import queue
import re

success = []

count = input("How many threads would you like to use? ")

url = 'https://172.16.20.100:9443/samlsso?spEntityID=travelocity.com'

header_data = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

user = {'Authorization': 'Basic <Base64Encoded[admin:admin]>'}


def do_request():
    response = requests.post(url, headers=header_data, data=user, verify=False)
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
