# SmartWatch 
Implementing the accelerometer portion of a SmartWatch IOT project using the Adafruit ADXL345 and a Raspberry Pi 3

## Table of Contents
1. [Introduction](#Introduction)
2. [System Diagram](#System-Diagram)
3. [BOM/Budget](#Bill-of-Materials-and-Budget)
4. [Time Commitment](#Time-Commitment)
5. [Mechanical Assembly](#Mechanical-Assembly)
6. [PCB Design and Soldering](#PCB-Design-and-Soldering)
7. [Power Up](#Power-Up)
8. [Unit Testing](#Unit-Testing)
9. [Production](#Production-Testing)

## Introduction
This project is to implement the Adafruit ADXL345 accelerometer into a development platform. The ADXL345 is soldered on to a custom-designed PCB to allow for plug-and-play functionality with our Raspberry Pi 3 development platform. Firmware was written to interface with the connected sensor, and an enclosure was designed to hold the Pi and sensor assembly. 

The accelerometer (the Adafruit ADXL345) is a  low-power, 3-axis MEMS accelerometer with both I2C and SPI interfaces. It was chosen due to its low-cost, very small power budget, and advanced functionality including freefall and tap detection. The Raspberry Pi 3 is an ARM-based 64-bit single board computer with a large developer community and support - a perfect development platform for integrating multiple sensors into a final working product.

Once complete, this project can be integrated alongside other sensors to provide more complex functionality and handle more applications. This project in particular is part of a multi-semester group project to integrate an accelerometer, pulse sensor and a temperature sensor alongside an appropriate enclosure and development platform in order to create a smartwatch device.


## System Diagram
Placeholder

## Bill of Materials and Budget
Placeholder

## Time Commitment
Placeholder

## Mechanical Assembly
**Step 1: Preparing your development platform**
This step will outline how to prepare the project's development platform - the Raspberry Pi 3B+. This process *should* be the same on any older Raspberry Pi models (1B+, 2B+), and very similar to the newest model (4B), notwithstanding any port changes.

  1. Download the latest [Raspberry Pi image](https://www.raspberrypi.org/downloads/). NOOBS (New Out Of Box Software) is recommended, as it includes the latest Raspbian operating system, a variety of useful software tools pre-installed, and a selection of alternate operating systems should you choose to repurpose the Pi after the project is complete.
  
  2. Prepare your microSD card for imaging. Plug the card into any computer, and unzip the downloaded image to an easily-accessible folder on your computer - like the Desktop or Documents. Using a utility like [balenaEtcher](https://www.balena.io/etcher/), flash the unzipped image to the inserted microSD card. Once complete, unmount or safely eject the card. **Note:** If you are familiar with the command line (or would like to tinker with it for educational purposes), follow the instructions [here](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md) to setup your microSD card without any third-party utilities.
  
  3. Insert the prepared microSD card into the port located on the bottom-side of the Pi. Insert a keyboard, mouse, HDMI cable and Ethernet cable into the Pi. Ensure the HDMI cable is connected to a functioning display, and then plug in the micro-usb power adapter to power on the Pi.
  
  4. Upon booting, a splash screen with a variety of operating system options will appear. Select **Raspbian** and follow the on-screen prompts to configure your installation. The install process should take a few minutes. Once complete, the Pi will automatically restart to the the Desktop screen.
  
  5. Configure more connectivity options to your Pi. Open the *terminal* application, and enter `sudo raspi-config`. Navigate to *Interfacing options* and enable both **VNC** and **I2C**. VNC will allow for remote graphical connections to the Pi, and I2C will allow for physical data transfer over the I2C bus.
  
  6. Install required software tools and libraries. The I2C-tools library is a python3-based library built to interface with any device connected to the Pi's I2C bus. Python3, its dependencies, and the I2C-tools library can all be installed by entering `sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y` into the terminal, and following the prompts.
  
  7. Collect information for remote access. Once connected to the internet, open the terminal and enter `ifconfig`. Make a note of the value found next to *inet* underneath the *eth0* heading. This is the Pi's IP address, and will be used to connect to the Pi from another computer. It can change, but rarely does assuming network conditions remain consistent.
  
  8. From another computer, open any remote-connection app. For macOS, use Finder's *Connect to..* utility (CMD+K within Finder). On a Windows computer, the *Remote Desktop Connection* application can be used. Alternatively, RealVNC's *[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)* can be used on any platform, and is generally the most reliable means of connecting.
  Enter the IP address you noted above. The application will prompt you for a username and password - the Pi's default username is `pi` and the default password is `raspberry`. Enter these credentials, and the Pi's graphical interface should appear on the computer you are using. You are now controlling the Pi remotely!
  
  9. At this stage, all the software required for the development platform has been installed and configured. The Pi can be shutdown using the menu bar option, or by entering `sudo powerdown` into the terminal. Once the Pi is off, all the cables can be unplugged and the Pi set aside until later.
  

## PCB Design and Soldering
Placeholder

## Power Up
Placeholder

## Unit Testing
Placeholder

## Production Testing
Placeholder
