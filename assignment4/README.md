
# README.md Assignment4

### Prerequisites

You must have numpy, numba, argparse and cv2. Use pip install to install them all:

Numpy:
```
pip install numpy
```
Numba:
```
pip install numba
```
Argparse:
```
pip install argparse
```
cv2
```
pip install cv2
```

### Functionality

The package applies ether a sepia of a grayscale filter to a given image.

### Missing Functionality

The package only has sepia and grayscale filters. The sepia filter does not have a stepless functionality.

### Usage

After installing the package it can be used by running instapy.py followed by the wanted command line arguments.

The available arguments are

-f: The filename of the image you want to aff a filter on
-se: Applies the sepia filter
-g: Applies the grayscale filter
-i: Selects an implementation to add the filter. Can be python, numba or numpy
-o: Setts the output name of the image after the filter is applied

An example:

```
instapy.py -f background.jpg -g
```
### Note from writer
When trying to run the example above I get the following Importerror:

ImportError: cannot import name 'python_implementation' from 'instapy' (C:\Users\47995\Documents\3. aaret\1. semester\IN3110\IN3110-jmsomer\assignment4\instapy\bin\instapy.py)


#README peer review of assignment 4, some of the steps i edited or added code during the review:
by Jorgelun

1. Added docstrings to all of your py files in assignment 4 folder.

2. added rain.jpg and changed it from background to rain to compare with my results.

3. the code is good structured and easy to read.

4. removed the implementation == numpy in your package since it is in the else and dosent need to be there

5. added docstring and a scale args into your package

6. as you mention above you get a import error in the package. I added sys.path.append line in your package that fixes this problem
i also changed the name from instapy to this_instapy because i had a problem naming it instapy because package name problem.
dont now if this is a problem for you but i had to do it to test the program.

7. implemented the -sc so the user can use scaling of the output img

8. added image in same folder as package so i can just call -f rain.jpg

9. changed some code in the assignment4\instapy\instapy\filters\python_color2sepia.py so the python implementasion works since you had a index error

So to recap i added some docstrings. Removed som uncessesary code.
added docstring and scale into your package
changed some code to the python sepia part of your package works.
e.g. python this_instapy.py -f rain.jpg -se -i python -o test.jpg      Will now work :D
