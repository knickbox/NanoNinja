from pynput import keyboard
from Car import car

def on_press(key):
        if key.char == 'w':
            car.control_car(100, 100)
        elif key.char == 's':
            car.control_car(-100, -100)
        elif key.char == 'a':
            car.control_car(-100,100)
        elif key.char == 'd':
            car.control_car(100,-100)


def on_release(key):
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key.char == 'w':
        car.control_car(0, 0)
    elif key.char == 's':
        car.control_car(0, 0)
    elif key.char == 'a':
        car.control_car(0,0)
    elif key.char == 'd':
        car.control_car(0,0)


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

