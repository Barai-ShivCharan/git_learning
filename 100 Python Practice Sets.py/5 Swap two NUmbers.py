# Solution 1(By using third variable i.e temp)
'''x=13
y=12

temp=x
print("The value of temps is:",temp)

x=y
print("The value of x is:",x)

y=temp
print("THe value of y is:",y)
'''

# Solution 1(without using third variables)
x=12
y=13

x,y=y,x
print("The value of x is : ",x)
print("The value of y is : ",y)