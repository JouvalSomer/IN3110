import cv2
import numpy as np

def python_color2sepia(image):
    """
    Weights the pixels in the given picture to put a sepia filter on it.

    Loops through all the pixels in the image, weights them 
    and ads them to a new array called image_sepia.

    Returns a 3d-array of uint8 ints.

    """
    sepia_matrix = [[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]]

    imgH = image.shape[0]
    imgW = image.shape[1]

    img_sepia = np.zeros((imgH,imgW, 3))
    
    for n in range (0, imgH):
        for m in range (0, imgW):
            b=int(image[n,m,0] * (0.393 ) + image[n,m,1] * (0.769 ) + image[n,m,2] * (0.189 ))
            g=int(image[n,m,0] * (0.349 ) + image[n,m,1] * (0.686 ) + image[n,m,2] * (0.168 ))
            r=int(image[n,m,0] * (0.272 ) + image[n,m,1] * (0.534 ) + image[n,m,2] * (0.131 ))

            r= min(255,r)
            g= min(255,g)
            b= min(255,b)

            img_sepia[n,m,0] = r
            img_sepia[n,m,1] = g
            img_sepia[n,m,2] = b

                
    img_sepia = img_sepia.astype("uint8")
    cv2.imwrite("background_sepia.jpeg", img_sepia)
    return img_sepia

if __name__ == "__main__":
    image = cv2.imread("background.jpg")

