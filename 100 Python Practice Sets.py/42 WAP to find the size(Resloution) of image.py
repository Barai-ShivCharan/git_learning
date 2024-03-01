import PIL
from PIL import image

img=PIL.image.open("C:/Users/DELL/Pictures/shivcharan.shivcharan.jpg")
width,height=img.size
print(width,"x",height)