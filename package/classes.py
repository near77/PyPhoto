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
        new_stack = self.content
        target = new_stack.pop()
        return target

a = Stack()
a.append("cc")
print(a.content)
a.append("bb")
print(a.content)
b = a.pop()
print(a.content)
print(b)