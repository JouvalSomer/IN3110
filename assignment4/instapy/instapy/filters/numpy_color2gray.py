import cv2
import numpy as np

def numpy_color2gray(image):
    """
    Weights the pixels in the given picture to make it gray. 

    Uses slicing to weight all the pixels in the image,
    and ads them to a new array called image_grayscale, (uses numpy optimization).

    Returns a 3d-array of uint8 ints.
    """
    weight_r = 0.21
    weight_g = 0.72
    weight_b = 0.07

    image_grayscale = np.empty_like(image)

    imake_scaling = image[:,:,0]*weight_r + image[:,:,1]*weight_g + image[:,:,2]*weight_b
    
    image_grayscale[:,:,0] = imake_scaling
    image_grayscale[:,:,1] = imake_scaling
    image_grayscale[:,:,2] = imake_scaling
    
    image_grayscale = image_grayscale.astype("uint8")
    cv2.imwrite("background_grayscale.jpeg", image_grayscale)
    return image_grayscale

if __name__ == "__main__":
    image = cv2.imread("background.jpg")
