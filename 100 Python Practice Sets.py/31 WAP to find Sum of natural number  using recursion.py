def NNS(n):
    if n<=1:
        return n
    else:
            return (n)+NNS(n-1)
    n=int(input("Enter the number: "))
    if n<=0:
        print(":Enter the positive number:")
    else:
        print("The sum of natural numbers upto given number is",NNS(n))
    