'''f=open("file57.text","r")
lines=f.readlines()
print(lines)
new_lines=[x.strip() for x in lines]
print(new_lines)'''

# Solution 2 Usinf for loop and List Comprehension
'''f=open("file57.text","r")
line=[line for line in f]
print(line)

new_lines=[x.strip() for x in line]
print(new_lines)'''
