"""Modules & Libraries are used to
organise our codes 
promote reusability
provide built-in functions

Libraries are a collections of modules that serve a specific purpose.
Module is a single python file
- we can use modules to import a new file
"""
#all import should be at the top of the file

import math
import random
import datetime
import os
import sys
from my_module import add


print (math.sqrt(25))
print (math.pi)

print(random.choice([2,3,5]))
print(random.randint(1,10))

now=datetime.datetime.now()
print (now)
tomorrow=now+datetime.timedelta(days=1)
print (tomorrow.strftime("%Y-%m-%d"))

print (os.name)
print(os.getcwd())
print(os.listdir("."))

print(sys.version)

#print(my_module.add(2,3))

print(add(2,3))
