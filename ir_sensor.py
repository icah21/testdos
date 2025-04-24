# ir_sensor.py
import RPi.GPIO as GPIO
import time

class IRSensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def is_object_detected(self):
        return GPIO.input(self.pin) == 0  # Adjust depending on your IR sensor output

    def cleanup(self):
        GPIO.cleanup(self.pin)
