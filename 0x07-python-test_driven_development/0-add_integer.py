#!/usr/bin/python3

def add_integer(a, b=98)
    """Add two integers or floats and  return the result as an integer 
    Args:
        a: the first number (can be an integer or float)
        b: the second number (can be an integer or float, defult is 98)

    Returns: 
        thee sum of a and b as an integer 

    Raises: 
        TypeError: If a or b is not an integer or float

    """
    #check if a is an integer or float 
    if not  isinstance(a , (int, float)):
        raise TypeError("a must be an integer")
    
    #check if b is an intger or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    #Cast a aand b to integers 
    a = int(a)
    b = int(b)

    #return the sum of a and b  
    return a + b