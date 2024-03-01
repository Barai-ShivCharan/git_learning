import time
'''starting_time=time.time()

num1=int(input("Enter the number 1"))
num2=int(input("Enter the number2 "))
print(num1+num2)

ending_time=time.time()
print(ending_time -starting-time)
print(starting_time)
print(ending_time)'''

# Solution 2 Using Timeit Module
from timeit import default_timer as timer
starting_value=timer()
print(78+9)
ending_time=timer()
print(starting_value)
print(ending_time)
