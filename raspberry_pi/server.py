# this is micro-python for a raspberry pi pico, this will not work with normal python

import time
import network
from sys import exit
import socket
import asyncio
from machine import Pin


def get_html() -> str:
    return """\
HTTP/1.1 200 OK

<!DOCTYPE html>
<html>
<head><title>Pico Server</title></head>
<body>
<h1>Hello from Pico W</h1>
<p>If you're seeing this, it somehow works.</p>
</body>
</html>
"""


def set_up_wlan() -> dict:
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
        exit(1)
    print("Connected")
    return wlan


async def blink_led(led):
    led.value(1)
    await asyncio.sleep(0.3)
    led.value(0)
    print("blinked LED")


async def server(sock, led, webpage):
    while True:
        client, addr = sock.accept()
        print(f"Client from {addr}")

        request = client.recv(1024)
        print("Request:", request)

        asyncio.create_task(blink_led(led))

        client.send(webpage)
        client.close()

        await asyncio.sleep(0)  # yield control


async def main():
    led = Pin("LED", Pin.OUT)
    wlan = set_up_wlan()
    led.value(0)

    html = get_html()

    port = 80
    sock = socket.socket()
    while True:
        try:
            addr = socket.getaddrinfo("0.0.0.0", port)[0][-1]
            sock.bind(addr)
            break
        except:
            port += 1
    sock.listen(1)
    print(f"Pico IP: {wlan.ifconfig()[0]}:{port}")

    await server(sock, led, html)


asyncio.run(main())
