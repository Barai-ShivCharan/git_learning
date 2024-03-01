num1=int(input("Enter the number num1: "))
num2=int(input("Enter the number num2: "))
num3=int(input("Enter the number num3: "))

if (num1>num2 and num1>num3):
    print(num1,'Num1 is greater')
elif (num2>num1 and num2>num3):
    print(num2,'num2 is greater')
else:
    print(num3,"Num3 is grater")
