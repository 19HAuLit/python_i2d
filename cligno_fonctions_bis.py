import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

LedR = 18
LedV = 23

GPIO.setup(LedR, GPIO.OUT)
GPIO.setup(LedV, GPIO.OUT)

def cligno_dephase(Nb_cligno, tempo1, tempo2):
    count1 = 0
    for count1 in range(Nb_cligno):
        print("En dephassage")

        GPIO.output(LedR, GPIO.HIGH)
        GPIO.output(LedV, GPIO.LOW)
        time.sleep(tempo1)

        GPIO.output(LedV, GPIO.HIGH)
        GPIO.output(LedR, GPIO.LOW)
        time.sleep(tempo2)

def cligno_phase(Nb_cligno, tempo1, tempo2):
    count2 = 0
    for count2 in range(Nb_cligno):
        print("en phase")
        GPIO.output(LedR, GPIO.HIGH)
        GPIO.output(LedV, GPIO.HIGH)
        time.sleep(tempo1)

        GPIO.output(LedR, GPIO.LOW)
        GPIO.output(LedV, GPIO.LOW)
        time.sleep(tempo2)

while True:

    cligno_dephase(7, 0.5, 1)

    cligno_phase(4, 0.8, 1.5)