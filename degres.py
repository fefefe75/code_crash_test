# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht

# Initialize the DHT device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D18)

while True:
    try:
        # Read temperature in Celsius and humidity
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        
        # Print the values to the serial port
        print("Temp: {:.1f} C    Humidity: {}% ".format(temperature_c, humidity))

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
