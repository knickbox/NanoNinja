from Car import Car
import time

if __name__ == '__main__':
    car = Car()
    for i in range(4):
        car.control_car(100, 100)
        time.sleep(2)
        car.control_car(0,0)
        time.sleep(.3)
        car.control_car(-100, 100)
        time.sleep(.5)
        car.control_car(0, 0)
        time.sleep(.3)
