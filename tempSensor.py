"""
    File name: tempSensor.py
    Author: faelb (faelb@gmx.at)
    Date created: 29/06/2020
    Date last modified: 29/06/2020
    Python Version: 3.8
   This program reads data from a DHT22 (joy-it) Temp & air humidity
   sensor.
"""
import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to: (D17 = GPIO 4)
dhtDevice = adafruit_dht.DHT22(board.D4)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} C    Humidity: {}% ".format(
                temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])

    time.sleep(2.0)
