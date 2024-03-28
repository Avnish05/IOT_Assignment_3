import network
import time
import urandom
from umqtt.simple import MQTTClient

# ThingSpeak MQTT broker details
mqtt_client_id = "HCoqCBILISg7BxwoIwwxGSg"
mqtt_user = "HCoqCBILISg7BxwoIwwxGSg"
mqtt_password = "AHT4dSISRXgMnH2fCAwA78+v"
mqtt_server = "mqtt3.thingspeak.com"
mqtt_port = 1883
mqtt_topic_temperature = "channels/2488600/publish/fields/field1"
mqtt_topic_humidity = "channels/2488600/publish/fields/field2"
mqtt_topic_co2 = "channels/2488600/publish/fields/field3"

# Wi-Fi details
WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

# Historical data storage
historical_data = []

# Function to generate random sensor values
def generate_sensor_data():
    random_temperature = urandom.uniform(-50, 50)
    random_humidity = urandom.uniform(0, 100)
    # Ensure CO2 value is within the acceptable range (300 to 2000 ppm)
    random_co2 = urandom.uniform(300, 2000)
    return random_temperature, random_humidity, random_co2

# Function to publish data to ThingSpeak
def publish_to_thingspeak(temperature, humidity, co2):
    client = MQTTClient(mqtt_client_id, mqtt_server, user=mqtt_user, password=mqtt_password)
    client.connect()
    client.publish(mqtt_topic_temperature, str(temperature))
    client.publish(mqtt_topic_humidity, str(humidity))
    client.publish(mqtt_topic_co2, str(co2))
    client.disconnect()

# Connect to Wi-Fi
wifi_interface = network.WLAN(network.STA_IF)
wifi_interface.active(True)
wifi_interface.connect(WIFI_SSID, WIFI_PASSWORD)

# Wait for Wi-Fi connection
while not wifi_interface.isconnected():
    pass

print("Connected to Wi-Fi")

# Main loop to generate and publish sensor data
while True:
    temp, hum, co2 = generate_sensor_data()
    historical_data.append((temp, hum, co2))  # Store historical data
    if len(historical_data) > 720:  # Approximately 5 hours with data every 5 seconds
        historical_data.pop(0)  # Remove oldest data point if exceeds 5 hours
    publish_to_thingspeak(temp, hum, co2)
    print("Published: Temperature={:.2f}C, Humidity={:.2f}%, CO2={:.2f}ppm".format(temp, hum, co2))
    time.sleep(5)  # Adjust the delay as needed (Reduced to 5 seconds for faster data entry)
