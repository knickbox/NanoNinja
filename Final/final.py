from Car import Car
import time

SPEED = 50



if __name__ == '__main__':
    car = Car()
    car.sing()
    time.sleep(0.5)
    car.set_servo(1, 180)
    time.sleep(0.1)
    car.set_servo(2, 85)
    time.sleep(0.2)

    # Main control loop
    try:
        while True:
            dist = car.distance()
            if dist < 20:
                car.control_car(0, SPEED)
            else:
                car.control_car(SPEED + 10, SPEED)
            time.sleep(0.3)
    except KeyboardInterrupt:
        car.control_car(0, 0)
        # car.set_servo(1, 90)
        # car.set_servo(2, 90)
        car.cleanup()