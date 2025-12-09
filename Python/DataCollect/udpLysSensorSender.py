from socket import *
from datetime import datetime
import time
import json
import lightLevel

BROADCAST_IP = '255.255.255.255'
PORT = 32000

socket_sender = socket(AF_INET, SOCK_DGRAM)
socket_sender.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)


def generateDatapoint():
    light_dict = {
        "LightValue": lightLevel.determineLightLevel(datetime.fromtimestamp(time.time()).hour)
    }
    return light_dict

for _ in range(100):
    light_dict = generateDatapoint()
    message = json.dumps(light_dict)
    print(f'Broadcaster sending: {message}')
    socket_sender.sendto(message.encode(), (BROADCAST_IP, PORT))
    time.sleep(600)
    
socket_sender.close()