# Solution 1 using os Module
'''import os
file_size=os.stat("C:/Users/DELL/Pictures/shivcharan.jpg")
print(file_size)# size is in bytes'''

# Solution 2 Using Module
from pathlib import path
file_size=path("C:/Users/DELL/Pictures/shivcharan.jpg")
print(file_size.stat().st_size)


