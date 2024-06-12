# Raspberry Pi Distance Sensor Video Trigger

This repository contains Python code to interface a distance sensor with a Raspberry Pi. The sensor detects objects within a specified range and triggers an HDMI output to play a designated video. This project can be used for interactive exhibits, security systems, or any application requiring sensor-triggered media playback.
Table of Contents

    Installation
    Hardware Requirements
    Software Requirements
    Setup
    Usage
    Contributing
    License

Installation

Clone the repository to your local machine:

bash

git clone https://github.com/cthadeufaria/raspberrypi-hdmi-output.git
cd raspberrypi-hdmi-output

Hardware Requirements

    Raspberry Pi (any model with GPIO pins)
    HC-SR04 Ultrasonic Distance Sensor (or compatible)
    HDMI compatible display
    Connecting wires and a breadboard
    Resistors for voltage divider

Software Requirements

    Python 3.x
    RPi.GPIO library
    opencv library (for video playback)

Install the required Python libraries:

bash

pip install -r requirements.txt

Setup
Wiring the Distance Sensor

    Connect the VCC pin of the HC-SR04 to the 5V pin of the Raspberry Pi.
    Connect the GND pin of the HC-SR04 to the GND pin of the Raspberry Pi.
    Connect the TRIG pin of the HC-SR04 to GPIO pin 18 of the Raspberry Pi.
    Connect the ECHO pin of the HC-SR04 to GPIO pin 24 of the Raspberry Pi.

Configuring the Code

Edit the config.py file to set the GPIO pins and the video file path:

python

config.py

Path to the video file
VIDEO_PATH = "/path/to/your/video/"

Usage

Run the Python script to start the distance sensor and video trigger system:

bash

python rpi_control.py

The system will continuously monitor the distance sensor. When an object is detected within the specified range, the video will be played on the connected HDMI display.
Script Overview

    sensor.py: Contains functions to measure distance using the HC-SR04 sensor.
    video.py: Manages video playback using pygame.
    rpi_control.py: Main script to run the sensor and video trigger logic.

Contributing

Contributions are welcome! Please fork this repository and submit pull requests.

    Fork the Project
    Create your Feature Branch (git checkout -b feature/YourFeature)
    Commit your Changes (git commit -m 'Add some YourFeature')
    Push to the Branch (git push origin feature/YourFeature)
    Open a Pull Request

License

This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to customize this README further based on your project's specific details and requirements.