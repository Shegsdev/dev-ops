#Sum of Two Numbers
#Write a function add(a, b) that takes two numbers as parameters and returns their sum

def add(a, b):
	return a + b
result = add(5, 8)

print(result)


#Factorial of a Number
#Write a function factorial(n) that takes a number n as input and returns the factorial of n (n!).

def factorial(n):
   if n == 0:
      return 1

   else:
      return n * factorial(n - 1)

print(factorial(5))


#Even or Odd Check
#Write a function is_even(n) that takes a number n and returns True if the number is even and False if it is odd.

def is_even(n):
   return n %  2 == 0

print(is_even(6))
print(is_even(9))



#Prime Number Check
#Write a function is_prime(n) that takes a number n and returns True if n is a prime number, and False otherwise.


def is_prime(n):
   return n % 2 == 0

print(is_prime(4))
print(is_prime(15))


#Fibonacci Sequence
#Write a function fibonacci(n) that takes a number n and returns the n`th Fibonacci number. The Fibonacci sequence starts with `0, 1, 1, 2, 3, 5, 8, ....


def fibonacci(n):
   if n == 0:
      return 0

   elif n == 1:
      return 1

   return fibonacci(n - 1) + fibonacci(n - 2) #not sure about how this came about though

print(fibonacci(6))


#Count Occurrences of a Character in a String
#Write a function count_char(string, char) that takes a string and a character and returns the number of occurrences of that character in the string.


def count_character(string, char):
   return string.count(char)

print(count_character('Papaya', 'a'))
print(count_character('AirportTaxi', 'i'))



#Find the Largest Number in a List
#Write a function find_max(lst) that takes a list of numbers as input and returns the largest number in the list.


def find_max(lst):
   return max(lst)

print(find_max([12,15,20,90,604]))



#Reverse a String
#Write a function reverse_string(string) that takes a string as input and returns the string reversed.

def reverse_string(string):
   return string[::-1]

print(reverse_string([2,5,7,9,]))



#Calculate the Average of a List of Numbers
#Write a function calculate_average(lst) that takes a list of numbers and returns the average of those numbers.


def calculate_average(lst):
   if not lst:
      return none
   return sum (lst) / len (lst)
   
print(calculate_average([2,4,5,7,8]))