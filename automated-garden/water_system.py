"""This module will handle the water system for the automated garden"""

#to do:
## investigate about Xiaomi Mi Flora (bluetooth plant sensor) and how to connect it to the system
## investigate about ESP8126 or ESP32 sensors and how to connect it to the system through wifi-
## which method is better?
## can it be read by the Raspberry Pi?
## investigat how to build the architecture

#ARCHITECTURE (first approach):
## 1. Soil sensors (ESP8266/ESP32 + sensor):
##    - Measure soil moisture and temperature
##    - Send data to Raspberry Pi via Wi-Fi
## 2. Raspberry Pi:
##    - Receives data from sensors
##    - Controls water pump based on soil moisture levels
## 3. Water Pump (pending to define details):
##    - Activated by Raspberry Pi when soil moisture is below threshold
## 4. Optional: Web interface for monitoring and control
