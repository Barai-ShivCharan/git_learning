# Solution 1 using __class__.__name__
'''class SmartPhone:
    def name_phone(self,name):
        return name
s1=SmartPhone()
print(s1.__class__.__name__)'''

# Solution 2 using type() and __name__attributes
class SmartPhone:
    def name_1(self,name):
        return name
s2=SmartPhone()
print(type(s2).__name__)