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

    def push(self,item):
        self.content.append(item)
    
    def pop_status(self):
        target = self.content[-1]
        return target

class Queue():
    def __init__(self):
        self.content = []

    def dequeue(self):
        target = self.content.pop(0) 
        return target

    def inqueue(self,item):
        self.content.insert(0,item)



def BubbleSortImg(InputList):#sorted by size
    imglist=[]
    path = os.path.abspath('')+'/image/album/'
    for item in InputList:
        img = cv2.imread(path+item)
        imglist.append(img)
    for i in range(len(imglist)-1,-1,-1):
        for j in range(i):
            if len(imglist[j]) > len(imglist[j+1]):
                imglist[j], imglist[j+1] = imglist[j+1], imglist[j]
    return imglist

path = os.path.abspath('')+'/image/album/'
File = "2.jpg"
for the_file in os.listdir(path):
    file_path = os.path.join(path, the_file)
    try:
        if os.path.isfile(file_path) and the_file == File:
            os.unlink(file_path)
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)