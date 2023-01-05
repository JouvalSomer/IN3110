<<<<<<< HEAD
import cv2
import numpy as np

def numpy_color2gray(image):
    weight_r = 0.21
    weight_g = 0.72
    weight_b = 0.07
    background_grayscale = np.empty_like(image)

    imake_scaling = image[:,:,0]*weight_r + image[:,:,1]*weight_g + image[:,:,2]*weight_b
    
    background_grayscale[:,:,0] = imake_scaling
    background_grayscale[:,:,1] = imake_scaling
    background_grayscale[:,:,2] = imake_scaling
    
    background_grayscale = background_grayscale.astype("uint8")
    return background_grayscale

if __name__ == "__main__":
    image = cv2.imread("background.jpg")
    cv2.imwrite("background_grayscale.jpeg", numpy_color2gray(image))
=======
import cv2
import numpy as np
import time 

def numpy_color2gray(image):
    """
    Function:
    This is the grayscale function for numpy. it takes in a img and makes a empty img with same size as inp img
    then uses slicing on the 3 depths of the img and adds the input img multiplied with the grayscale filter.

    Usage:
    its used to change a img to a grayscale image. This is a fast method compared to python but slower than numba if you dont consider
    the compilating time.

    Para and Ret:
    parameter is a img, and returns the img with grayscale (int)
    """
    weight_r = 0.21
    weight_g = 0.72
    weight_b = 0.07
    background_grayscale = np.empty_like(image)

    imake_scaling = image[:,:,0]*weight_r + image[:,:,1]*weight_g + image[:,:,2]*weight_b
    
    background_grayscale[:,:,0] = imake_scaling
    background_grayscale[:,:,1] = imake_scaling
    background_grayscale[:,:,2] = imake_scaling
    
    background_grayscale = background_grayscale.astype("uint8")
    return background_grayscale

if __name__ == "__main__":
    image = cv2.imread("rain.jpg")
    cv2.imwrite("background_grayscale.jpeg", numpy_color2gray(image))






>>>>>>> 2d584c6b2718dde66912d4c4a33ebb461354228b
