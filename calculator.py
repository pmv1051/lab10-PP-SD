# https://github.com/pmv1051/lab10-PP-SD
# Partner 1: Prem Patel
# Partner 2: Samuel Deegan


"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b): 
    return a+b

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def subtract(a, b):
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    if a == 0:
        raise ZeroDivisionError
    return b / a # raise ZeroDivisionError if a == 0

def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be greater than 0 and not equal to 1.")
    if b <= 0:
        raise ValueError("Logarithm argument must be greater than 0.")

    return math.log(b, a)

def exp(a, b):
    return a**b

