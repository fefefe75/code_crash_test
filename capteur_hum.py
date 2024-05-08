import Adafruit_DHT
import time

# Spécifiez le modèle du capteur (DHT11 ou DHT22) et la broche GPIO à laquelle il est connecté.
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Remplacez 4 par le numéro de la broche GPIO à laquelle votre capteur est connecté.

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Température={0:0.1f}°C  Humidité={1:0.1f}%".format(temperature, humidity))
    else:
        print("Lecture du capteur a échoué. Réessayer...")
    time.sleep(2)  # Attendre quelques secondes avant de lire à nouveau les données du capteur=

