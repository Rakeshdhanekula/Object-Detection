


def main():
    import cv2
    import matplotlib.pyplot as plt
    import numpy as np

    image = cv2.imread("kang0.jpg")
    tmp =image
    w = image.shape[1]
    h = image.shape[0]
    scaling = 2
    factor = 2
    w_width = 50
    w_height = 50
    temp =1
    count = 1
    width = 50
    height = 50
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
                            # you can change strides by modifying w_width and w_height in the step size section
                            for x in range(0, image.shape[1]-w_width, w_width):
                                for y in range(0, image.shape[0]-w_height, w_height):
                                    new_cut = cv2.rectangle(image, (x,y), (x+w_width, y+w_height), (255,0,0),1)
                                    plt.imshow(np.array(new_cut).astype('uint8'))

                            w_width = int((image.shape[1]*scaling)/1)

                        else:
                            tmp = 0

                    w_height = int((image.shape[0]*scaling)/1)
                    w_width = width
                    temp = 1

                else:
                    temp = 0


           
            ab = int(image.shape[1]/factor)
            ba = int(image.shape[0]/factor)
    
            image = cv2.resize(image, (ab, ba))
            count = 1
            w_width = width
            w_height = height

        else:
            count = 0


    plt.show()

                    
if __name__ =='__main__':
    main()
