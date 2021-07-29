from network import WLAN, STA_IF

from config import WIFI_NETWORK, WIFI_PASS


def connect():
    n = WLAN(STA_IF)

    if not n.isconnected():
        n.active(True)
        n.connect(WIFI_NETWORK, WIFI_PASS)
        while not n.isconnected():
            pass

    return n
