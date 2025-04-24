# stepper_motor.py
import RPi.GPIO as GPIO
import time

class StepperMotor:
    def __init__(self, pins):
        self.pins = pins
        self.sequence = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1]
        ]
        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

    def rotate(self, steps, delay=0.002):
        for _ in range(steps):
            for step in self.sequence:
                for pin, val in zip(self.pins, step):
                    GPIO.output(pin, val)
                time.sleep(delay)

    def go_to_angle(self, current_angle, target_angle):
        # approx 512 steps for 360°, so ~1.42 steps/degree
        steps_per_degree = 512 / 360
        step_count = int((target_angle - current_angle) * steps_per_degree)
        self.rotate(step_count if step_count >= 0 else -step_count, 0.002 if step_count >= 0 else -0.002)

    def cleanup(self):
        GPIO.cleanup(self.pins)
