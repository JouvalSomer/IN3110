import numpy as np
class Array_2d()
    def __init__(self, shape, *values):
        """
        Initialize an array of 1-dimensionality. Elements can only be of type:
        - int
        - float
        - bool
        
        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        self.shape = shape
        self.values = values
        self.array = []                

        # Checks if the values are of valid type, i.e. of only one data type
        for val in values:
            if type(val) != type(values[0]):
                raise ValueError(f'An array must only contain one data type!')

        # Checks if the size of the array is 
        if shape != np.shape(values):
                raise ValueError('The number of values does not fit with the shape.')

        # Converts all values to floats and adds them to self.array
        for val in values:
            val = float(val)

        # Creats the array
        # Position in values
        p = 0
        # i in range of number of rows
        for i in range(self.shape[0]):

            # Append an empty sublist inside the list
            self.array.append([])

            # j in range of number of column
            for j in range(self.shape[1]):
                # Adding the correct values to it's correct position
                self.array[i].append(list(values)[p])
                p += 1

    def __add__(self, other):
        for i, (x, y) in enumerate(zip(self.array, other.array)):
            for j in range(2):
                self.array[i][j] = x[j] + y[j]
        return self.array

    def __sub__(self, other):
        for i, (x, y) in enumerate(zip(self.array, other.array)):
            for j in range(2):
                self.array[i][j] = x[j] - y[j]
        return self.array

    def is_equal_2d_array(self, other):
        booleans = []
        for i in range(2):
            for j in range(2):
                if self.arry[i][j] == other.array[i][j]:
                    booleans.append(True)
                elif self.arry[i][j] != other.array[i][j]:
                    booleans.append(False)
        return booleans

    def eq_array(b):
        if np.shape(array.other) != np.shape(a) or type(a) != type(b) or a != b:
            return False
        else:
            return True

inst = Array_2d