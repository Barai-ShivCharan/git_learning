'''# Solution by  using Dictionary
a="Harry potter and the prisoner of Azkaban"
vowels="aeiou"
a=a.casefold()
print(a)

count={}.fromkeys(vowels,0)
for char in a:
    if char in count:
        count[char] +=1
print(count)'''

# Solution using list abd Dictionary
a="Harry Potter and the prisoner of Azkabhan"
vowels=a.casefold()
print(vowels)
count={key:sum([1 for char in a if char==key]) for key in vowels}
print(count)

