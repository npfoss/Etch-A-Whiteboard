import RPi.GPIO as GPIO
import time

# Variables

delay = 0.0055
steps = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

''' don't need to do this for ours
# Enable GPIO pins for  ENA and ENB for stepper

enable_a = 18
enable_b = 22
'''
# Enable pins for IN1-4 to control step sequence

coil_A_1_pin = 26
coil_A_2_pin = 19
coil_B_1_pin = 13
coil_B_2_pin = 6 # this is the one closest to power on the H-Bridge module

# Set pin states

'''GPIO.setup(enable_a, GPIO.OUT)
GPIO.setup(enable_b, GPIO.OUT)'''
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

'''
# Set ENA and ENB to high to enable stepper

GPIO.output(enable_a, True)
GPIO.output(enable_b, True)
'''
# Function for step sequence

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

# loop through step sequence based on number of steps

print('clockwise')
for i in range(0, steps):
    setStep(1,0,1,0)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(1,0,0,1)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)

# Reverse previous step sequence to reverse motor direction

print('counterclockwise')
for i in range(0, steps):
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(1,0,0,1)
    time.sleep(delay)
    setStep(1,0,1,0)
    time.sleep(delay)

print('Program end.')