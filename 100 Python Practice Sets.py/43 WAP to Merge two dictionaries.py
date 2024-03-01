# Using Bar(|) Operators
'''
dict1={"jhon:45","Lisha:78"}
dict2={"Lisha:89","Ghanshyam:89"}
print(dict1 | dict2)'''

#Solution 2 chorks(**) Operators
dict1={"jhon:45","Lisha:78"}
dict2={"Lisha:89","Ghanshyam:89"}
print( ({**dict1,**dict2}))

# Solutions 3 Using copy() and Upadate( )Methods

# dict1={"jhon:45","Lisha:78"}
# dict2={"Lisha:89","Ghanshyam:89"}
# dict1=dict2.copy()
# dict1.update(dict1)
# print(dict1)

