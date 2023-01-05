# Importing the implementations
from instapy import python_implementation
from instapy import numba_implementation
from instapy import numpy_implementation

# List of the three implementations
implementations = [python_implementation, numba_implementation, numpy_implementation] 

import numpy as np

# Creating a random image and chosing a random row and column 
n_rows = 1080
n_columns = 1920
random_image = np.random.randint(0, 255, (n_rows, n_columns, 3))
row = np.random.randint(0, n_rows)
column = np.random.randint(0, n_columns)

def expected_gray():
    """
    Computes the expected values for the grayscale test by scaling the values in the given image.
    Has three parameters, wich in this case are the global variables random_image row and column.
    Returns a tuple of three values, blue, green and blue.
    """
    weight_r = 0.21
    weight_g = 0.72
    weight_b = 0.07
    
    scaling = random_image[row,column,0]*weight_r + random_image[row,column,1]*weight_g + random_image[row,column,2]*weight_b
    
    r = np.uint8(scaling)
    g = np.uint8(scaling)
    b = np.uint8(scaling)

    return b, g, r 

def expected_sepia():
    """
    Computes the expected values for the sepia test by scaling the values in the given image.
    Has one parameter, wich in this case is the global variable random_image.
    Returns a tuple of three values, blue, green and blue.
    """
    sepia_matrix = [[0.393, 0.769, 0.189],
                    [0.349, 0.686, 0.168],
                    [0.272, 0.534, 0.131]]

    b = np.uint8((random_image[row,column,2]*sepia_matrix[0][0] 
                    + random_image[row,column,1]*sepia_matrix[0][1] 
                    + random_image[row,column,0]*sepia_matrix[0][2])/3)

    g = np.uint8((random_image[row,column,2]*sepia_matrix[1][0] 
                    + random_image[row,column,1]*sepia_matrix[1][1] 
                    + random_image[row,column,0]*sepia_matrix[1][2])/3)

    r = np.uint8((random_image[row,column,2]*sepia_matrix[2][0] 
                    + random_image[row,column,1]*sepia_matrix[2][1] 
                    + random_image[row,column,0]*sepia_matrix[2][2])/3)

    return b, g, r

def test_grayscale():
    """
    Loops through the different implementations of adding the filter gryscale to an image, 
    and tests them by comparing them to randomly generated values 
    in random locations in the array, compluted here in a controlled environment.

    The test can be run as a script or using pytest.

    It takes four parameters, wich in this case are the three global variables random_image, row and column,
    and the function expected_grayscale().

    Asserts that expected == computed, if not, returns a message to the user of dtype string the ints (uint8).
    """
    for imp in implementations:
        b = imp.grayscale_image(random_image, None)[row][column][0]
        g = imp.grayscale_image(random_image, None)[row][column][1]
        r = imp.grayscale_image(random_image, None)[row][column][2]
        computed = b, g, r
        expected = expected_gray()
        print(f'computed = {computed}')
        print(f'expected = {expected}')
        assert expected == computed, f'The {imp} does not work properly. Expected {expected}, but computed {computed}!'

def test_sepia():
    """
    Loops through the different implementations of adding the filter sepia to an image, 
    and tests them by comparing them to randomly generated values 
    in random locations in the array, compluted here in a controlled environment.

    The test can be run as a script or using pytest.

    It takes four parameters, wich in this case are the three global variables random_image, row and column,
    and the function expected_sepia().

    Asserts that expected == computed, if not, returns a message to the user of dtype string the ints (uint8).
    """
    for imp in implementations:
        b = imp.sepia_image(random_image, None)[row][column][0]
        g = imp.sepia_image(random_image, None)[row][column][1]
        r = imp.sepia_image(random_image, None)[row][column][2]
        computed = b, g, r
        expected = expected_sepia()
        print(f'computed = {computed}')
        print(f'expected = {expected}')
        assert expected == computed, f'The {imp} does not work properly. Expected {expected}, but computed {computed}!'

# Running the tests
test_grayscale()
test_sepia()