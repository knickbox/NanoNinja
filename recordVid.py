from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording([file path])
sleep(10)
camera.stop_recording()
camera.stop_preview()

