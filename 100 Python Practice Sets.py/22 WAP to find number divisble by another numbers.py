# Solution 1 by using for loop
print("The number divisble by 13 is")
for i in range(1,100):
    if i %13==0:
        print(i)

# Solution 2 by using lambda(anoymanous function)
l=[39,48,26,98,33,67,87]
result=list(filter(lambda x:x%13==0,l))
print(result)
