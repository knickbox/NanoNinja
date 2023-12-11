import time

from Car import Car
from detector import Detector

SPEED = 80
CLOSE_THRESH = 40
FAR_THRESH = 100
FREQ = 0.3 # length of sleep each loop
DETECT_FREQ = 5 # count people every DETECT_FREQ seconds

# Use - of SPEED as modifier for turning
def turn_left(car):
    car.control_car(-SPEED, SPEED)

# Use .5 of SPEED as modifier for turning
def slight_right(car):
    car.control_car(SPEED + (SPEED // 2), SPEED - (SPEED // 2))

if __name__ == '__main__':
    car = Car()
    car.sing()
    detector = Detector()
    car.set_servo(1, 180)
    time.sleep(0.1)
    car.set_servo(2, 60)
    time.sleep(0.2)

try:
    time.sleep(.1)
    turningSharp = False
    timeAtLastDetection = 0
    while True:
        if time.time() - timeAtLastDetection > DETECT_FREQ:
            car.control_car(0, 0)
            time.sleep(.3)
            personCount = detector.detect()
            print(f"Person count: {personCount}")
            timeAtLastDetection = time.time() # reset timer at current time (after detection)

        # Dist test takes multiple readings and returns a more robust distance
        testDist = car.Distance_test()
        # print(testDist)
        if turningSharp:
            if testDist > FAR_THRESH and car.getRightSensor() == 1:
                turningSharp = False
                slight_right(car)
            else:
                turn_left(car)
        else:
            if testDist < CLOSE_THRESH or car.getRightSensor() == 0:
                turningSharp = True
                turn_left(car)
            else:
                slight_right(car)
        time.sleep(FREQ)
except KeyboardInterrupt:
    car.control_car(0, 0)
    car.cleanup()