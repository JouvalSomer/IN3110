import time 
import cv2

def runtime(f, image):
    """
    Computes the average time it takes to put a filter on an image 
    by running it three times and returning the average of the three, dtype floate.
    """
    r = []
    for i in range(3):
        start = time.time()
        f(image)
        end = time.time()
        r.append(end - start)
    return sum(r)/3

def Task_4_1(image):
    """
    Writes the reports for task 4.1.
    Takes an image as a parameter.
    Returns three files, one for each implementation, with the corresponding text. 
    """
    from python_color2gray import python_color2gray
    from numpy_color2gray import numpy_color2gray
    from numba_color2gray import numba_color2gray

    python_time = runtime(python_color2gray, image)
    numpy_time = runtime(numpy_color2gray, image)
    numba_time = runtime(numba_color2gray, image)

    def python_numpy_diff(python, numpy):
        """
        Computers the the difference in time between the python and numpy implementations.
        Takes to parameters, pythen and numpy, wich both are the times used by their respectiv implementations.
        Returns a string wich states how many times one is faster than the other.
        """
        if (python/numpy) > 1:
            return f"Average runtime of numpy_color2gary is {round(python/numpy)} times faster than python_color2gray\n"
        else:
            return f"Average runtime of python_color2gary is {round(numpy/python)} times faster than numpy_color2gray\n"

    def numba_python_diff(python, numba):
        """
        Computers the the difference in time between the python and numba implementations.
        Takes to parameters, pythen and numba, wich both are the times used by their respectiv implementations.
        Returns a string wich states how many times one is faster than the other.
        """
        if (python/numba) > 1:
            return f"Average runtime of numba_color2gary is {round(python/numba)} times faster than python_color2gray\n"
        else:
            return f"Average runtime of python_color2gary is {round(numba/python)} times faster than numpy_color2gray\n"

    def numba_numpy_diff(numpy, numba):
        """
        Computers the the difference in time between the numpy and numba implementations.
        Takes to parameters, numpy and numba, wich both are the times used by their respectiv implementations.
        Returns a string wich states how many times one is faster than the other.
        """
        if (numpy/numba) > 1:
            return f"Average runtime of numba_color2gary is {round(numpy/numba)} times faster than numpy_color2gray\n"
        else:
            return f"Average runtime of numpy_color2gary is {round(numba/numpy)} times faster than numba_color2gray\n"

    python_report = "python_report_color2gray.txt"
    numpy_report = "numpy_report_color2gray.txt"
    numba_report = "numba_report_color2gray.txt"

    with open(python_report, "w") as pr:
        pr.write("Timing: python_color2gray\n")
        pr.write(f"Average runtime after running python_color2gray three times: {python_time:.6f}s\n")
        pr.write(f"Timing performed using: {image.shape}")
        
    with open(numpy_report, "w") as nr:
        nr.write("Timing: numpy_color2gray\n")
        nr.write(f"Average runtime after running numpy_color2gray three times: {numpy_time:.6f}s\n")
        nr.write(python_numpy_diff(python_time, numpy_time))
        nr.write(f"Timing performed using: {image.shape}")

    with open(numba_report, "w") as nr:
        nr.write("Timing: numba_color2gray\n")
        nr.write(f"Average runtime after running numba_color2gray three times: {numba_time:.6f}s\n")
        nr.write(numba_python_diff(python_time, numba_time))
        nr.write(numba_numpy_diff(numpy_time, numba_time))
        nr.write(f"Timing performed using: {image.shape}\n")
        nr.write("""One advantages of using numba insted of numpy is the fact that you can write simple python code and donn't have to worry about vectorization or optimization. A disadvantages could be that the code runs slower than vectorized numpy code.""")

def Task_4_2(image):
    """
    Writes the reports for task 4.2.
    Takes an image as a parameter.
    Returns three files, one for each implementation, with the corresponding text. 
    """
    from python_color2sepia import python_color2sepia
    from numpy_color2sepia import numpy_color2sepia
    from numba_color2sepia import numba_color2sepia

    python_time = runtime(python_color2sepia, image)
    numpy_time = runtime(numpy_color2sepia, image)
    numba_time = runtime(numba_color2sepia, image)

    def python_numpy_diff(python, numpy):
        """
        Computers the the difference in time between the python and numpy implementations.
        Takes to parameters, pythen and numpy, wich both are the times used by their respectiv implementations.
        Returns a string wich states how many times one is faster than the other.
        """
        if (python/numpy) > 1:
            return f"Average runtime of numpy_color2sepia is {round(python/numpy)} times faster than python_color2sepia\n"
        else:
            return f"Average runtime of python_color2sepia is {round(numpy/python)} times faster than numpy_color2sepia\n"

    def numba_python_diff(python, numba):
        """
        Computers the the difference in time between the python and numba implementations.
        Takes to parameters, pythen and numba, wich both are the times used by their respectiv implementations.
        Returns a string wich states how many times one is faster than the other.
        """
        if (python/numba) > 1:
            return f"Average runtime of numba_color2sepia is {round(python/numba)} times faster than python_color2sepia\n"
        else:
            return f"Average runtime of python_color2sepia is {round(numba/python)} times faster than numpy_color2sepia\n"

    def numba_numpy_diff(numpy, numba):
        """
        Computers the the difference in time between the numpy and numba implementations.
        Takes to parameters, numpy and numba, wich both are the times used by their respectiv implementations.
        Returns a string wich states how many times one is faster than the other.
        """
        if (numpy/numba) > 1:
            return f"Average runtime of numba_color2sepia is {round(numpy/numba)} times faster than numpy_color2sepia\n"
        else:
            return f"Average runtime of numpy_color2sepia is {round(numba/numpy)} times faster than numba_color2sepia\n"

    python_report = "python_report_color2sepia.txt"
    numpy_report = "numpy_report_color2sepia.txt"
    numba_report = "numba_report_color2sepia.txt"

    with open(python_report, "w") as pr:
        pr.write("Timing: python_color2sepia\n")
        pr.write(f"Average runtime after running python_color2sepia three times: {python_time:.6f}s\n")
        pr.write(f"Timing performed using: {image.shape}")

    with open(numpy_report, "w") as nr:
        nr.write("Timing: numpy_color2sepia\n")
        nr.write(f"Average runtime after running numpy_color2sepia three times: {numpy_time:.6f}s\n")
        nr.write(python_numpy_diff(python_time, numpy_time))
        nr.write(f"Timing performed using: {image.shape}")

    with open(numba_report, "w") as nr:
        nr.write("Timing: numba_color2sepia\n")
        nr.write(f"Average runtime after running numba_color2sepia three times: {numba_time:.6f}s\n")
        nr.write(numba_python_diff(python_time, numba_time))
        nr.write(numba_numpy_diff(numpy_time, numba_time))
        nr.write(f"Timing performed using: {image.shape}\n")
        nr.write("""One advantages of using numba insted of numpy is the fact that you can write simple python code and don't have to worry about vectorization or optimization. A disadvantages could be that the code runs slower than vectorized numpy code.""")

if __name__ == "__main__":
    image = cv2.imread("background.jpg")
    Task_4_1(image)
    Task_4_2(image)