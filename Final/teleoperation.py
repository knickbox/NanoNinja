import RPi.GPIO as GPIO
import time
import curses
from Car import Car
car = Car()
screen = curses.initscr()
curses.noecho()
curses.cbreak() # don't have to press enter
screen.keypad(True)
speed = 50


GPIO.setwarnings(False)

EchoPin = 18
TrigPin = 16
GPIO.setmode(GPIO.BOARD)

GPIO.setup(EchoPin, GPIO.IN)
GPIO.setup(TrigPin, GPIO.OUT)

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


try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print("up")
            car.control_car(speed,speed)
        elif char == curses.KEY_DOWN:
            print("down")
            car.control_car(-speed,-speed)
        elif char == curses.KEY_RIGHT:
            print("right")
            car.control_car(speed,-speed)
        elif char == curses.KEY_LEFT:
            print("left")
            car.control_car(-speed,speed)
        elif char == ord('m'):
            print("stop")
            car.control_car(0,0)
        print(f"Distance: {distance()}")
finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
