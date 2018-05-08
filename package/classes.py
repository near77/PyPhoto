import cv2
import os
from PIL import ImageTk, Image
class hello():
    def __init__(self,statement):
        self.statement = statement
    def say(self):
        print('Hello '+self.statement)

def test_cv():
    cap=cv2.VideoCapture(0)
    while True:
        ret,image_np=cap.read()
        cv2.imshow('object detection',image_np)
        if cv2.waitKey(25)&0xFF==ord('q'):
            cv2.destroyAllWindows()
            break
    cap.release()

class blur():
    def __init__(self,filename):
        pass


