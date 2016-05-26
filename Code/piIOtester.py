import RPi.GPIO as GPIO
import time

# Variables

delay = 0.002
steps = 1000

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Enable pins for IN1-4 to control step sequence

coil_A_1_pin = 26
coil_A_2_pin = 19
coil_B_1_pin = 13
coil_B_2_pin = 6 # this is the one closest to power on the H-Bridge module

# Set pin states

GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Function for step sequence

def setStep(w1, w2, w3, w4):
  GPIO.output(coil_A_1_pin, w1)
  GPIO.output(coil_A_2_pin, w2)
  GPIO.output(coil_B_1_pin, w3)
  GPIO.output(coil_B_2_pin, w4)

# loop through step sequence based on number of steps

print('left')
for i in range(0, steps):
    setStep(1,0,1,0)
    time.sleep(delay)
    setStep(0,1,1,0)
    time.sleep(delay)
    setStep(0,1,0,1)
    time.sleep(delay)
    setStep(1,0,0,1)
    time.sleep(delay)

# Reverse previous step sequence to reverse motor direction

print('right')
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