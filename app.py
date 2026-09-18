from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def hottest(devices):
    return max(devices, key=lambda x: x["temp"])

def average_temp(devices):
    total = sum(device["temp"] for device in devices)
    return total / len(devices) if devices else 0 


@app.get ("/devices")                # task 1: all devices
def all_devices():
    return readings


@app.get("/devices/hottest")             # task 2: hottest
def get_hottest():
    return hottest(readings)

@app.get("/devices/online")              # task 3: online
def online_devices():
    return [d for d in readings if d["online"]]

