# Assignment 3
A cloud-based IoT system which collects data from a set of virtual sensors that are deployed to collect environmental information using the MQTT protocol.  This project displays the latest sensor data values received from all the sensors of a specified environmental station. 

# Description 
In this project I designed  and simulated a smart home environment using Wokwi for circuit simulation, ThingSpeak for data monitoring, and integrated them using both  and MQTT protocols. I implemented various sensors and actuators commonly found in smart homes and utilized both protocols for communication between the simulated environment and ThingSpeak for real-time monitoring.

# Objectives (What I learned)
1. Understood the concepts of MQTT protocols.
2. Learned how to simulate electronic circuits using Wokwi
3. Integrated the simulated environment with ThingSpeak using MQTT protocols for data monitoring and control.

#Requirements
1. Access to Wokwi platform (s://wokwi.com/)
2. ThingSpeak account (s://thingspeak.com/)
3. components: ESP32 microprocessor, sensors (e.g., temperature sensor, motion sensor).

# Steps:
## Step 1:  Setting up Wokwi Environment  and create a new simulation project. 
## Step 2:  Simulating Sensors
          1. Add components to Wokwi simulation for sensors (e.g., temperature sensor, motion sensor).
          2. Write code to interact with sensors and actuators, simulating basic smart home functionaliities.
## Step 3:  integrating with ThingSpeak 
          1. Set up a new channel in ThingSpeak for data logging.
          2. Modify the code to send sensor data to ThingSpeak using  requets at regular intervals.
## Step 4:  Integrating with ThingSpeak using MQQT protocol 
          1. Set up an MQTT broker for communication.
          2. Configure ThingSpeak's MQTT broker settings. 
          3. Modify your code to publish sensor data to ThingSpeak using MQTT protocol.
## Step 5: Real-time Monitoring
          Explore ThingSpeak's visualization tools to monitor sensor data in real-time.

          
