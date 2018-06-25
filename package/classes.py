import cv2
import os
from PIL import ImageTk, Image
import matplotlib.pyplot as plt


class Stack():
    def __init__(self):
        self.content = []

    def pop(self):
        target = self.content.pop() 
        return target

    def append(self,item):
        self.content.append(item)
    
    def pop_status(self):
        target = self.content[-1]
        return target

img = cv2.imread("image/save.png")

s = Stack()

s.append(img)
print(len(s.content))
s.append(img)
print(len(s.content))
p = s.pop()
print(len(s.content))
c = s.pop_status()
print(len(s.content))