import cv2
from ultralytics import YOLO

class Detector:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.model = YOLO('yolov8n.pt')  # load an official model

    def detect(self):
        result, image = self.cam.read()
        image = cv2.imread('../../test.jpg')
        if True:
            image = cv2.resize(image, (320, 320))
            return self.model(image)  # predict on an image
        else:
            return None
        