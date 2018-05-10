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
The LCD I am using is 16x2.

# Usage
1. Add the program TrackTime.py to your pi
2. Open the file /etc/rc.local on your pi with the following command:
  * `sudo nano /etc/rc.local`
3. Add the following line before the command `exit` and save the file. Adding this will run this program on boot and log any errors to logTrackTime.txt
  * `sudo python /path/to/TrackTime.py & > /path/to/logTrackTime.txt 2>&1`



# Helpful Places
[Using GPIO pins](https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api)
[SSH into pi](https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md)
[Run program on boot](https://www.raspberrypi.org/documentation/linux/usage/rc-local.md)
[Setup LCD](http://www.circuitbasics.com/raspberry-pi-lcd-set-up-and-programming-in-python/)
