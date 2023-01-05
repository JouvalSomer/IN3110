from .filters import python_color2gray as gray
from .filters import python_color2sepia as sepia

def grayscale_image(input_filename, output_filename=None):
    """
    Feeds input_filename or output_filename to the function numpy_color2gray 
    in the file numpy_color2gray.py in the folder filters.

    Two parameters, input_filename and the optional output_filename.

    Returs the grayed image, dtype array
    """
    if output_filename != None:
        return gray.python_color2gray(input_filename)
    else:
        return gray.python_color2gray(input_filename)

def sepia_image(input_filename, output_filename=None):
    """
    Feeds input_filename or output_filename to the function numpy_color2sepia 
    in the file numpy_color2sepia.py in the folder filters.

    Two parameters, input_filename and the optional output_filename.

    Returs the sepiad image, dtype array 
    """
    if output_filename != None:
        return sepia.python_color2sepia(input_filename)
    else:
        return sepia.python_color2sepia(input_filename)