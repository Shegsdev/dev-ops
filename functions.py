# Lesson 3: Functions

# function are a re-usable blocks of code that performances a specfic task. 

# python keyword for Functions

# def greet(name):
#     return f"Hello, {name}"

# # print (greet("Michael"))

# # Class work 1
# def calcute_area(length , breadth):
#     area = (length * breadth)
#     return area

# # print (calcute_area(20 , 10))

# # Class work 2
# def calculate_square(root):
#     square = (root * root)
#     return square

# # print (calculate_square(4))
# # print (calculate_square(5))
# # print (calculate_square(6))

# # Error handling keyword
# #  try
# #  except
# #  finally

# # x = 10 / 0
# try:
#     x = 10 / 0
# except ZeroDivisionError as e:
#     print("error: Can't divide by zero")
# finally:
#     # print("This will always run")


# # def open_file():
# #     try:
# #         with open("file.txt" , "r") as f:
# #             content = f.read()
# #             # print(content)
# #     except FileNotFoundError as e:
# #         print("error: File not found")
# #     finally:
# #         # print("This will always run")

# # open_file()

# # def write_to_file():
# #     with open("file.txt" , "w+") as f:
# #         f.write("Hello , DevOps Engineer")

# # write_to_file()

# #  concatenation - joining strings "Hello" + "world"
# # interpolation - joining different data types we use f "Hello, {name}"


# # class work 3

# # def calculate_sum(n):
# #     total_sum = 0
# #     for sum in range(n + 1):
# #         total_sum = total_sum + sum
# #     return total_sum

# # print(calculate_sum(50))
# # print(calculate_sum(20))
# # print(calculate_sum(10))

# # def calculate_sum (n):
# #     total_sum = 0
# #     counter = 1
# #     while(counter<=n):
# #         total_sum = total_sum + counter
# #         counter = counter + 1
# #     return total_sum

# # print(calculate_sum(50))
# # print(calculate_sum(20))
# # print(calculate_sum(10))

# # Recursion - a function that calls itself

# def calculate_sum (n):
#     if n == 1:
#         return 1
#     return n + calculate_sum(n-1)

# print(calculate_sum(50))
# print(calculate_sum(20))
# print(calculate_sum(10))



