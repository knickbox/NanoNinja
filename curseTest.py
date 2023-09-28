import curses
curses.initscr()
curses.noecho()
curses.cbreak() # don't have to press enter
stdscr.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
            print "up"
        elif char == curses.KEY_DOWN:
            print "down"
        elif char == curses.KEY_RIGHT:
            print "right"
        elif char == curses.KEY_LEFT:
            print "left"
        elif char == 10:
            print "stop"
finally:
    curse.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
