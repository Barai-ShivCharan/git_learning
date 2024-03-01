def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter  a number here" ))
if n<=0:
    print("Enter the a positve number")
else:
    print("Fibonacci esquence")
    for i in range(n):
        print(fibo(i))