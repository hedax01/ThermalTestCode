import RPi.GPIO as GPIO
import serial
ser=serial.Serial('/dev/ttyS0',9600, timeout=2)

from time import sleep
from timing import delayMicroseconds

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

EN=5
PUL=22
DIR=6
head=17
body=26
trigger=27
hand=16
handTrig=25
buzz=24

GPIO.setup(EN,GPIO.OUT)
GPIO.setup(PUL,GPIO.OUT)
GPIO.setup(DIR,GPIO.OUT)

GPIO.setup(trigger,GPIO.OUT)
GPIO.output(trigger,1)
GPIO.setup(head,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(body,GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(hand,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(handTrig,GPIO.OUT)
GPIO.setup(buzz,GPIO.OUT)
GPIO.output(buzz,1)
GPIO.output(handTrig,1)

GPIO.output(EN,1)
GPIO.output(PUL,0)
GPIO.output(DIR,0)

class ThermalTest:
    @staticmethod
    def trig():
        GPIO.output(trigger,0)
        sleep(0.5)
        GPIO.output(trigger,1)
    @staticmethod
    def measure():
        GPIO.output(trigger,0)
        value = ser.readline()
        GPIO.output(trigger,1)
        return value

class Motor:
    UP=1
    DOWN=0
    def __setDir(self, dir):
        """
        docstring
        """
        if dir:
            GPIO.output(DIR,self.UP)
        else:
            GPIO.output(DIR,self.DOWN)
    def __generaFulse(self, duration=50):
        GPIO.output(PUL,1)
        delayMicroseconds(duration)
        GPIO.output(PUL, 0)
        delayMicroseconds(duration)
    def lock(self):
        GPIO.output(EN,0)

    
    def moveUp(self, v=50, steps=6400):
        self.__setDir(self.UP)
        GPIO.output(EN,0)
        for i in range(0,steps):
            self.__generaFulse(v)
        GPIO.output(EN,1)

    def moveDown(self, v=50, steps=6400):
        self.__setDir(self.DOWN)
        GPIO.output(EN,0)
        for i in range(0,steps):
            self.__generaFulse(v)
        GPIO.output(EN,1)


class DistanceSensor:
    @staticmethod
    def isHuman():
        """
        docstring
        """
        return GPIO.input(body)
    @staticmethod
    def isNeedMeasure():
        """
        docstring
        """
        return GPIO.input(head)

class HandWasher:
    @staticmethod
    def On():
        GPIO.output(handTrig,0)
    def Off():
        GPIO.output(handTrig,1)
class Buzz:
    @staticmethod
    def On():
        GPIO.output(buzz,0)
    def Off():
        GPIO.output(buzz,1)
