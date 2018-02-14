"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    """
    This function returns a string value
    """
    x='Viraj' 
    return x

def give_me_an_integer():
    """
    This function returns an integer value
    """
    a=7
    return a
    

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    b= (7<10)
    return b
    

def give_me_a_float():
    """
    This function returns a float value
    """
    f=3.14
    return f
    

def give_me_a_list():
    """
    This function returns a list
    """
    l=['CR7', 'SR4', 'TK8', 'KN1', 'GB11']
    return l
    

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    spanish = dict()
    spanish['hello'] = 'hola'
    spanish['yes'] = 'si'
    spanish['one'] = 'uno'
    spanish['two'] = 'dos'
    spanish['three'] = 'tres'
    spanish['red'] = 'rojo'
    spanish['black'] = 'negro'
    spanish['green'] = 'verde'
    spanish['blue'] = 'azul'
    return spanish
    

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    t=('A','B','C')
    return t
    

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    a = 0
    for i in range(1,11):
   		a=i+a
    return a
   

def check_is_even(number):
    """
    This function returns True if num is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    if number%2==0:
    	return True
    else :
    	return False

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    if number1 < number2 :
    	return True
    else :
    	return False
    	
def plus(a,b):
	"""
	this function adds th two number
	"""
	return a+b

def  hello():
	"""
	this returns the string
	"""
	return ('hello')
    
