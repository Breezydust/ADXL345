# SmartWatch 
Implementing the accelerometer portion of a SmartWatch IOT project using the Adafruit ADXL345 and a Raspberry Pi 3

## Table of Contents
1. [Introduction](#Introduction)
2. [Build Instructions](#build-instructions)
3. [System Diagram]()
4. [Material/Budget](#Materials-Budget)
5. [Time Commitment](#Time-Commitment)
6. [Mechanical Assembly](#Mechanical-Assembly)
7. [PCB](#PCB-Soldering)
8. [Power Up](#Power-Up)
9. [Unit Testing](#Unit-Testing)
10. [Production](#Production-Testing)

## Introduction
This project is to implement the Adafruit ADXL345 accelerometer into a development platform. The ADXL345 is soldered on to a custom-designed PCB to allow for plug-and-pluy functionality with our Raspberry Pi 3 development platform. Firmware was written to interface with the connected sensor, and an enclosure was designed to hold the Pi and sensor assembly. 

The accelerometer (the Adafruit ADXL345) is a  low-power, 3-axis MEMS accelerometer with both I2C and SPI interfaces. It was chosen due to its low-cost, very small power budget, and advanced functionality including freefall and tap detection. The Raspberry Pi 3 is an ARM-based 64-bit single board computer with a large developer community and support - a perfect development platform for integrating multiple sensors into a final working product.

Once complete, this project can be integrated alongside other sensors to provide more complex functionality and handle more applications. This project in particular is part of a multi-semester group project to integrate an accelerometer, pulse sensor and a temperature sensor alongside an appropriate enclosure and development platform in order to create a smartwatch device.

