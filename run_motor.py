import RPi.GPIO as GPIO
from gpiozero import Button
from gpiozero import OutputDevice
from time import sleep, time

'''
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(14,GPIO.RISING,callback=playVideo)
'''

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN)
GPIO.setup(21, GPIO.IN)

motor1 = OuputDevice(11)
motor2 = OutputDevice(13)

button = Button(14)
button.when_pressed = run_motor

def run_motor():
    if GPIO.input(19) == 1:
        motor1.on()
        while GPIO.input(21) == 0:
            print("running motor 1")
        motor1.off()
        time.sleep(2)
        motor2.on()
        while GPIO.input(19) == 0:
            print("running motor 2")
        motor2.off()
        time.sleep(2)