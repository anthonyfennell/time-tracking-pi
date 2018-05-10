import RPi.GPIO as GPIO
from RPLCD import CharLCD
import time

# Using pin setup GPIO.BOARD numbering for pins
ledPin = 7
buttonOnePin = 11
buttonTwoPin = 13
buttonThreePin = 12
buttonFourPin = 18

### Begin class TimeTracker
class TimeTracker:
  elapsedTimeString = ""
  __startTime = time.time()
  __isRunning = False
  __elapsedTime = 0.0
  
  def __init__(self, pin):
    self.pin = pin

  def buttonPressed(self):
    if self.__isRunning:
      self.__stopTimer()
    else:
      self.__startTimer()
    time.sleep(.1)

  def reset(self):
    self.__isRunning = False
    self.__elapsedTime = 0.0

  def __stopTimer(self):
    self.__isRunning = False
    self.__elapsedTime = time.time() - self.__startTime + self.__elapsedTime

  def __startTimer(self):
    self.__isRunning = True
    self.__startTime = time.time()

  def isTimeUpdated(self):
    # Check if elapsed time has updated
    currentElapsedTime = self.__getElapsedTimeString()
    if currentElapsedTime != self.elapsedTimeString:
      self.elapsedTimeString = currentElapsedTime
      return True
    else:
      return False

  def __getElapsedTimeString(self):
    runningCharacter = ""
    trackedTime = 0.0
    timeString = "0s"
    
    if self.__isRunning:
      # Show carrot when a timer is running
      runningCharacter = ">"
      trackedTime = time.time() - self.__startTime + self.__elapsedTime
    else:
      trackedTime = self.__elapsedTime

    if self.getHours(trackedTime) > 0:
      # Display hours and minutes
      timeString = "%s%dh%dm" % (runningCharacter, self.getHours(trackedTime), self.getMinutes(trackedTime))
    elif self.getMinutes(trackedTime) > 0:
      # Display minutes
      timeString = "%s%dm" % (runningCharacter, self.getMinutes(trackedTime))
    else:
      # Display seconds
      timeString = "%s%ds" % (runningCharacter, self.getSeconds(trackedTime))

    return timeString.ljust(7)

  def getSeconds(self, trackedTime):
    return trackedTime % 60

  def getMinutes(self, trackedTime):
    return int(trackedTime / 60) % 60

  def getHours(self, trackedTime):
    return int(trackedTime / 3600)
### End class TimeTracker


# Global methods
def setupGPIO():
  # Setup four pins to be used with buttons
  GPIO.setup(buttonOnePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonTwoPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonThreePin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(buttonFourPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def getDefaultLCD():
  # Setup 16x2 LCD
  lcd = CharLCD(cols=16, rows=2, pin_rs=15, pin_e=16, pins_data=[36, 33, 31, 29],
		numbering_mode=GPIO.BOARD, auto_linebreaks=True, charmap="A02")
  return lcd

def resetTimeTrackers(*timeTrackers):
  for timeTracker in timeTrackers:
    timeTracker.reset()

def hasTimeChanged(*timeTrackers):
  # Check if any of the tracker's elapsed time has changed
  isNewTime = False
  for timeTracker in timeTrackers:
    if timeTracker.isTimeUpdated():
      isNewTime = True
  return isNewTime

def writeTimeToLCD(lcd, button1, button2, button3, button4):
  # Only update the lcd if the elapsed time has changed
  if not hasTimeChanged(button1, button2, button3, button4):
    return

  lcd.clear()
  time1 = button1.elapsedTimeString
  time2 = button2.elapsedTimeString
  time3 = button3.elapsedTimeString
  time4 = button4.elapsedTimeString
  # Write first row
  lcd.cursor_pos = (0,0)
  text1 = "%s %s" % (time1, time2)
  lcd.write_string(text1)
  # Write second row
  lcd.cursor_pos = (1,0)
  text2 = "%s %s" % (time3, time4)
  lcd.write_string(text2)


# Start program
lcd = getDefaultLCD()
setupGPIO()
# Setup a TimeTracker for each button pin
button1 = TimeTracker(buttonOnePin)
button2 = TimeTracker(buttonTwoPin)
button3 = TimeTracker(buttonThreePin)
button4 = TimeTracker(buttonFourPin)

try:
  while True:
    writeTimeToLCD(lcd, button1, button2, button3, button4)
    
    if GPIO.input(button1.pin) and GPIO.input(button2.pin):
      # Button 1 and 2 pressed at same time
      # Used to reset all time trackers
      resetTimeTrackers(button1, button2, button3, button4)

    elif GPIO.input(button1.pin) and GPIO.input(button3.pin):
      # Button 1 and 3 pressed at same time
      # Used to exit program
      lcd.close(clear=True)
      exit(0)
    else:
      
      if GPIO.input(button1.pin):
        button1.buttonPressed()

      if GPIO.input(button2.pin):
        button2.buttonPressed()

      if GPIO.input(button3.pin):
        button3.buttonPressed()

      if GPIO.input(button4.pin):
        button4.buttonPressed()

      time.sleep(.2)

except KeyboardInterrupt: # CTRL+C is pressed
  lcd.close(clear=True)



