import cv2
import os
from PIL import ImageTk, Image
import matplotlib.pyplot as plt


path = os.path.abspath('')
path = path+'/image/template/'
print(path)
fileNum = 0
for item in os.listdir(path):
    fileNum = fileNum+1
print(fileNum)

