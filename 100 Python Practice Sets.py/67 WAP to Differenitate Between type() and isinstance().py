class SmartPhone:
    def name(self):
        pass
class Nokia(SmartPhone):
    def Phone_name():
        pass
obj1=SmartPhone()
obj2=Nokia()

print(type(obj1)==SmartPhone)
print(type(obj2)==SmartPhone)
print()
print(isinstance(obj1, SmartPhone))
# print(isinstance(obj2, Nokia))
print(isinstance(obj2, SmartPhone)) # here is the difference of type() and instance()
