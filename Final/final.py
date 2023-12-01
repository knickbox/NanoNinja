from Car import Car
import time

SPEED = 50



if __name__ == '__main__':
    car = Car()
    car.sing()
    time.sleep(0.5)
    car.set_servo(1, 180)
    time.sleep(0.1)
    car.set_servo(2, 95)
    print(car.distance())