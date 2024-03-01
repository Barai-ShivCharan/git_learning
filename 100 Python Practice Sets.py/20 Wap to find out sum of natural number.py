# num=int(input("Enter the number here: "))

# if num<0:
#     print("Please, Enter the positive number: ")
# else:
#     sum=0
#     while num>0:
#         sum +=num
#         num -=1
#     print(sum)

num=int(input("Enter the number here: "))
if num<0:
    print("Please,Enter the Positive Number")
else:
    sum=0
while num>0:
    sum=num+1
    num -=1 
    print(sum) 