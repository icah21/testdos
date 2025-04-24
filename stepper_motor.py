import RPi.GPIO as GPIO
import time

class StepperMotor:
    def __init__(self, pins, steps_per_rev=512):
        self.pins = pins
        self.steps_per_rev = steps_per_rev
        self.sequence = [
            [1,0,0,1],
            [1,0,0,0],
            [1,1,0,0],
            [0,1,0,0],
            [0,1,1,0],
            [0,0,1,0],
            [0,0,1,1],
            [0,0,0,1]
        ]
        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

    def rotate(self, step_count, total_time):
        steps = abs(step_count)
        if steps == 0:
            return
        delay = total_time / steps
        direction = 1 if step_count > 0 else -1
        for _ in range(steps):
            for step in range(8)[::direction]:
                for pin in range(4):
                    GPIO.output(self.pins[pin], self.sequence[step][pin])
                time.sleep(delay)

    def go_to_angle(self, current_angle, target_angle):
        step_angle = 360 / self.steps_per_rev
        delta_angle = target_angle - current_angle
        step_count = int(delta_angle / step_angle)
        self.rotate(step_count, total_time=5)
        return target_angle
