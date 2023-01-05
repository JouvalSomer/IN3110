<<<<<<< HEAD:assignment4/instapy/bin/instapy.py
from argparse import ArgumentParser 
import cv2

from instapy import python_implementation
from instapy import numpy_implementation
from instapy import numba_implementation

parser = ArgumentParser()

parser.add_argument("-f",
                    "--file",
                    metavar = "FILE",
                    type=str,
                    required=True,
                    help="Type the filename of the image you want to apply a filter to.")

parser.add_argument("-se",
                    "--sepia",
                    action = "store_true",
                    help="Selects the sepia filter.")

parser.add_argument("-g",
                    "--gray",
                    action = "store_true",
                    help="Selects the grayscale filter.")

parser.add_argument("-i",
                    "--implementation",
                    metavar = "{python, numpy, numba}",
                    type=str,
                    help="Select the implementation you want to use.")

parser.add_argument("-o",
                    "--out",
                    metavar = "OUT",
                    type=str,
                    help="Select the output filename you want to use.")

args = parser.parse_args()

image = cv2.imread(args.file)

if args.out:
    output_filename = args.out
else:
    output_filename = None

if args.sepia:
    if args.implementation:
        implementation = args.implementation
        if implementation == "python":
            image = python_implementation.sepia_image(image, output_filename)
        if implementation == "numpy":
            image = numpy_implementation.sepia_image(image, output_filename)
        if implementation == "numba":
            image = numba_implementation.sepia_image(image, output_filename)
    else:
        image = numpy_implementation.sepia_image(image, output_filename)


elif args.gray:
    if args.implementation:
        implementation = args.implementation
        if implementation == "python":
            image = python_implementation.grayscale_image(image, output_filename)
        if implementation == "numpy":
            image = numpy_implementation.grayscale_image(image, output_filename)
        if implementation == "numba":
            image = numba_implementation.grayscale_image(image, output_filename)
    else:
        image = numpy_implementation.grayscale_image(image, output_filename)

=======
from argparse import ArgumentParser 
import cv2
import sys, os

sys.path.append(os.path.abspath(os.path.join(__file__,"../..")))

from instapy import python_implementation
from instapy import numpy_implementation
from instapy import numba_implementation

"""
package:
This is the package. includes all the arguments the user can input in the terminal. checks if the user has inputed a file or not.
then checks if the gray filter or sepia filter argument is passed. creates a img from the file argument and checks if the user
passed the scale argument. Calls the functions in filter with the necessary parameters. 

Usage:
its used to get input from the user and calls the different functions that the user wants to use on the img

"""

parser = ArgumentParser()

parser.add_argument("-f",
                    "--file",
                    metavar = "FILE",
                    type=str,
                    required=True,
                    help="Type the filename of the image you want to apply a filter to.")

parser.add_argument("-se",
                    "--sepia",
                    action = "store_true",
                    help="Selects the sepia filter.")

parser.add_argument("-g",
                    "--gray",
                    action = "store_true",
                    help="Selects the grayscale filter.")

parser.add_argument("-i",
                    "--implementation",
                    metavar = "{python, numpy, numba}",
                    type=str,
                    help="Select the implementation you want to use.")

parser.add_argument("-o",
                    "--out",
                    metavar = "OUT",
                    type=str,
                    help="Select the output filename you want to use.")

parser.add_argument('-sc',
                    "--scale",
                    help="Scale for resize img",
                    action='store_true')

args = parser.parse_args()

image = cv2.imread(args.file)

if args.scale:
    image = cv2.resize(image, (0 , 0) ,fx =0.5 ,fy =0.5)  

if args.out:
    output_filename = args.out
else:
    output_filename = None

if args.sepia:
    if args.implementation:
        implementation = args.implementation
        if implementation == "python":
            image = python_implementation.sepia_image(image, output_filename)
        if implementation == "numba":
            image = numba_implementation.sepia_image(image, output_filename)
    else:
        image = numpy_implementation.sepia_image(image, output_filename)
    if(output_filename != None):
        cv2.imwrite(output_filename, image)


elif args.gray:
    if args.implementation:
        implementation = args.implementation
        if implementation == "python":
            image = python_implementation.grayscale_image(image, output_filename)
        if implementation == "numba":
            image = numba_implementation.grayscale_image(image, output_filename)
    else:
        image = numpy_implementation.grayscale_image(image, output_filename)
    if(output_filename != None):
        cv2.imwrite(output_filename, image)
>>>>>>> 2d584c6b2718dde66912d4c4a33ebb461354228b:assignment4/instapy/bin/this_instapy.py
