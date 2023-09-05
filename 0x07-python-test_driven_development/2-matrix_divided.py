#!/usr/bin/python3
"""
    This module defines a function matrix_divided
"""
def matrix_divided(matrix, div):
    """
    divides all elements of a matrix by div
    
    Args:
        matrix: Matrix of equal row length
        div: number to divide each element by

    Returns:
        New matrix with completed division
    
        Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero
        TypeError: If each row of the matrix does not have the same size
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    rowlen=len(matrix[0])
    if any(len(row) != rowlen for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    newMatrix = []
    for row in matrix:
        newRow = [val / div for val in row]
        newMatrix.append(newRow)
        
    return newMatrix
