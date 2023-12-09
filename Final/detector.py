import cv2
from ultralytics import YOLO

class Detector:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.model = YOLO('yolov8n.pt')  # load an official model

    def detect(self):
        result, image = self.cam.read()
        if True:
            image = cv2.resize(image, (320, 320))
            return self.model(image)  # predict on an image
        else:
            return None
        