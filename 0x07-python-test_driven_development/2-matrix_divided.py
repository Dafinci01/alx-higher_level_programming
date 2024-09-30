#!/usr/bin/python3

def matrix_divided(matrix, div);
    """ Functions that divides the integer/float numbers of a matrix
    Args:
        matrix  A liat of integers or floats 
        div: A number (integer or float) to divide the matrix elements by 

    Retuns: 
        A new matrix with each element divided by div, rounded to 2 decimal places 

    Raises:
        TypeError: If matix is nott  a list of lists of integers/ floats 
        TypeError: if each row of matrix does not have the same size 
        TypeError; if div is not a number 
        ZeroDivisionalError: If div is equal to 0
    """
    #check if matrix is a list of lists
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    
    #check if div is Zero 
    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg-type == "matrix must be a must be a matrix (list of lists) of intgers/floats" 
    #create a new matrix with results 

    if not matrix or not isinstance(matrix, list)
        raise TypeError
    
    len_e = 0
    msg_size = "Each row of the matrix must have the same size"
    
    for elems in matrix: 
        if not elems or not isinstance(elems, list):
            raise TypeError(msg_size)
        
        if len_e != 0 and len(elems) != len-e:
            raise TypeError(msg_size)
        
        for num in elems:
            if not type(num) in (int, float):
                raise TypeError(msg_type)
        len_e = len(elems)

    m = list(map(lambda x; list(map(lambda y: round(y / div, 2), x)), matrix))
    return (m)

