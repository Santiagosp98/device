from urequests import post
from ujson import dumps

from config import API_URL, API_KEY, DEVICE_ID


def upload_reading(sensor_id: int, value: float):
    """Using a POST request, uploads sensor data to an API.

        :param sensor_id: The unique identifier defined by the API.
        :param value: The sensor readed data.
    """
    response = post(
        API_URL,
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Bearer " + API_KEY
        },
        data=dumps({
            "device_id": DEVICE_ID,
            "sensor_id": sensor_id,
            "value": value
        })
    )

    # Necessary to avoid getting out of memory.
    response.json()
