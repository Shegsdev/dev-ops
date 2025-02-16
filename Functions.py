#pythons keywords for functions

def greet (name):
	return f"hello, {name}"

# print(greet("Mr Trump"))

#classwork
#create a function that calculates the area of a rectangle given the L & B
def calculate (Length,Breath):
	Area = Length*Breath 
	return Area

# print(calculate(20,10))

#calculate square
def square (n):
	return n*n 

# print (square(4))
# print (square(5))
# print (square(6))


#Error Handling

try:
	x = 10/0
	
except ZeroDivisionError as e:
	pass
	# print ("error: cannot divide by Zero")

	
finally:
	pass
	# print ("this will always run")


#Create a function
def open_file ():
	try:
		with open("file.txt","r") as f:
			content = f.read()
			print (content)

	except FileNotFoundError as e:
		print ("file not found")

	finally:
		print ("this program must not crash")


# open_file()


def write_to_file():
	with open ("file.txt","w+") as f:
		f.write("hello,devops engineer")

#write_to_file()

#assignment: read up on file handling


#Recap on functions #for loop sample
def calculate_sum(n):
	total = 0
	for i in range (n+1):
		total = total+i

	return total


print(calculate_sum(50))
print(calculate_sum(10))
print(calculate_sum(20))

#While loop sample
def calculate_sum(n):
	total = 0
	counter = 1
	while (counter <=n):
		total =total+counter
		counter=counter+1

	return total



#RECURSION: This is a fuction that calls itself
def calculate_sum(n):
 	if n==1:
 		return 1

 	return n + calculate_sum (n-1)

print(calculate_sum(50))
print(calculate_sum(10))
print(calculate_sum(20))


