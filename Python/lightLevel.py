import random

# Link to lux value ranges
# https://www.engineeringtoolbox.com/light-level-rooms-d_708.html

def determineLightLevel(hour):
    if hour >= 0 and hour < 4:
        return random.uniform(0.0001, 0.0011)
    elif hour >= 4 and hour < 5:
        return random.uniform(0.0011, 0.0108)
    elif hour >= 5 and hour < 6:
        return random.uniform(1.08, 10.8)
    elif hour >= 6 and hour < 7:
        return random.randint(107, 1075)
    elif hour >= 7 and hour < 8:
        return random.randint(1075, 10752)
    elif hour >= 8 and hour < 10:
        return random.randint(10752, 50000)
    elif hour >= 10 and hour < 12:
        return random.randint(50000, 107527)
    elif hour >= 12 and hour < 13:
        return random.randint(107527, 120000)
    elif hour >= 13 and hour < 15:
        return random.randint(50000, 107527)
    elif hour >= 15 and hour < 17:
        return random.randint(10752, 50000)
    elif hour >= 17 and hour < 18:
        return random.randint(1075, 10752)
    elif hour >= 18 and hour < 19:
        return random.randint(107, 1075)
    elif hour >= 19 and hour < 20:
        return random.uniform(10.8, 107)
    elif hour >= 20 and hour < 21:
        return random.uniform(1.08, 10.8)
    elif hour >= 21 and hour < 22:
        return random.uniform(1.08, 10.8)
    elif hour >= 22 and hour < 23:
        return random.uniform(0.0108, 0.108)
    elif hour >= 23 and hour < 24:
        return random.uniform(0.0011, 0.0108)