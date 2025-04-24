def rotate(self, step_count, total_time):
    steps = abs(step_count)
    if steps == 0:
        return  # no rotation needed
    delay = total_time / steps  # dynamic delay based on required steps
    direction = 1 if step_count > 0 else -1

    for _ in range(steps):
        for step in range(8)[::direction]:
            for pin in range(4):
                GPIO.output(self.pins[pin], self.sequence[step][pin])
            time.sleep(delay)

def go_to_angle(self, current_angle, target_angle):
    step_angle = 360 / self.steps_per_rev  # ~0.703 degrees per step
    delta_angle = target_angle - current_angle
    step_count = int(delta_angle / step_angle)

    # 🕔 Always rotate for 5 seconds
    self.rotate(step_count, total_time=5)
    return target_angle
