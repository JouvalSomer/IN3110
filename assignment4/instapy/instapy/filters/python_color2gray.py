import cv2
import numpy as np

def python_color2gray(image):
    """
    Weights the pixels in the given picture to make it gray. 

    Loops through all the pixels in the image, weights them 
    and ads them to a new array called image_grayscale.

    Returns a 3d-array of uint8 ints.
    """
    weight_r = 0.21
    weight_g = 0.72
    weight_b = 0.07

    image_grayscale = np.empty_like(image)
    
    n_rows = len(image)
    n_columns = len(image[0])
    for i in range(n_rows):
        for j in range(n_columns):
            for k in range(3):
                image_grayscale[i,j,k] = (image[i,j,0]*weight_r 
                                        + image[i,j,1]*weight_g 
                                        + image[i,j,2]*weight_b)

    image_grayscale = image_grayscale.astype("uint8")
    cv2.imwrite("background_grayscale.jpeg", image_grayscale)
    return image_grayscale

if __name__ == "__main__":
    image = cv2.imread("background.jpg")

