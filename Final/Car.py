# Modified to integrate distance method
import smbus2 as smbus
import time
import math
import RPi.GPIO as GPIO

class Car:
    def __init__(self):
        self._addr = 0x16
        self._device = smbus.SMBus(1)

        # GPIO for Sonar
        GPIO.setwarnings(False)

        EchoPin = 18
        TrigPin = 16
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(EchoPin, GPIO.IN)
        GPIO.setup(TrigPin, GPIO.OUT)

    def __write_u8(self, register, data):
        try:
            self._device.write_byte_data(self._addr, register, data)
        except:
            print('write_u8 error')

    def __write_register(self, register):
        try:
            self._device.write_byte(self._addr, register)
        except:
            print('write_register error')

    def __write_array(self, register, data):
        try:
            self._device.write_i2c_block_data(self._addr, register, data)
        except:
            print('write_array error')

    def control_car(self, left, right):
        """
        left: int (-255, 255)
        right: int (-255, 255)

        sets the motor with the speed given (not actually in unit, just a power amount)
        """
        register = 0x01
        left_direction = 0 if left < 0 else 1
        right_direction = 0 if right < 0 else 1

        if left < 0:
            left *= -1
        if right < 0:
            right *= -1

        data = [left_direction, left, right_direction, right]
        self.__write_array(register, data)

    def stop(self):
        register = 0x02
        self.__write_u8(register, 0x00)

    def set_servo(self, servo_id, angle):
        register = 0x03
        if angle < 0:
            angle = 0
        elif angle > 180:
            angle = 180
        data = [servo_id, angle]
        self.__write_array(register, data)

    def distance():
        GPIO.output(TrigPin, GPIO.LOW)
        time.sleep(0.000002)
        GPIO.output(TrigPin, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(TrigPin, GPIO.LOW)

        t3 = time.time()

        while not GPIO.input(EchoPin):
            t4 = time.time()
            if (t4 - t3) > 0.03:
                return -1
        t1 = time.time()
        while GPIO.input(EchoPin):
            t5 = time.time()
            if (t5 - t1) > 0.03:
                return -1

        t2 = time.time()
        time.sleep(0.01)
        return ((t2 - t1) * 340 / 2) * 100


# Example Main
if __name__ == '__main__':
    car = Car()

    car.set_servo(1, 90)
    time.sleep(0.5)

    car.set_servo(2, 90)
    time.sleep(0.5)

    car.set_servo(1, 180)
    time.sleep(0.5)

    car.set_servo(2, 180)
    time.sleep(0.5)

    car.set_servo(1, 90)
    time.sleep(0.5)
    car.set_servo(2, 90)
