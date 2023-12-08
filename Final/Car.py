# Modified to integrate distance method, sing, and cleaup
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

        self.EchoPin = 18
        self.TrigPin = 16
        self.BuzPin = 32
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.EchoPin, GPIO.IN)
        GPIO.setup(self.TrigPin, GPIO.OUT)
        GPIO.setup(self.BuzPin, GPIO.OUT)

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

    def distance(self):
        GPIO.output(self.TrigPin, GPIO.LOW)
        time.sleep(0.000002)
        GPIO.output(self.TrigPin, GPIO.HIGH)
        time.sleep(0.000015)
        GPIO.output(self.TrigPin, GPIO.LOW)

        t3 = time.time()

        while not GPIO.input(self.EchoPin):
            t4 = time.time()
            if (t4 - t3) > 0.03:
                return -1
        t1 = time.time()
        while GPIO.input(self.EchoPin):
            t5 = time.time()
            if (t5 - t1) > 0.03:
                return -1

        t2 = time.time()
        time.sleep(0.01)
        return ((t2 - t1) * 340 / 2) * 100
    

    def note_to_frequency(self, note):
        # Dictionary to map note names to the number of half steps away from A4
        note_to_steps = {'F#0': -15, 'C': -9, 'C#': -8, 'Db': -8, 'D': -7, 'D#': -6, 'Eb': -6,
                        'E': -5, 'Fb': -5, 'E#': -4, 'F': -4, 'F#': -3, 'Gb': -3,
                        'G': -2, 'G#': -1, 'Ab': -1, 'A': 0, 'A#': 1, 'Bb': 1,
                        'B': 2, 'Cb': 2, 'B#': 3}

        # Check if the note is in the dictionary
        if note in note_to_steps:
            # Calculate the number of half steps away from A4
            steps_away = note_to_steps[note]
            
            # Calculate the frequency using the formula
            frequency = 2 ** ((steps_away + 12) / 12) * 440
            
            return frequency
        else:
            return None  # Return None for invalid notes
        

    def sing(self, songId=0):
        # song is a list of tuples (note, duration)
        moonTheme = [
            ('F#0',.17),
            ('C#',.17),
            ('F#',.17),
            ('G#',.17),
            ('C#',.17),
            ('F#',.17),
            ('G#',.17),
            ('C#',.17),
            ('B' ,.17),
            ('C#',.17),
            ('B',.17),
            ('Bb',.17),
            ('C#',.17),
            ('Bb',.17),
            ('G#',.17),
            ('F#',.17)]
        
        rescueBeep = [
            ('F#0',.17),
            ('F#0',.17)
        ]
        
        songs = [moonTheme, rescueBeep]

        song = songs[songId]
        Buzz = GPIO.PWM(self.BuzPin, 440)
        Buzz.start(50)
        for note in song:
            Buzz.ChangeFrequency(self.note_to_frequency(note[0]))
            time.sleep(note[1])
        Buzz.stop()

    def cleanup(self):
        GPIO.cleanup()

    def rescue(self):
        self.control_car(0, 0)
        self.sing(1)
        self.control_car(-200, 225)
        time.sleep(.5)
        self.control_car(0, 0)
        
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
