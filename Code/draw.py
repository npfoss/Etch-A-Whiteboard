# +---------------------------------------------------------------------------+
# |                         Etch-A-Whiteboard driver                          |
# |                               Nate Foss                                   |
# |                                5/24/16                                    |
# |                          TJHSST Robotics Lab                              |
# +---------------------------------------------------------------------------+
import sys
#import RPi.GPIO as GPIO
import time
import Movement

###################################START OF PROGRAM#############################
#===============================< MAIN >========================================
def main():
    Movement.initSteppers()

    filename = sys.argv[1]
    print('Reading from file', filename)
    f = open ( filename )

    line = f.readLine()
    count = 1
    startTime = clock()
    while(line):
        print(line)
        Movement.parseLine(line.strip().split())
        print('lines complete: %d\telapsed time: %.1f mins'%(count, (clock() -startTime)/60)
        line = f.readLine()
        count += 1
#------------------------------------------------------------Etch-A-Whiteboard--
if __name__ == '__main__': main()
#############################< END OF PROGRAM >#################################