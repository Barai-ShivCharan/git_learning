# solution 1 using for loop
'''A=[[2,34,5],
    [35,6,8]]

T=[[0,0],
    [0,0],
    [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i]=A[i][j]
for i in T:
    print(i)'''

# Solution 2 Using list compression
A=[[2,34,5],
    [35,6,8]]
T=[[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
# print(T)
for i in T:
    print(i)

