import cv2
from ultralytics import YOLO

class Detector:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.model = YOLO('yolov8n.pt')  # load an official model

    
    def detect(self):
        """Takes an image and returns the number of people detected by the camera"""
        
        result = False
        image = None
        # grab frames a bunch of times to clear the buffer (cv2 does not have a better way)
        for i in range(5):
            self.cam.grab()
        result, image = self.cam.read()
        if result:
            image = cv2.resize(image, (320, 320)) # not super necessary but might save memory
            results = self.model(image, verbose=False) # predict on an image
            
            ## uncomment to save the image with the bounding boxes
            # annotated_frame = results[0].plot()
            # cv2.imwrite('out.jpg',annotated_frame)

            names = self.model.names
            # get the 'person' class id
            person_id = list(names)[list(names.values()).index('person')]
            # count 'person' objects in the results
            personCount = results[0].boxes.cls.tolist().count(person_id)
            return personCount
        else:
            return None
