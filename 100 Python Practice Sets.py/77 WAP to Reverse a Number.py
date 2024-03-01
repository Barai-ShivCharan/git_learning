# Solution 1 Using while loop
'''num=int(input("Enter the number here..."))
rever_num=0
while num!=0:
    digit=num%10
    rever_num=rever_num*10+digit
    num=num//10
    print("The revrse of given number is :",rever_num)'''

# Solution 2 Using string slicing
num=int(input("Enter the number:"))
print(str(num)[::-1])