#!/usr/bin/python3
"""
This module contains a function that  multiplies 2 matrices by using the module NumPy
"""
import numpy as np
def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices
    Args:
        m_a: first argument
        m_b: second argument
    Returns:
        The multiplication of the two arguments
    Raises:
        TypeError: If m_a or m_b are not lists
        TypeError: If m_a or m_b are not lists of lists
        ValueError: If m_a or m_b are empty lists or matrices
        TypeError: If m_a or m_b contain a non int or float
        TypeError: If m_a or m_b are not rectangular
        ValueError: If m_a or m_b can't be multiplied
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    m_a = np.array(m_a)
    m_b = np.array(m_b)
    return m_a.dot(m_b)
