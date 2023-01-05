import cv2
import numpy as np
from numba import jit

@jit
def numba_color2sepia(image):
    """
    Function:
    This is the sepia filter function for numba. it takes in a img and sepia grade, then makes a empty img with same size as inp img.
    then loops through empty img and adds the input img multiplied with the sepia filter with the users inputed sepia grade.

    Usage:
    its used to change a img to a sepia image. This is the fasted way to implement comparing the 3 ways. But it takes some time to compilate.

    Para and Ret:
    parameter is a img and a sepia grade, and returns the img with sepia (int)
    """
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    sepia_matrix = [[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]]

    background_sepia = np.empty_like(image)
    n_rows = len(image)
    n_columns = len(image[0])
    for i in range(n_rows):
        for j in range(n_columns):
            for k in range(2,-1,-1):
                background_sepia[i][j][k] = min(255,(
                    image[i][j][2]*sepia_matrix[k][0] 
                    + image[i][j][1]*sepia_matrix[k][1] 
                    + image[i][j][0]*sepia_matrix[k][2]))
    # astype("uint8") 
    background_sepia = background_sepia.astype(np.uint8)
    # background_sepia = cv2.cvtColor(background_sepia, cv2.COLOR_RGB2BGR)

    return background_sepia


if __name__ == "__main__":
    image = cv2.imread("rain.jpg")
    cv2.imwrite("background_sepia.jpeg", numba_color2sepia(image))

