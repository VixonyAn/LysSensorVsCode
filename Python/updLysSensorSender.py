from socket import *
from datetime import datetime
import time
import random
import json

BROADCAST_IP = '255.255.255.255'
PORT = 32000

socket_sender = socket(AF_INET, SOCK_DGRAM)
socket_sender.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


def generateDatapoint():
    date = datetime.now()
    light_dict = {
        "Date": "",
        "IsDrawn": False,
        "LightsOn": False,
        "LightLevel": ""
    }
    return light_dict

for _ in range(100):
    light_dict = generateDatapoint()
    message = json.dumps(light_dict)
    print(f'Broadcaster sending: {message}')
    socket_sender.sendto(message.encode(), (BROADCAST_IP, PORT))
    time.sleep(2)
    
socket_sender.close()