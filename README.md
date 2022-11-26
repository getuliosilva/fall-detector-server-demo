# Fall Detector Server Demo

## About

This repository is part of a [Distributed Systems](https://www.freecodecamp.org/news/a-thorough-introduction-to-distributed-systems-3b91562c9b3c/) class project. The project is an internet-connected fall detector using the [ESP32 MCU](https://www.espressif.com/en/products/socs/esp32).

This repository contains the [Python](https://www.python.org/) code to simulate the fall detector, the server that receives fall alerts and a phone application that notifies the user when a fall is detected.

## Running the code

### 1. Download the repository

Click the green *Code* button, then click *Download ZIP*. Or clone the repository using [Git](https://git-scm.com/):

`git clone https://github.com/getuliosilva/fall-detector-server-demo.git`

### 2. [Download and install Python](https://wiki.python.org/moin/BeginnersGuide/Download)

### 3. Install de dependencies

Using [pip](https://pip.pypa.io/en/stable/) run:

`pip install flask-restful `

### 4. Run the programs

These instructions are valid for [Ubuntu](https://ubuntu.com/desktop) 20.04.1 LTS, but should work for any operating system.
Open three terminals on the repository folder. 

On the first terminal run:

`python3 server.py`

On the second terminal run:

`python3 sensor.py`

On the third terminal run:

`python3 phone.py`

## Using the programs

The second terminal simulates the sensor. On the second terminal, press the *1* key, then press the *Enter* key on your keyboard. This will cause the sensor to detect a fall and send an alert to the server on the first terminal. On the third terminal, the phone will show a message telling you that a fall was detected. The alerts should disappear after five seconds.
