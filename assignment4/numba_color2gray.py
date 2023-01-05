import cv2
import numpy as np
from numba import jit

@jit
def numba_color2gray(image):
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
    n_rows = len(image)
    n_columns = len(image[0])
    for i in range(n_rows):
        for j in range(n_columns):
            for k in range(3):
                background_grayscale[i,j,k] = image[i,j,0]*weight_r + image[i,j,1]*weight_g + image[i,j,2]*weight_b
    background_grayscale = background_grayscale.astype(np.uint8)
    return background_grayscale


if __name__ == "__main__":
    image = cv2.imread("rain.jpg")
    cv2.imwrite("background_grayscale.jpeg", numba_color2gray(image))

