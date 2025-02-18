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

# Write a function is_even(n) that takes a number n and returns True if the number is even and False if it is odd.

# my thought process
def is_even (m):
    num = m
    if m == True:
        print('True')
    else:
        print('False')

print(is_even(5))

# option 2

def is_evens (mm):
    return mm % 2 == 0

print(is_evens(4))
print(is_evens(9))

# Write a function is_prime(n) that takes a number n and returns True if n is a prime number, and False otherwise.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(19))
print(is_prime(2))
print(is_prime(99))

#  Write a function fibonacci(n) that takes a number n and returns the n`th Fibonacci number. The Fibonacci sequence starts with `0, 1, 1, 2, 3, 5, 8, ....

def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(fibonacci(0))
print(fibonacci(3))
print(fibonacci(5))
print(fibonacci(7))

# Write a function count_char(string, char) that takes a string and a character and returns the number of occurrences of that character in the string.

def count_char(string, char):
    return string.count(char)


print(count_char("michael", "l"))
print(count_char("banana", "a"))
print(count_char("ovie", "v"))



# Write a function find_max(lst) that takes a list of numbers as input and returns the largest number in the list.

def find_max(lst):
    if not lst:
        raise ValueError("The list cannot be empty")
    return max(lst)


print(find_max([1, 5, 3, 9, 2]))
print(find_max([-10, -5, -1, -20]))
print(find_max([100]))


#  Write a function reverse_string(string) that takes a string as input and returns the string reversed.

def reverse_string(string):
    return string[::-1]


print(reverse_string("hello"))
print(reverse_string("Python"))
print(reverse_string(""))


#  Write a function calculate_average(lst) that takes a list of numbers and returns the average of those numbers.

def calculate_average(lst):
    if not lst:
        raise ValueError("The list cannot be empty")
    return sum(lst) / len(lst)


print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([10, 20, 30]))
print(calculate_average([100]))