import cv2
from ultralytics import YOLO

class Detector:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        # self.cam.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.model = YOLO('yolov8n.pt')  # load an official model

    def detect(self):
        result = False
        image = None
        # grab frames a bunch of times to clear the buffer (cv2 does not have a better way)
        for i in range(5):
            self.cam.grab()
        result, image = self.cam.read()
        if result:
            image = cv2.resize(image, (320, 320))
            # return self.model(image)  # predict on an image
            # test section (delete later)
            results = self.model(image)
            annotated_frame = results[0].plot()
            cv2.imwrite('out.jpg',annotated_frame)

        else:
            return None
        