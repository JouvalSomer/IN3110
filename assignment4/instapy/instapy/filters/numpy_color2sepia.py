import cv2
import numpy as np

def numpy_color2sepia(image):
    """
    Weights the pixels in the given picture to put a sepia filter on it. 

    Uses slicing to weight all the pixels in the image,
    and ads them to a new array called image_sepia, (uses numpy optimization).
    The new red pixel is a spesific weighted compination of the old red, green and blue, 
    same with the new green and blue pixels. 

    Returns a 3d-array of uint8 ints.
    """
    sepia_matrix = [[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]]

    image_sepia = np.empty_like(image)
    
    image_scaling_0 = ((image[:,:,2]*sepia_matrix[0][0] 
                    + image[:,:,1]*sepia_matrix[0][1] 
                    + image[:,:,0]*sepia_matrix[0][2])/3)

    image_scaling_1 = ((image[:,:,2]*sepia_matrix[1][0] 
                    + image[:,:,1]*sepia_matrix[1][1] 
                    + image[:,:,0]*sepia_matrix[1][2])/3)

    image_scaling_2 = ((image[:,:,2]*sepia_matrix[2][0] 
                    + image[:,:,1]*sepia_matrix[2][1] 
                    + image[:,:,0]*sepia_matrix[2][2])/3)

    image_sepia[:,:,0] = image_scaling_0
    image_sepia[:,:,1] = image_scaling_1
    image_sepia[:,:,2] = image_scaling_2

    image_sepia = image_sepia.astype("uint8")
    cv2.imwrite("background_sepia.jpeg", image_sepia)
    return image_sepia

if __name__ == "__main__":
    image = cv2.imread("background.jpg")

