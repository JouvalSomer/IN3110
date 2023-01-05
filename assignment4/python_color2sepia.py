import cv2
import numpy as np

def python_color2sepia(image):
    """
    Function:
    This is the sepia filter function for python. it takes in a img and sepia grade, then makes a empty img with same size as inp img with depth 3.
    then loops through empty img and adds the input img multiplied with the sepia filter with the users inputed sepia grade.
    Puts the 3 depts b g r into the output img

    Usage:
    its used to change a img to a sepia image. This is a slow way to do it compaired to the 2 other.

    Para and Ret:
    parameter is a img and a sepia grade, and returns the img with sepia (int)
    """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    sepia_matrix = [[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]]

    background_sepia = np.empty_like(image)
    n_rows = len(image)
    n_columns = len(image[0])
    for i in range(n_rows):
        for j in range(n_columns):
            for k in range(3):
                background_sepia[i][j][k] = min(255,(
                    image[i][j][0]*sepia_matrix[k][0] 
                    + image[i][j][1]*sepia_matrix[k][1] 
                    + image[i][j][2]*sepia_matrix[k][2]))
                
                
    background_sepia = background_sepia.astype("uint8")
    background_sepia = cv2.cvtColor(background_sepia, cv2.COLOR_RGB2BGR)

    return background_sepia

if __name__ == "__main__":
    image = cv2.imread("rain.jpg")
    cv2.imwrite("background_sepia.jpeg", python_color2sepia(image))

