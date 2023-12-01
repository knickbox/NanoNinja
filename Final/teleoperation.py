import curses
from Car import Car
car = Car()
screen = curses.initscr()
curses.noecho()
curses.cbreak() # don't have to press enter
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print("up")
            car.control_car(100,100)
        elif char == curses.KEY_DOWN:
            print("down")
            car.control_car(-100,-100)
        elif char == curses.KEY_RIGHT:
            print("right")
            car.control_car(100,-100)
        elif char == curses.KEY_LEFT:
            print("left")
            car.control_car(-100,100)
        elif char == ord('m'):
            print("stop")
            car.control_car(0,0)
finally:
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
