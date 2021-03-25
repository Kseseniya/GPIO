import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

num_bits = 8

D =  [24, 25, 8, 7, 12, 16, 20, 21]

GPIO.setup(D[:], GPIO.OUT)

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
            lightUp(j % num_bits, period)

def darkUp(ledNumber, period):
    GPIO.output(D[ledNumber], 0)
    time.sleep(period)
    GPIO.output(D[ledNumber], 1)

def runningDark(count, period):
    for i in range(0, count):
        for j in range(0, num_bits):
            darkUp(j % num_bits, period)

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
        GPIO.output(D[i], N[num_bits - (i + 1)])
    time.sleep(0.5)
        

def runningPattern(pattern, direction): #direction: 1 - right, 0 - left
    lightNumber(pattern)
    if direction == 1:
        while True:
            lightNumber(pattern)
            if (pattern // 2)*2 != pattern:
                pattern += 2**num_bits 
            pattern = pattern >> 1
            time.sleep(0.5)
    if direction == 0:
        while True:
            lightNumber(pattern)
            pattern = pattern << 1 % 255
            time.sleep(0.5)

def PWM(ledNumber, frec):
    p = GPIO.PWM(D[ledNumber], frec)
    p.start(0)
    while True:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
    p.stop()

#lightUp(2, 2)
#blink(4,5,0.2)
#runningLight(2,0.2)
#runningDark(2,0.3)
GPIO.cleanup()
#lightNumber(15)
#runningPattern(5,1)
PWM(3, 50)
GPIO.cleanup()






























































































































































































