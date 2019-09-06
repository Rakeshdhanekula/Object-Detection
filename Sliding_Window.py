import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("kang0.jpg")
tmp =image
w = image.shape[1]
h = image.shape[0]
scaling = 1.2
factor = 0.8
w_width = 50
w_height = 50
temp =1
count = 1
width = 50
height = 50

def resizing(image, factor):
    ab = image.shape[1]*factor/1
    ba = image.shape[0]*factor/1
    
    new_resize = cv2.resize(image, (ab, ba))
    return new_resize

def width(image, scaling):
    new_width = image.shape[1]*scaling/1
    return new_width

def height(image, scaling):
    new_height = image.shape[0]*scaling/1
    return new_height

while count == 1:
    if image.shape[1] >= w_width and image.shape[0] >= w_height:
        count = 1
        temp = 1
        tmp = 1
        while temp == 1:
            if w_width <= image.shape[1] and w_height <= image.shape[0]:
                tmp = 1
                while tmp == 1:
                    if w_width <= image.shape[1] and w_height <= image.shape[0]:
                        for x in range(0, image.shape[1]-w_width, w_width):
                            for y in range(0, image.shape[0]-w_height, w_height):
                                new_cut = cv2.rectangle(image, (x,y), (x+w_width, y+w_height), (255,0,0),1)
                                plt.imshow(np.array(new_cut).astype('uint8'))

                        w_width = width(image, scaling)

                    else:
                        tmp = 0

                w_height = height(image, scaling)
                w_width = width
                temp = 1

            else:
                temp = 0

        image = resizing(image, factor)
        count = 1
        w_width = width
        w_height = height

    else:
        count = 0


plt.show()

                    
            
