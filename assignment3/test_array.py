from array_class import Array
import numpy as np


def test_Array_nice_print():
    # Check that your print function returns the nice string
    inst = Array((4,), 1, 2, 3, 4)
    expected = [1.0, 2.0, 3.0, 4.0]
    computed = inst.__str__()
    assert computed == expected, ''

def test_add_Array_with_a_number():
    # One or more tests verifying that adding to a 1d-array element-wise returns what it’s supposed to
    # Test for adding a number
    values_to_add = [5, 1, 3, 7]
    for val in values_to_add:
        inst = Array((4,), 1, 2, 3, 4)
        computed = inst.__add__(val)
        expected = [1.0 + val, 2.0 + val, 3.0 + val, 4.0 + val]
        assert computed == expected, ''

    # Test for adding an array
    inst = Array((4,), 1, 2, 3, 4)
    inst2 = Array((4,), *values_to_add)
    computed = inst.__add__(inst2)
    expected =  [6, 3, 6, 11]
    assert computed == expected, f'computed {computed}, expected {expected}'

def test_subtract_Array_with_a_number():
    # One or more tests verifying that substracting from a 1d-array elementwise returns what it’s supposed to
    values_to_add = [5, 1, 3, 7]
    for val in values_to_add:
        inst = Array((4,), 1, 2, 3, 4)
        computed = inst.__sub__(val)
        expected = [1.0 - val, 2.0 - val, 3.0 - val, 4.0 - val]
        assert computed == expected, ''

    # Test for adding an array
    inst = Array((4,), 1, 2, 3, 4)
    inst2 = Array((4,), *values_to_add)
    computed = inst.__sub__(inst2)
    expected =  [-4, 1, 0, -3]
    assert computed == expected, f'computed {computed}, expected {expected}'

def test_multiply_Array_by_a_factor():
    # One or more tests verifying that multiplying a 1d-array element-wise by a factor returns what it’s supposed to
    values_to_add = [0, 1, 3, 7]
    for i in values_to_add:
        inst = Array((4,), 1, 2, 3, 4)
        computed = inst.__mul__(i)
        expected = [1.0*i, 2.0*i, 3.0*i, 4.0*i]
        assert computed == expected, ''

def test_multiply_Array_by_an_array():
    inst2 = Array((4,), 0, 1, 3, 7)
    inst = Array((4,), 1, 2, 3, 4)
    computed = inst.__mul__(inst2)
    expected =  [0, 2, 9, 28]
    assert computed == expected, ''
    # One or more tests verifying that multiplying a 1d-array element-wise by a 1-d array returns what it’s supposed to

def test_boolean_equality():
    # One or more tests verifying that comparing arrays (by ==) returns what it is supposed to - which should be a boolean.
    a = []
    expected_boolean = [True, True, True, True]
    for (i, ex) in enumerate(expected_boolean):
        print(i)
        a.append(i+1)
        print(a)
        length = len(a)
        inst = Array((length,), *a)
        computed = inst.__eq__(inst)
        assert computed == ex,''

def compare_element_wise_equality():
    # Verifying that comparing a 1d-array element-wise to another array through is equal returnsa boolean array
    inst1 = Array((4,), 72, -3, 15, 19)
    inst2 = Array((4,), 72, -3, 15, 19)
    computed = inst1.min_element(inst2)
    expected = [True, True, True, True]
    assert computed == expected, ''

def min_element_in_array():
    # Verifying that the the element returned by min element is the ”smallest” one in the array
    inst1 = Array((4,), 72, -3, 15, 19)
    #elements_to_compare = []
    computed = inst1.min_element()
    expected = -3
    assert computed == expected, ''