def convertBinary(n):
    if n>1:
        convertBinary(n//2)
    print(n%2,end='')
print("THe biaray of the given number is: ")

convertBinary(15)