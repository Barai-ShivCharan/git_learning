# Solution 1 Using Tuples Unpacking
'''ef friends():
    return "shiva","barai","bhaijan"

print(friends())
n1,n2,n3=friends()
print(n1,",",n2,"and",n3)'''

def friends():
    n1="shyam"
    n2="Lilesh Tiwri"
    return {1:n1,2:n2}
names=friends()
print(names)
print(names[1],",",names[2])

