# NanoNinja

NanoNinja is a robot that navigates around the outside of a room using its sonar and IR avoidance sensors.  Every 5 seconds the robot will stop and take a picture facing the center of the room and then detect the number of people in the image.  The robot will report this count and then resume its movement.  We used YOLO version 8 to implement the person detection.  Besides the dependencies listed below all code is included in the *Final* directory.

Before you begin, make sure you have the following dependencies installed:

- **Time:** pythons built in time library.
- **smbus2:** used to interact with the hardware
- **cv2** used to interact with camera and manipulate images
- **ultralytics** includes the YOLO algorithms


## Usage

### Running the main loop

The main code for loop for the NanoNinja is all in */Final*.  You should enter this directory before running the main loop.  The main loop is located in *Final/final.py*. 

To run the main loop:

1. Navigate to the */Final* directory:  
   ```
   cd Final
   ```
2. Run final.py using python3:

   ```
   python3 final.py
   ```

3. NanoNinja will move around the room counting the people in it.
4. Use control + c to keyboard interrupt.  NanoNinja will exit cleanly after running some cleanup.


## Additional Documentation

### Methods added to Car class

- distance: method was provided separately by the TA's and now is incorporated in the Car class
- Distance_test: A more reliable distance read found in Yahboom's documentation that takes multiple reads and averages them.
- sing: accesses the buzzer
- cleanup: runs GPIO cleanup
- rescue:  shakes the car loose if it gets stuck against the wall.  This is no longer necessary since the incorporation of the IR avoid sensors.
- getLeftSensor and getRightSensor: returns a True or False value for if the sensor is triggered
- Also note that the constructor was modified to add relevant GPIO pins.

### Detector Class

- detect method: returns the number of people visible to the camera. (takes about 1 - 2 seconds)
- This is the part that uses **yolov8n**. See notes below if you have problems with yolo running out of memory.


### Notes
- ran into segfault problems when both yolov5 and yolov8 on raspberry pi.  Problem was fixed by downgrading pytorch ```pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2```
- The movement basically works by veering slightly right when the distance read is over the threshold and turning left hard when dist is under the threshold (See image below)
![movement Diagram](./media/basicMovement.png)
- In order to get a current picture from the camera using cv2 it was necessary to "flush" the buffer. This was simply done by reading stored frames without loading them into memory.
- Movement toggles between turning left and not turning left and uses two thresholds for cleaner movement.
- Movement uses the right-side avoidance sensor to detect if it needs to turn.
- Because the robot uses IR sensors you should not expect it to work as expected when exposed to sunlight.
