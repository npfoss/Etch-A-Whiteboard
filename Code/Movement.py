# +---------------------------------------------------------------------------+
# |                    Etch-A-Whiteboard movement methods                     |
# |                               Nate Foss                                   |
# |                                5/24/16                                    |
# |                          TJHSST Robotics Lab                              |
# +---------------------------------------------------------------------------+
import RPi.GPIO as GPIO
import time
import sys
#import multiprocessing
#======================< GLOBAL STUFFS >==============================Movement==
delay = 0.002
               #A1  A2  B1  B2  #B2 is closest to power on the H-Bridge module
stepperPins = [[26, 19, 13,  6],
               [12, 16, 20, 21]]
    # stepperPins row 0 is horizontal, 1 is vertical
#---------------------------------------------------------------------Movement--
def initSteppers():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    for lst in stepperPins:
        for pin in lst:
            GPIO.setup(pin, GPIO.OUT)

    #this again, just in case
    delay = 0.002
                   #A1  A2  B1  B2  #B2 is closest to power on the H-Bridge module
    stepperPins = [[26, 19, 13,  6],
                   [12, 16, 20, 21]]
        # stepperPins row 0 is horizontal, 1 is vertical

    print('--Initialization complete.')
#---------------------------------------------------------------------Movement--
# should be in format [dir, steps,]
def parseLine(lineList):
    lineList = [int(lineList[x]) for x in range(len(lineList))]
    if lineList[0] < 8:
        move(lineList[0], lineList[1])
    else:
        [penup, pendown][lineList[0]-8]()
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
    for x in range(steps):
        stepCounterclockwise(1)
        stepClockwise(0)
#---------------------------------------------------------------------Movement--
def right(steps):
    for x in range(steps):
        stepClockwise(0)
#---------------------------------------------------------------------Movement--
def downright(steps):
    for x in range(steps):
        stepClockwise(0)
        stepClockwise(1)
#---------------------------------------------------------------------Movement--
def down(steps):
    for x in range(steps):
        stepClockwise(1)
#---------------------------------------------------------------------Movement--
def downleft(steps):
    for x in range(steps):
        stepClockwise(1)
        stepCounterclockwise(0)
#---------------------------------------------------------------------Movement--
def left(steps):
    for x in range(steps):
        stepCounterclockwise(0)
#---------------------------------------------------------------------Movement--
def upleft(steps):
    for x in range(steps):
        stepCounterclockwise(0)
        stepCounterclockwise(1)
#---------------------------------------------------------------------Movement--
def penup():
    #todo: actuators
    return
#---------------------------------------------------------------------Movement--
def pendown():
    #todo: actuators
    return
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
#------------------------------------------------------------Etch-A-Whiteboard--
if __name__ == '__main__': main()
#############################< END OF PROGRAM >#################################
'''
p1 = multiprocessing.Process(target=up, args=(steps))
p2 = multiprocessing.Process(target=right, args=(steps))
p1.start()
p2.start()
while p1.isAlive() or p2.isAlive():
    sleep(.1)
'''