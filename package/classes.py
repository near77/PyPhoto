import cv2
import os
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
img = cv2.imread('../image/doge.jpg')
def grey_scale(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img

imgg = grey_scale(img)
plt.imshow(imgg, cmap = plt.get_cmap('gray'))
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

cv2.destroyAllWindows()

'''
import pathlib

#define the path
ImageDirectory = pathlib.Path('image/.')

for ImageFile in ImageDirectory.iterdir():  
    print(ImageFile)

'''

