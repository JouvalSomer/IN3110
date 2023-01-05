import cv2
import numpy as np


def python_color2gray(bgr):
    """
        Function to convert a bgr image to a grayscale image using the weighted method
        All calculations are done in pure python
        Values for colors weight:
            Red: 0.07, Green: 0.72, Blue: 0.21
        Arguments:
            Numpy array of BGR values
        Returns:
            Numpy array of grayscale values
    """
    for i, p in enumerate(bgr):    
        for j, cell in enumerate(p):
            # blue is on the first index in cell, so multiply this with 0.21        
            bgr[i][j] = int(0.21 * cell[0] +  0.72 * cell[1] + 0.07 * cell[2])
    # print(np.shape(bgr))
    print(bgr[100,100,0])
    print(bgr[100,100,1])
    print(bgr[100,100,2])
    gray = bgr[:, :, :1]

    print(gray[100,100,:])
    # print(np.shape(gray))
    gray = gray.astype("uint8")
    cv2.imwrite("background_grayscale.jpeg", gray)                                          
    return gray





image = cv2.imread("background.jpg")
python_color2gray(image)