from socket import *
from datetime import datetime
import time
import random
import json

BROADCAST_IP = '255.255.255.255'
PORT = 32000

socket_sender = socket(AF_INET, SOCK_DGRAM)
socket_sender.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

clicked_sun = False
curtainDrawn = False
lightOn = False
    
def determineLightLevel(hour):
    if hour >= datetime(hour=0) and hour < datetime(hour=1):
        return random.randint(0.0001, 0.0011)
    elif hour >= datetime(hour=1) and hour < datetime(hour=2):
        return random.randint(0.0001, 0.0011)
    elif hour >= datetime(hour=2) and hour < datetime(hour=3):
        return random.randint(0.0001, 0.0011)
    elif hour >= datetime(hour=3) and hour < datetime(hour=4):
        return random.randint(0.0001, 0.0011)
    elif hour >= datetime(hour=4) and hour < datetime(hour=5):
        return random.randint(0.0001, 0.0108)
    elif hour >= datetime(hour=5) and hour < datetime(hour=6):
        return random.randint(1.08, 10.8)
    elif hour >= datetime(hour=6) and hour < datetime(hour=7):
        return random.randint(107, 1075)
    elif hour >= datetime(hour=7) and hour < datetime(hour=8):
        return random.randint(1075, 10752)
    elif hour >= datetime(hour=8) and hour < datetime(hour=9):
        return random.randint(10752, 50000)
    elif hour >= datetime(hour=9) and hour < datetime(hour=10):
        return random.randint(10752, 50000)
    elif hour >= datetime(hour=10) and hour < datetime(hour=11):
        return random.randint(50000, 107527)
    elif hour >= datetime(hour=11) and hour < datetime(hour=12):
        return random.randint(50000, 107527)
    elif hour >= datetime(hour=12) and hour < datetime(hour=13):
        return random.randint(107527, 120000)
    elif hour >= datetime(hour=13) and hour < datetime(hour=14):
        return random.randint(50000, 107527)
    elif hour >= datetime(hour=14) and hour < datetime(hour=15):
        return random.randint(50000, 107527)
    elif hour >= datetime(hour=15) and hour < datetime(hour=16):
        return random.randint(10752, 50000)
    elif hour >= datetime(hour=16) and hour < datetime(hour=17):
        return random.randint(10752, 50000)
    elif hour >= datetime(hour=17) and hour < datetime(hour=18):
        return random.randint(1075, 10752)
    elif hour >= datetime(hour=18) and hour < datetime(hour=19):
        return random.randint(107, 1075)
    elif hour >= datetime(hour=19) and hour < datetime(hour=20):
        return random.randint(10.8, 107)
    elif hour >= datetime(hour=20) and hour < datetime(hour=21):
        return random.randint(1.08, 10.8)
    elif hour >= datetime(hour=21) and hour < datetime(hour=22):
        return random.randint(21, 40)
    elif hour >= datetime(hour=22) and hour < datetime(hour=23):
        return random.randint(0.108, 1.08)
    elif hour >= datetime(hour=23) and hour < datetime(hour=0):
        return random.randint(0.0108, 0.108)

def DrawCurtain():
    if not curtainDrawn:
        curtainDrawn = True
    else:
        curtainDrawn = False
        
def SwitchLight():
    if not lightOn:
        lightOn = True
    else:
        lightOn = False
        
def clickedNight():
    lightOn = False
    curtainDrawn = True

def generateDatapoint():
    date = datetime.now()
    light_dict = {
        "Date": date,
        "IsDrawn": curtainDrawn,
        "LightsOn": lightOn,
        "LightLevel": determineLightLevel(date.hour)
    }
    return light_dict
