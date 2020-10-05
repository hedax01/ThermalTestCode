import serial
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
ser=serial.Serial('/dev/ttyUSB0',9600, timeout=2)
trigger=26
head=17
human=0
step=5
pull=27
UP=1
DOWN=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(step, GPIO.OUT)
GPIO.setup(pull, GPIO.OUT)

GPIO.setup(head, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(human, GPIO.IN,pull_up_down=GPIO.PUD_UP)

def trigggerMeasure():
    GPIO.output(trigger,0)
    sleep(0.1)
    GPIO.output(trigger,1)

GPIO.output(trigger,1)

i=0
while i<5:
    sleep(5)
    i=i+1
    trigggerMeasure()
    temp=ser.readline()
    print(temp)
    
ser.close()

GPIO.cleanup()
