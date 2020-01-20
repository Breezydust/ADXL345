# ADXL345
Designing and implementing a plug-and-play accelerometer board using an AdaFruit ADXL345 for use with a Raspberry Pi 3 development platform.

## Table of Contents
1. [Introduction](#Introduction)
2. [BOM/Budget](#Bill-of-Materials-and-Budget)
3. [Time Commitment](#Time-Commitment)
4. [Mechanical Assembly](#Mechanical-Assembly)
5. [PCB Design and Soldering](#PCB-Design-and-Soldering)
6. [Power Up](#Power-Up)
7. [Unit Testing](#Unit-Testing)
8. [Production](#Production-Testing)

## Introduction
This project is to implement the Adafruit ADXL345 accelerometer into a development platform. The ADXL345 is soldered on to a custom-designed PCB to allow for plug-and-play functionality with our Raspberry Pi 3 development platform. Firmware was written to interface with the connected sensor, and an enclosure was designed to hold the Pi and sensor assembly. 

The accelerometer (the Adafruit ADXL345) is a  low-power, 3-axis MEMS accelerometer with both I2C and SPI interfaces. It was chosen due to its low-cost, very small power budget, and advanced functionality including freefall and tap detection. The Raspberry Pi 3 is an ARM-based 64-bit single board computer with a large developer community and support - a perfect development platform for integrating multiple sensors into a final working product.

Once complete, this project can be integrated alongside other sensors to provide more complex functionality and handle more applications. This project in particular is part of a multi-semester group project to integrate an accelerometer, pulse sensor and a temperature sensor alongside an appropriate enclosure and development platform in order to create a smartwatch device.

## Bill of Materials and Budget
The total price of the project - assuming nothing is owned before hand - is around 320CAD. A spreadsheet with up-to-date pricing (at the time of project completion) and links can be found [here](https://github.com/Breezydust/ADXL345/blob/master/Documentation/ADXL345Budget_No_Preowned.xlsx).

![](https://github.com/Breezydust/ADXL345/blob/master/Images/ADXL345Budget_No_Preowned_Image.png)

## Time Commitment
The project was completed from scratch over a 15-week semester, with an average weekly time commitment of 160 minutes. Certain parts of the project (PCB design and soldering) took longer.

Assuming that all parts of the project have been acquired and the person building the project is familiar with the concepts covered in the guide (setting up a development platform, hardware soldering, etc.) the entire project can be completed within a weekend.

![](https://github.com/Breezydust/ADXL345/blob/master/Images/ProjectTimelineImage_readme.png)

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
  
  8. From another computer, open any remote-connection app. On macOS, use Finder's *Connect to..* utility (CMD+K within Finder). On a Windows computer, the *Remote Desktop Connection* application can be used. Alternatively, RealVNC's *[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)* can be used on any platform, and is generally the most reliable means of connecting.
  Enter the IP address you noted above. The application will prompt you for a username and password - the Pi's default username is `pi` and the default password is `raspberry`. Enter these credentials, and the Pi's graphical interface should appear on the computer you are using. You are now controlling the Pi remotely!
  
  9. At this stage, all the software required for the development platform has been installed and configured. The Pi can be shutdown using the menu bar option, or by entering `sudo powerdown` into the terminal. Once the Pi is off, all the cables can be unplugged and the Pi set aside until later.
  
**Step 2: Breadboarding and Prototyping**
This step will outline basic sensor connectivity using jumper wires and a breadboard. The design and layout established in this step will carry over to PCB design and soldering.

  1. Gather the following items: Breadboard, ADXL345 Sensor, and 4 Female-to-Male GPIO cables. 
  
  2. Identify the correct pins on the sensor. For basic I2C functionality, the following four pin should be used: 3V3, GND, SDA and SCL.
  
  ![](https://github.com/Breezydust/ADXL345/blob/master/Images/ADXL345_Physical_Board.jpg)
  
  3. Identify the corresponding pins on your development platforms GPIO header. On the Raspberry Pi 3, the correct pins are 1, 3, 5 and 6. [This website](https://pinout.xyz/#) can be used for pin references.
  
  4. Line the sensor up with holes on the main part of the breadboard, and insert the male-end of the jumper cables into the pins previously identified. Insert the female end of each cable into the matching GPIO pin on the Raspberry Pi. 
  
  In my implementation, the 3V3 and GND connections were jumped to dedicated rails on the outside of the breadboard. This can be skipped, as it only provides a slight stability increase and allows for shared power across a single breadboard - which does not apply to this project.
  
  The connection should look similar to this:
  
  ![](https://github.com/Breezydust/ADXL345/blob/master/Images/Breadboard_setup_picture.png)
  
  5. When your physical connections are secured, plug in your peripherals into the Raspberry Pi and power it on.
  
  6. Following the directions established above, create a remote desktop connection to the Pi. Use the ip address that you noted when preparing your platform initially - the login credentials should be the same.
  
  7. Open a terminal, and enter `i2cdetect -y 1`. A fair bit of information should be displayed - look for the number *53*; this is your sensor's i2c address, and signifies a successful connection to the sensor.
  
  At this point, breadboard prototyping is complete and sensor functionality has been verified. It is time to move on the designing and soldering a plug-and-play PCB.

## PCB Design and Soldering
PCB design and soldering is the most crucial step to this project. PCB cutting is a time-consuming and costly process, and any errors in design will most likely require your board to be re-printed. If you have access to a dedicated production lab (like I did through my school), mistakes are less detrimental.

Regardless, it is heavily advised to ensure that your design is correct prior to any cutting being done. 

**Step 1: Fritzing**
[Fritzing](https://fritzing.org/home/) is an open-source application that allows users to create PCB schematics for a variety of development platforms. It's highly customizable, extensible and is generally very user-friendly.

  1. [Download](https://fritzing.org/download/) and extract Fritzing. Installation notes for a variety of operating systems are listed on the download site.
  
  2. [Download](https://github.com/adafruit/Fritzing-Library) and install the AdaFruit Fritzing Library. This will allow you to import a digital ADXL345 sensor for easier design.
  
  3. Fritz! Create the appropriate connections, ensuring that any traces do not cross. Try to get your board to be as compact as possible. Alternatively, you can use my fritzing file found [here](https://github.com/Breezydust/ADXL345/blob/master/Electronics/ADXL345Breadboard.fzz).
  
  4. Export as a Gerber file. `File > Export for Production > Extended Gerber` and select an easily-accessible folder. These files are the standard filetype used to etch and cut physical PCBs.
  
  5. Compress the Gerber files, and send them to your etcher of choice. I used the [Humber Prototyping Lab](https://www.humber.ca/research/prototyping-lab/).
  
**Step 2: Soldering**
Once the PCB has been etched, it's time to solder. Ensure that you work in a well-ventilated area, wearing safety glasses and using an iron that you are comfortable with. Beginners can watch [this](https://www.youtube.com/watch?v=oqV2xU1fee8) video for tips.
 
  1. Gather your ADXL345 sensor, a length of copper wire, a wire stripper, a 9-pin double-sided header (should've come with your sensor), a 6-pin stackable header, your PCB, solder and a soldering iron.
  
  2. Solder the 9-pin header to the sensor board. To make this easier, you can place the extended pins into a breadboard, and place the sensor on the shorter pins. This ensures a sturdy connection.
    
  3. Solder the vias on your PCB. The easiest method for this is to strip a copper wire, and place it through the via into a breadboard. Solder all vias on the exposed side, and then flip and repeat for the opposite side.
  
  4. Solder the sensor to the PCB. You will need to rest the PCB on a flat surface for this, as there is no way to access the extended pins while they are mounted. 
  
  5. Solder the stackable header on to the PCB. Although only 5 pins all used, all 6 should be soldered to ensure stability when attached to the Pi.
  
  ![](https://github.com/Breezydust/ADXL345/blob/master/Images/ADXL345_PCB_Top.jpeg)
  
  At this point, soldering is complete. Attach your soldered board to the appropriate GPIO pins on the Pi, and get ready for further testing.

## Power Up
With all peripherals plugged into your Pi, power it on. As above, establish a remote desktop connection, and rerun the `i2cdetect -y 1` command within a terminal.

If everything is in working order, you will be greeted with a terminal output similar to this:

  ![](https://github.com/Breezydust/ADXL345/blob/master/Images/ADXL345_i2cDetect.png)

## Unit Testing
All testing thus far has been to verify that the sensor is in working condition, and that there is a valid connection to the Pi. Further testing needs to be done - particularly in verifying that acceleration values can be read off the sensor and displayed in real-time.

  1. Download the python file found [here](https://github.com/Breezydust/ADXL345/blob/master/Firmware/ADXL345.py) and save it to your home directory.
  
  2. Open a terminal, and navigate to your home directory using `cd ~`. 
  
  3. Run the script by entering `python3 ADXL345.py`. It will prompt you for basic or advanced measurements. Basic measurements include acceleration in the X, Y and Z coordinates. Advanced measurements also include tap detection, movement detection, and freefall detection.
  
  You should get readings similar to this: 
  
  ![](https://github.com/Breezydust/ADXL345/blob/master/Images/ADXL345_scriptTest.png)
  
  Try moving the sensor around - readings are polled every .5s, and updated immediately.
  
At this point, the project is more or less complete. You have a functioning sensor on a custom-designed PCB, allowing for plug-and-play functionality with your development platform. All that remains is production testing, and the discussion of possible integration within other projects.

## Production Testing
Schematics for an acrylic case can be found [here](https://github.com/Breezydust/SmartWatch/blob/master/Mechanical/ADXL345_Enclosure_CorelDraw.cdr). The case encloses the Pi and the board, has a cutout for tapping the sensor, and is sturdy enough to withstand reasonable freefall detection testing.

This concludes the build instructions for this project.
