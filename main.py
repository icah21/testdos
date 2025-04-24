# main.py
import threading
import time
from ir_sensor import IRSensor
from stepper_motor import StepperMotor

IR_PIN = 17
STEPPER_PINS = [18, 23, 24, 25]  # adjust according to your wiring

ir = IRSensor(IR_PIN)
motor = StepperMotor(STEPPER_PINS)
current_angle = 0
lock = threading.Lock()

def ir_thread_func():
    global ir_detected
    while True:
        if ir.is_object_detected():
            ir_detected = True
        else:
            ir_detected = False
        time.sleep(0.2)

def motor_thread_func():
    global current_angle
    while True:
        if ir_detected:
            with lock:
                if current_angle != 90:
                    motor.go_to_angle(current_angle, 90)
                    current_angle = 90
                time.sleep(15)
                motor.go_to_angle(current_angle, 180)
                current_angle = 180
                time.sleep(10)
                motor.go_to_angle(current_angle, 0)
                current_angle = 0
                time.sleep(10)
        else:
            time.sleep(1)

try:
    ir_detected = False
    ir_thread = threading.Thread(target=ir_thread_func, daemon=True)
    motor_thread = threading.Thread(target=motor_thread_func, daemon=True)

    ir_thread.start()
    motor_thread.start()

    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Cleaning up GPIO...")
    ir.cleanup()
    motor.cleanup()
