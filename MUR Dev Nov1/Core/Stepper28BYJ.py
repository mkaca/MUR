#!/usr/bin/env python
 
# import required libs
import time
import RPi.GPIO as GPIO

class Stepper28BYJ():
  def __init__(self, Pin1, Pin2, Pin3, Pin4, cleanup = True, setGPIOMode = True):

    #Throw error if class is called without the 4 pins
    if (Pin1 == None or Pin2 == None or Pin3 == None or Pin4 == None):
      raise ValueError("You MUST define all 4 pins as INTEGERS, ex: 2,23,4,21")

    if cleanup:
      GPIO.cleanup() #cleaning up in case GPIOS have been preactivated
    
    # Use BCM GPIO references
    # instead of physical pin numbers
    if(setGPIOMode):
      GPIO.setmode(GPIO.BOARD)
    
    # be sure you are setting pins accordingly
    #in 1, 2, 3, 4
    self.StepPins = [Pin1,Pin2,Pin3,Pin4]
   
    # Set all pins as output and ensure they are low
    for pin in StepPins:
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, False)
    #wait some time to start
    time.sleep(0.5)
      # Define some settings from datasheet
    self.StepCounter = 0
    self.WaitTime = 0.0015
     
     
    # Define stepper sequence
    self.StepCount = 8
    self.Seq = []
    Seq = range(0, StepCount)
    Seq[0] = [1,0,0,0]
    Seq[1] = [1,1,0,0]
    Seq[2] = [0,1,0,0]
    Seq[3] = [0,1,1,0]
    Seq[4] = [0,0,1,0]
    Seq[5] = [0,0,1,1]
    Seq[6] = [0,0,0,1]
    Seq[7] = [1,0,0,1]

  def moveDegrees(self, degrees):
    try:
      self.steps = int(round(degrees*1024/90))
      println('Moving Stepper %i steps',steps)
      print(', which is the same as %i degrees',degrees)
      # moves stepper motor by 45 degrees forever
      for _ in range(0,steps):  # 12 =1 degree
          for pin in range(0, 4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin]!=0:
              #print " Step %i Enable %i" %(StepCounter,xpin)
              GPIO.output(xpin, True)
            else:
              GPIO.output(xpin, False)
          StepCounter += 1
        # If we reach the end of the sequence
        # start again
          if (StepCounter==StepCount):
            StepCounter = 0
          if (StepCounter<0):
            StepCounter = StepCount
        # Wait before moving on
          time.sleep(WaitTime)

    except:
      if cleanup:
        GPIO.cleanup()

    #turn off stepper motor
    finally: #cleaning up and setting pins to low again (motors can get hot if you wont) 
        for pin in StepPins:
          GPIO.setup(pin,GPIO.OUT)
          GPIO.output(pin, False)
  