from datetime import datetime
import random

# Link to lux value ranges
# https://www.engineeringtoolbox.com/light-level-rooms-d_708.html

def determineLightLevel(hour):
    if hour >= datetime(hour=0) and hour < datetime(hour=4):
        return random.uniform(0.0001, 0.0011)
    elif hour >= datetime(hour=4) and hour < datetime(hour=5):
        return random.uniform(0.0011, 0.0108)
    elif hour >= datetime(hour=5) and hour < datetime(hour=6):
        return random.uniform(1.08, 10.8)
    elif hour >= datetime(hour=6) and hour < datetime(hour=7):
        return random.randint(107, 1075)
    elif hour >= datetime(hour=7) and hour < datetime(hour=8):
        return random.randint(1075, 10752)
    elif hour >= datetime(hour=8) and hour < datetime(hour=10):
        return random.randint(10752, 50000)
    elif hour >= datetime(hour=10) and hour < datetime(hour=12):
        return random.randint(50000, 107527)
    elif hour >= datetime(hour=12) and hour < datetime(hour=13):
        return random.randint(107527, 120000)
    elif hour >= datetime(hour=13) and hour < datetime(hour=15):
        return random.randint(50000, 107527)
    elif hour >= datetime(hour=15) and hour < datetime(hour=17):
        return random.randint(10752, 50000)
    elif hour >= datetime(hour=17) and hour < datetime(hour=18):
        return random.randint(1075, 10752)
    elif hour >= datetime(hour=18) and hour < datetime(hour=19):
        return random.randint(107, 1075)
    elif hour >= datetime(hour=19) and hour < datetime(hour=20):
        return random.uniform(10.8, 107)
    elif hour >= datetime(hour=20) and hour < datetime(hour=21):
        return random.uniform(1.08, 10.8)
    elif hour >= datetime(hour=21) and hour < datetime(hour=22):
        return random.uniform(1.08, 10.8)
    elif hour >= datetime(hour=22) and hour < datetime(hour=23):
        return random.uniform(0.0108, 0.108)
    elif hour >= datetime(hour=23) and hour < datetime(hour=0):
        return random.uniform(0.0011, 0.0108)