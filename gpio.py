import RPi.GPIO as GPIO
import time

num_bits = 8

D =  [21, 20, 16, 12, 1 , 7, 8, 25]

def lightUp(ledNumber, period) :
    GPIO.output(D[ledNumber], 1)
    time.sleep(period)
    GPIO.output(D[ledNumber], 0)

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(0, blinkCount):
        GPIO.output(D[ledNumber], 1)
        time.sleep(blinkPeriod)
        GPIO.output(D[ledNumber], 0)
        time.sleep(blinkPeriod)

def runningLight(count, period):
    for i in range(0, count):
        for j in range(0, num_bits):
            lightUp(i % num_bits, period)

def darkUp(ledNumber, period):
    GPIO.output(D[ledNumber], 0)
    time.sleep(period)
    GPIO.output(D[ledNumber], 1)

def runningDark(count, period):
    for i in range(0, count):
    for j in range(0, num_bits):
        darkUp(i % num_bits, period)

def decToBinList(decNumber):
    N = num_bits - 1
    p = 0
    x = []
    while N > 0:
        p = int(decNumber / 2**N)
        if p == 1:
            x.append(1)
            decNumber -= 2**N
        else:
            x.append(0)
        N -= 1
    x.append(decNumber)
    return(x)

def lightNumber(number):
    N = decToBinList(number)
    for i in range(0, num_bits):
        GPIO.output(D[i], N[num_bits - i - 1)])

def runningPattern(pattern, direction):
    lightNumber(pattern)
    if direction == 1:
        while True:
            time.sleep(0.5)
            pattern = pattern >> 1
            lightNumber(pattern)
    if direction == 0:
        while True:
            time.sleep(0.5)
            pattern = pattern << 1 % 256
            lightNumber(pattern)
