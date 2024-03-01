# Solution 1 (using for loop)
'''num=int(input("Enter the number: "))

fact=1

if num<0:
    print("factorial of 0 doesnot exist")
if num==0:

    print("factorial of 0 is ",1)
if num>0:
    for i in range(1,num+1):
        fact=fact*i
print("the factorial of the given number is",fact)
'''

# Solution 2(using recuresion)
def  fact(a):
    if a==0:
        return 1
    else:
        return (a*fact(a-1))
num=int(input("Enter the number"))
result=fact(num)
print("The factorial of the given number is: ",result)
