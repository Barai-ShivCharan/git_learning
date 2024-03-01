# Solution 1 Using Zip() and Dictionary methods
'''name=["Shiva","shyam","Radhe"]
marks=[45,67,43,23]
dictionary=zip(name,marks)
# print(tuple(dictionary))
print(dict(dictionary))'''

# Solution 2 using zip() and list comprehension
name=["Shiva","shyam","Radhe"]
marks=[45,67,43,23]
dictionary={key:value for key ,value in zip(name,marks)}
print(dictionary)