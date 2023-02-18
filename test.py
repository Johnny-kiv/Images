def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb
from tkinter import *
root = Tk()
c = Canvas(width=640,height=480)
inp = open("output.txt")
lines = inp.read().split("\n")
y=0

for line in lines:
    y+=1
    pixels = line.split(" ")
    pixels.pop(-1)
    x=0
    for pixel in pixels:
        c.create_line(x,y,x,y,fill=get_rgb(pixel))
        x+=1
c.pack()
root.mainloop()
