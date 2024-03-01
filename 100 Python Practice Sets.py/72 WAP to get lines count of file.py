#Solution 1 Using len() function
'''f=open("demo.txt","r")
print(len(f.readlines()))
f.close()'''

# Solution 2 Using list Comprehension  method
lines=sum(1 for i in open("demo.txt"))
print(lines)
