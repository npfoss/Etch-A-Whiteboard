# +---------------------------------------------------------------------------+
# |                    Etch-A-Whiteboard movement methods                     |
# |                               Nate Foss                                   |
# |                                5/24/16                                    |
# |                          TJHSST Robotics Lab                              |
# +---------------------------------------------------------------------------+
import RPi.GPIO as GPIO
import time
import sys
#======================< GLOBAL STUFFS >==============================Movement==
delay = 0.002
               #A1  A2  B1  B2  #B2 is closest to power on the H-Bridge module
stepperPins = [[26, 19, 13,  6],
                ??, ??, ??, ??]
    # stepperPins row 0 is horizontal, 1 is vertical
#---------------------------------------------------------------------Movement--
def initSteppers():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for lst in stepperPins:
        for pin in lst:
            GPIO.setup(pin, GPIO.OUT)
#---------------------------------------------------------------------Movement--
# should be in format [dir, steps,]
def parseLine(lineList):
    lineList = [int(lineList[x]) for x in range(len(lineList))]
    if len(lineList) <= 2:
        #not parallel
        if lineList[0] < 8:
            move(lineList[0], lineList[1])
        else:
            [penup, pendown][lineList[0]-8]()
    else:
        #todo: do things in parallel

#---------------------------------------------------------------------Movement--
# Function for step sequence
def setStep(s, w1, w2, w3, w4):
  GPIO.output(stepperPins[s][0], w1)
  GPIO.output(stepperPins[s][1], w2)
  GPIO.output(stepperPins[s][2], w3)
  GPIO.output(stepperPins[s][3], w4)

#---------------------------------------------------------------------Movement--
def up(steps):
    for x in range(steps):
        stepCounterclockwise(1)
#---------------------------------------------------------------------Movement--
def upright(steps):
    #todo: parallel
#---------------------------------------------------------------------Movement--
def right(steps):
    
#---------------------------------------------------------------------Movement--
def downright(steps):
    #todo: parallel
    
#---------------------------------------------------------------------Movement--
def down(steps):
    
#---------------------------------------------------------------------Movement--
def downleft(steps):
    #todo: parallel
    
#---------------------------------------------------------------------Movement--
def left(steps):
    
#---------------------------------------------------------------------Movement--
def upleft(steps):
    #todo: parallel
    
#---------------------------------------------------------------------Movement--
def penup():
    #todo: actuators
    
#---------------------------------------------------------------------Movement--
def pendown():
    #todo: actuators
    
#---------------------------------------------------------------------Movement--
def stepClockwise(stepper):
    setStep(stepper, 1,0,0,1)
    time.sleep(delay)
    setStep(stepper, 0,1,0,1)
    time.sleep(delay)
    setStep(stepper, 0,1,1,0)
    time.sleep(delay)
    setStep(stepper, 1,0,1,0)
    time.sleep(delay)
#---------------------------------------------------------------------Movement--
def stepCounterclockwise(stepper):
    setStep(stepper, 1,0,1,0)
    time.sleep(delay)
    setStep(stepper, 0,1,1,0)
    time.sleep(delay)
    setStep(stepper, 0,1,0,1)
    time.sleep(delay)
    setStep(stepper, 1,0,0,1)
    time.sleep(delay)
#---------------------------------------------------------------------Movement--
def move(direction, steps):
    fnct = [up, upright, right, downright, down, downleft, left, upleft][direction]
    fnct(steps)
#===============================< MAIN >========================================
def main():
    # DO STUFF HERE
    if sys.argv[0] > 1:
        # NOTE: input should be in the form  int , int  where the first int is
        #       direction, and the second is the number of steps.
        #       This is the same format as the instruction file.
        initSteppers()
        parseLine(argv[1:])