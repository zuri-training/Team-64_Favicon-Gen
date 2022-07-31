from PIL import Image 
filename = r'pin.png'
img = Image.open(filename)
img.save("pin2.ico",size=[(32,32)])