num1=float(input("Enter the first number here: "))
num2=float(input("Enter the Second number here: "))

print("Press 1 for Addition \nPress 2 for Sunstraction \nPress 3 for Multiplication\nPress 4 for division")
while True:
    choice=int(input("Enter the choice from 1 to 4: "))
    if choice==1:
        print("The addition of two number is",num1+num2)
    elif choice==2:
        print("The Substraction of two number is",num1-num2)
    elif choice==3:
        print("The Multiplication of two number is",num1*num2)
    elif choice==4:
        print("The Division of two number is",num1/num2)
    else:
        print("Invalid input")
