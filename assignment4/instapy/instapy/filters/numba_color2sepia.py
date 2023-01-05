import cv2
import numpy as np
from numba import jit

@jit
def numba_color2sepia(image):
    """
    Weights the pixels in the given picture to put a sepia filter on it. 

    Loops through all the pixels in the image, weights them 
    and ads them to a new array called image_sepia, (uses numba optimization).
    The new red pixel is a spesific weighted compination of the old red, green and blue, 
    same with the new green and blue pixels. 

    Returns a 3d-array of uint8 ints.
    """
    sepia_matrix = [[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]]

    image_sepia = np.empty_like(image)

    n_rows = len(image)
    n_columns = len(image[0])
    for i in range(n_rows):
        for j in range(n_columns):
            for k in range(2,-1,-1):
                image_sepia[i][j][k] = ((
                    image[i][j][2]*sepia_matrix[k][0] 
                    + image[i][j][1]*sepia_matrix[k][1] 
                    + image[i][j][0]*sepia_matrix[k][2])/3)

    image_sepia = image_sepia.astype(np.uint8)
    cv2.imwrite("background_sepia.jpeg", image_sepia)
    return image_sepia

if __name__ == "__main__":
    image = cv2.imread("background.jpg")

