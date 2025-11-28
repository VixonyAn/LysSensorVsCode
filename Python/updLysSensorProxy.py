from socket import *
import requests
import json
import time

PORT = 32000

socket_reciever = socket(AF_INET, SOCK_DGRAM)
socket_reciever.bind(('', PORT))

print("Proxy UDP ready")
print(f"Listening for incoming messages on PORT {PORT}")

REST_API_URL = "http://localhost:####/api/"

while True:
    msg, addr = socket_reciever.recvfrom(3000)
    msg_str = msg.decode()
    print(f"UDP Broadcaster {addr} sent the following message: {msg_str}")
    msg_obj = json.loads(msg_str)
    new_time = time.time()
    msg_obj["TimeTurnedOn"] = new_time
        
    response = requests.post(REST_API_URL, json=msg_obj)
    print(f"Response from REST API: {response.status_code} -- {response.text}")
