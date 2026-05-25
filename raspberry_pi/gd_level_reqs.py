# this is micro-python for a raspberry pi pico, this will not work with normal python

import time
import network
import sys
import requests
import json

ssid = "Vodafone9E3760"
password = "PZ4H23ZLemHJptgd"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(ssid, password)

timeout = 10
while timeout > 0:
    status = wlan.status()
    print("Status:", status)

    if status < 0 or status >= 3:
        break

    timeout -= 1
    time.sleep(1)

if wlan.status() != 3:
    print("Failed to connect")
    sys.exit(1)
print("Connected")


def request_level(ID):
    req = requests.get(f"http://gdladder.com/api/level/{str(ID)}")
    print(f"STATUS CODE: {req.status_code}")
    level = json.loads(req.content)
    req.close()

    print()
    print(f"===== {level['Meta']['Name']} =====")
    print(f"ID: {level['Meta']['ID']}")
    print(f"Description: {level['Meta']['Description']}")
    print(f"Made by: {level['Meta']['Publisher']['name']}")
    print(f"In-game difficulty: {level['Meta']['Difficulty']} Demon")
    print(f"GDDL difficulty: {round(level['Rating'], 1)}")
    print()


request_level(3)
request_level(10565740)
request_level(118509879)
