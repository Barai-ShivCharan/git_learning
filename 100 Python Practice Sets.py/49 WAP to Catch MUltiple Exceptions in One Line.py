String=input("Enter Something here...")
try:
    NUmber=int(input("Enter the Number here......."))
    print(String +NUmber)
except(ValueError,TypeError) as a :
    print(a)