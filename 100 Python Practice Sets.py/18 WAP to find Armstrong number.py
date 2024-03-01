num=int(input("Enter the number here: "))
# order=len(str(num))# for more then 3 digits
sum=0
temp=num
while temp >0:
    digit=temp%10
    cube=digit**3# in instead of 3 used (order)
    sum= sum+cube
    temp //=10
if sum ==num:
    print("it is an armstrong number")
else:
    print("it is not armstrong number")
# num=int(input("Enter the number here:"))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     cube=digit**3
#     sum=sum+cube
#     temp //=10
# if sum==num:
#     print("it is  a armstrong number")
# else:
#     print("it is not a armstrong number")