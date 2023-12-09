from Car import Car
import time

SPEED = 70
CLOSE_THRESH = 40
FAR_THRESH = 100
FREQ = 0.3 # length of sleep each loop

if __name__ == '__main__':
    car = Car()
    car.sing()
    time.sleep(0.5)
    car.set_servo(1, 180)
    time.sleep(0.1)
    car.set_servo(2, 70)
    time.sleep(0.2)

    # Use .25 of SPEED as modifier for turning
    def turn_left():
        car.control_car(-(SPEED//4), SPEED)

    def slight_right():
        car.control_car(SPEED + (SPEED // 4), SPEED)


try:
    time.sleep(.1)
    turningSharp = False
    while True:
        # Dist test takes multiple readings and returns a more robust distance
        testDist = car.Distance_test()
        print(testDist)
        if turningSharp:
            if testDist > FAR_THRESH and car.getRightSensor() == 0:
                turningSharp = False
                slight_right()
            else:
                turn_left()
        else:
            if testDist < CLOSE_THRESH or car.getRightSensor() == 1:
                turningSharp = True
                turn_left()
            else:
                slight_right()
        time.sleep(FREQ)
except KeyboardInterrupt:
    car.control_car(0, 0)
    car.cleanup()