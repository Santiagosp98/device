"""
Main boot file.
"""
from machine import Pin
from dht import DHT11
from utime import sleep

from config import SENSOR_CELSIUS, SENSOR_FAHRENHEIT, SENSOR_HUMIDITY, SENSOR_CO
from mq9 import MQ9

from service import upload_reading
from wifi import connect

DHT11 = DHT11(Pin(13))
MQ9 = MQ9(Pin(32))


def main():
    """
    Boot function. Connects to Wi-Fi network, loops indefinitely while reading sensor data.
    """
    wifi = connect()

    if wifi.isconnected():
        while True:
            DHT11.measure()

            upload_reading(SENSOR_CELSIUS, DHT11.temperature())
            upload_reading(SENSOR_FAHRENHEIT, DHT11.temperature() * 2)
            upload_reading(SENSOR_HUMIDITY, DHT11.humidity())
            upload_reading(SENSOR_CO, MQ9.gas())

            sleep(0.5)


if __name__ == '__main__':
    main()
