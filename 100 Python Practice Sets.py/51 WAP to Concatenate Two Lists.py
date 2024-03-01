# Solution 1 Using  + Operators
# l1=[3,4,5,6,2,3,7,"a","j"]
# l2=[3,5,"f","y"]
# print(l1+l2)


# Sollutio 2  using uniques values

# l1=[3,4,5,6,2,3,7,"a","j"]
# l2=[3,5,"f","y"]
# l12=set(l1+l2)
# l12=list(set(l1+l2))
# print(l12)

# Solution 3 Using extend() function
l1=[3,4,5,6,2,3,7,"a","j"]
l2=[3,5,"f","y"]
l1.extend(l2)
print(l1)