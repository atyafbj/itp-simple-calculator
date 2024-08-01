import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Invalid value for denominator, can't divide by 0!" if b == 0 else a / b

def square(a):
    return a ** 2

def power(a, b):
    return a ** b

def sqrt(a):
    return "Cannot take the square root of a negative number!" if a < 0 else math.sqrt(a)
