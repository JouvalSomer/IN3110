import numpy as np
class Array:

    def __init__(self, shape, *values):
        """
        Initialize an array of  one of more dimensionalities. Elements can only be of type:
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

        # If the array is 1d:
        self.d_1 = True
        if np.size(shape) == 1 or shape[1] == 0:
            # Checks if the size of the array is 
            if shape != np.shape(values):
                    raise ValueError('The number of values does not fit with the shape.')

            # Converts all values to floats and adds them to self.array
            for val in values:
                self.array.append(float(val))
        
        # If the array is > 1d:
        else:
            self.d_1 = False
            # Checks if the size of the array is 
            if shape[0]*shape[1] != len(values):
                    raise ValueError('The number of values does not fit with the shape.')

            # Adds the elements from values to the associated array shape
            p = 0
            for i in range(shape[0]):
                # Append an empty sublist inside the list
                self.array.append([])
                for j in range(shape[1]):
                    # Appending the values
                    self.array[i].append(float(values[p]))
                    p += 1
        
    def __getitem__ ( self , row, column ):
        """ Returns value of item in array .
            Args :
            item (int): Index of value to return .
            Returns :
            value : Value of the given item .
        """
        return self.array[row][column]

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        return self.array

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """   
        # Checks if other is of correct data type
        if not isinstance(other, (Array, int, float)):
            raise TypeError('The addend has to be of type Array, int or float.')

        # If other is of type Array:
        elif isinstance(other, Array):
            if other.shape != self.shape:
                return NotImplemented
            elif self.d_1:
                length = np.arange(len(self.array))
                for (i, j, k) in zip(self.array, other.array, length):
                    self.array[k] = i + j
                return self.array
            else:
                for i, (x, y) in enumerate(zip(self.array, other.array)):
                    for j in range(2):
                        self.array[i][j] = x[j] + y[j]
                return self.array

        # If other is of type float:  
        elif isinstance(other, float):
            if self.d_1:
                self.array = list(map(lambda x: x + other, self.array))
                return self.array
            else:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self.array[i][j] = self.array[i][j] + other
                return self.array

        
        # If other is of type int:
        elif isinstance(other, int):
            other = float(other)
            if self.d_1:
                self.array = list(map(lambda x: x + other, self.array))
                return self.array
            else:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self.array[i][j] = self.array[i][j] + other
                return self.array


    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        # Checks if other is of correct data type
        if not isinstance(other, (Array, int, float)):
            raise TypeError('The subtrahend has to be of type Array, int or float.')

        # If other is of type Array:
        elif isinstance(other, Array):
            if other.shape != self.shape:
                return NotImplemented
            elif self.d_1:
                length = np.arange(len(self.array))
                for (i, j, k) in zip(self.array, other.array, length):
                    self.array[k] = i - j
                return self.array
            else:
                for i, (x, y) in enumerate(zip(self.array, other.array)):
                    for j in range(2):
                        self.array[i][j] = x[j] - y[j]
                return self.array

        # If other is of type float:  
        elif isinstance(other, float):
            if self.d_1:
                self.array = list(map(lambda x: x + other, self.array))
                return self.array
            else:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self.array[i][j] = self.array[i][j] - other
                return self.array

        
        # If other is of type int:
        elif isinstance(other, int):
            other = float(other)
            if self.d_1:
                self.array = list(map(lambda x: x - other, self.array))
                return self.array
            else:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self.array[i][j] = self.array[i][j] - other
                return self.array

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        # Checks if other is of correct data type
        if not isinstance(other, (Array, int, float)):
            raise TypeError('The factor(s) has to be of type Array, int or float.')

        # If other is of type Array:
        elif isinstance(other, Array):
            if other.shape != self.shape:
                return NotImplemented
            elif self.d_1:
                length = np.arange(len(self.array))
                for (i, j, k) in zip(self.array, other.array, length):
                    self.array[k] = i*j
                return self.array
            else:
                for i, (x, y) in enumerate(zip(self.array, other.array)):
                    for j in range(2):
                        self.array[i][j] = x[j]*y[j]
                return self.array

        # If other is of type float:  
        elif isinstance(other, float):
            if self.d_1:
                self.array = list(map(lambda x: x*other, self.array))
                return self.array
            else:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self.array[i][j] = self.array[i][j]*other
                return self.array

        
        # If other is of type int:
        elif isinstance(other, int):
            other = float(other)
            if self.d_1:
                self.array = list(map(lambda x: x*other, self.array))
                return self.array
            else:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        self.array[i][j] = self.array[i][j]*other
                return self.array
            
    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """
        if self.d_1:
            if other.shape != self.shape or not isinstance(other, Array) or self.array != other.array:
                return False
            else:
                return True
        else:
            if other.shape != self.shape or type(other.values) != type(self.values) or other.array != self.array:
                return False
            else:
                return True

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """
        
        # Checks if other is of correct data type
        if not isinstance(other, (Array, int, float)):
            raise TypeError('Has to be of type Array, int or float.')

        # If other is of type Array:
        elif isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError('Shape not equal.')

            else:
                booleans = []
                if self.d_1:
                    for (element1, element2) in zip(self.array, other.array):
                        if element1 == element2:
                            booleans.append(True)
                        elif element1 != element2:
                            booleans.append(False)
                    return booleans

                else:
                    for i in range(self.shape[0]):
                        for j in range(self.shape[1]):
                            if self.arry[i][j] == other.array[i][j]:
                                booleans.append(True)
                            elif self.arry[i][j] != other.array[i][j]:
                                booleans.append(False)
                    return booleans

        # If other is of type int or float
        elif isinstance(other, (int,float)):
            booleans = []
            if self.d_1:
                for element in self.array:
                    if element == other:
                        booleans.append(True)
                    elif element != other:
                        booleans.append(False)
                return booleans
            else:
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        if self.arry[i][j] == other:
                            booleans.append(True)
                        elif self.arry[i][j] != other:
                            booleans.append(False)
                return booleans

    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for type int and float (not boolean).
        Returns:
            float: The value of the smallest element in the array.
        """
        return min(self.values)
