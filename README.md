# time-tracking-pi

A raspberry pi that keeps track of time spent on tasks. 
I use this to keep track of time on different tasks at work. You can start/stop a tracker with the press of a button. Current timing is output on an LCD screen. 

<img src="https://raw.githubusercontent.com/anthonyfennell/time-tracking-pi/master/topSeconds.jpg" width="400">
<img src="https://raw.githubusercontent.com/anthonyfennell/time-tracking-pi/master/topMinutes.jpg" width="400">
<img src="https://raw.githubusercontent.com/anthonyfennell/time-tracking-pi/master/topBackwards.jpg" width="50">
<img src="https://raw.githubusercontent.com/anthonyfennell/time-tracking-pi/master/topSide.jpg" width="50">
<img src="https://raw.githubusercontent.com/anthonyfennell/time-tracking-pi/master/leftSide.jpg" width="50">


# Description
This uses four pins for button input. Pressing buttons 1 and 2 simultaneously will reset all tracked time to zero. Pressing buttons 1 and 3 simultaneously will exit the program. The LCD screen will show all four times either in the form of seconds, minutes, or hours + minutes. Also, the LCD screen will display a carrot '>' in front of the time that is currently still running.

**Contents**
* LCD screen of 16x2
* Adafruit Perma-Proto HAT for Pi Mini Kit 
* Raspberry Pi B+

# Usage
1. Add the program TrackTime.py to your pi
  * This program uses GPIO.BOARD to reference the pins
2. Open the file /etc/rc.local on your pi with the following command:
  * `sudo nano /etc/rc.local`
3. Add the following line before the command `exit` and save the file. Adding this will run this program on boot and log any errors to logTrackTime.txt
  * `sudo python /path/to/TrackTime.py & > /path/to/logTrackTime.txt 2>&1`
  
# Pins (GPIO.BOARD)
### Buttons
Each button is a 3 pin button. One side goes to a pin on the Pi, center pin goes to **3.3V** (Pi pin 1).
The program sets up the Pi to use a pull down* resistor on each pin that a button is wired to.
- Button 1 :: 11 (BCM 17)
- Button 2 :: 13 (BCM 27)
- Button 3 :: 12 (BCM 18)
- Button 4 :: 18 (BCM 24)
### LCD pin - Pi pin (4-bit mode)
- Pin 1 :: Pi 6 **GND**
- Pin 2 :: Pi 2 **5V**
- Pin 3 :: Potentiometer center pin (Other sides go to GND and 5V)
- Pin 4 :: Pi 15
- Pin 5 :: Pi 6 **GND**
- Pin 6 :: Pi 16
- Pin 11 :: Pi 37
- Pin 12 :: Pi 33
- Pin 13 :: Pi 31
- Pin 14 :: Pi 29
- Pin 15 :: Pi 2 **5v**
- Pin 16 :: Pi 6 **GND**





# Helpful Places
[Pi Pinout](https://pinout.xyz/)

[Using the GPIO pins](https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api)

[SSH into a raspberry pi](https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md)

[Run a program on boot](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)

[Setup an LCD with your pi](http://www.circuitbasics.com/raspberry-pi-lcd-set-up-and-programming-in-python/)

