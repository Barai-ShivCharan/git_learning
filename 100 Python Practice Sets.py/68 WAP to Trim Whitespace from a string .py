# Solution 1 Using strip() function
'''string =" I Love Python"
print(string)
print(string.strip())'''

# Solution 2 Using Regular Expression
import re
string="I       Love   Python"
s1=re.sub(r'^\s+|\s$', '', string)
print(s1)
