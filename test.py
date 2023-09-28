from keyboard_listener import KeyboardListener, Combo, KeyWord
from Car import Car
import sys
car = Car()
def moveForward():
	car.control_car(100,100)

def moveLeft():
	car.control_car(-100,100)

def moveRight():
	car.control_car(100,-100)

def moveBackward():
	car.control_car(-100,-100)

def stop():
	car.control_car(0,0)

def exitMode():
	sys.exit()

combinations = {
	'function 1': Combo(['alt'], 'f', moveLeft),
	'function 2': Combo(['alt'], 'g', moveRight)
}

keywords = {
	'keyword_1': KeyWord('w', moveForward),
	'keyword_2': KeyWord('s', moveBackward),
	'left': KeyWord('a', moveLeft),
	'right': KeyWord('d', moveRight),
	'exitWord': KeyWord('q', exitMode)
	'stop': KeyWord(' ', stop)
}

keyboard_listener = KeyboardListener(combinations=combinations, keywords=keywords)
keyboard_listener.run()



