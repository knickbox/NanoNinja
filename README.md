# NanoNinja

## Basic Mobility

NanoNinja uses a Python class called `Car`, which was provided by our TA, to interface with its hardware. Currently, it has two main components: `DeadRec.py` and `teleoperation.py` which are bot located in the **BasicMobility**. With these components, you can make NanoNinja move in a square pattern or control it remotely using your keyboard.

## Dependencies

Before you begin, make sure you have the following dependencies installed:

- **Time:** pythons built in time library.

- **Curses Library:** The `teleoperation.py` script uses the `curses` library to capture keyboard input for remote control.

## Usage

### 1. Moving NanoNinja in a Square (DeadRec.py)

To make NanoNinja move in a square pattern, follow these steps:

1. Open a terminal.
2. Navigate to the directory containing `DeadRec.py`.
3. Run the following command:

   ```
   python DeadRec.py
   ```

4. NanoNinja will move in a square pattern.

### 2. Remote Control (teleoperation.py)

To remotely control NanoNinja using your keyboard, follow these steps:

1. Open a terminal.
2. Navigate to the directory containing `teleoperation.py`.
3. Run the following command:

   ```
   python teleoperation.py
   ```

4. Use the arrow keys to control NanoNinja's movement:
   - Up arrow: Move forward.
   - Down arrow: Move backward.
   - Left arrow: Turn left.
   - Right arrow: Turn right.

5. To stop NanoNinja, press 'm'.
6. To quit the program, press 'q'.
