# Module and libaries

# organise codes
# promote reusability
# provide built -in function

# a libaries - a collection of modules that serve a specfic pupose
# module - a single python file

# import math

# print(math.sqrt(25))
# print(math.pi)

# import random

# print(random.choice([2, 3, 4, 5]))
# print(random.randint(1, 10))

# import datetime

# now = datetime.datetime.now()

# print(now)

# tommorrow = now + datetime.timedelta(days=1)

# print(tommorrow.strftime("%d-%m-%Y"))

# import os

# print(os.name)
# print(os.getcwd())
# print(os.listdir("."))


# import sys


# print(sys.version)

# import my_module
# from my_module import add


# print(my_module.add(2, 3))
# print(add(2, 3))


# assignment
# write a pthyon script that will ping a list of servers 
# retrieves server uptime

#write up subprocess

# Classwork execerse 1

# 1. Sum of Two Numbers
#    Write a function add(a, b) that takes two numbers as parameters and returns their sum.

def total_sum (a, b):
    sum = (a + b)
    return sum


print(total_sum(55 , 93))

# 2. Factorial of a Number
#    Write a function factorial(n) that takes a number n as input and returns the factorial of n (n!).

def factorial_n (n):
    factorial = 1
    for i in range(1,  n + 1):
        factorial *=i
    return factorial


print(factorial_n(5))