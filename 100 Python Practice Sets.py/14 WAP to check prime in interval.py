lower=int(input("Enter lower limit here: "))
upper=int(input("Enter upper limit here: "))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
            else:
                print(num)

# num1=23
# num2=50
# for i in range(num1,num2):
#     if num1%i and num2%i==0:
#         print("it is not a prime number")
#     else:
#         print("it is prime number")














    
    