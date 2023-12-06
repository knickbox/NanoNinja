from Car import Car
import time

SPEED = 70
CLOSE_THRESH = 40
FAR_THRESH = 100
FREQ = 0.3

if __name__ == '__main__':
    car = Car()
    car.sing()
    time.sleep(0.5)
    car.set_servo(1, 180)
    time.sleep(0.1)
    car.set_servo(2, 85)
    time.sleep(0.2)


    def turn_left():
        car.control_car(-10, SPEED)

    def slight_right():
        car.control_car(SPEED + 10, SPEED)

# TODO: Use the last value to reduce false reads
# TODO: Make a rescue code to unstick the car
# Main control loop
try:
    turningSharp = False
    while True:
        dist = car.distance()
        print(dist)
        if turningSharp:
            if dist > FAR_THRESH:
                turningSharp = False
                slight_right()
            else:
                turn_left()
        else:
            if dist < CLOSE_THRESH:
                turningSharp = True
                turn_left()
            else:
                slight_right()
        time.sleep(FREQ)
except KeyboardInterrupt:
    car.control_car(0, 0)
    # car.set_servo(1, 90)
    # car.set_servo(2, 90)
    car.cleanup()