import cv2
import numpy as np

def numpy_color2sepia(image):
    """
    Function:
    This is the sepia filter function for numpy. it takes in a img and sepia grade, then makes a empty img with same size as inp img with depth 3.
    then slices through empty img and adds the input img multiplied with the sepia filter with the users inputed sepia grade.
    Puts the 3 depts together.

    Usage:
    its used to change a img to a sepia image. This is a fast method compared to python but slower than numba if you dont consider
    the compilating time. 


    Para and Ret:
    parameter is a img and a sepia grade, and returns the img with sepia (int)
    """

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    sepia_matrix = [[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]]

    background_sepia = np.empty_like(image)
    
    image_scaling_0 = (image[:,:,0]*sepia_matrix[0][0] + image[:,:,1]*sepia_matrix[0][1] + image[:,:,2]*sepia_matrix[0][2])/3
    image_scaling_1 = (image[:,:,0]*sepia_matrix[1][0] + image[:,:,1]*sepia_matrix[1][1] + image[:,:,2]*sepia_matrix[1][2])/3
    image_scaling_2 = (image[:,:,0]*sepia_matrix[2][0] + image[:,:,1]*sepia_matrix[2][1] + image[:,:,2]*sepia_matrix[2][2])/3

    background_sepia[:,:,0] = image_scaling_0
    background_sepia[:,:,1] = image_scaling_1
    background_sepia[:,:,2] = image_scaling_2

    background_sepia = background_sepia.astype("uint8")
    background_sepia = cv2.cvtColor(background_sepia, cv2.COLOR_RGB2BGR)

    return background_sepia


if __name__ == "__main__":
    image = cv2.imread("rain.jpg")
    cv2.imwrite("background_sepia.jpeg", numpy_color2sepia(image))
