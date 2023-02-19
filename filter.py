import random
import time


def get_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'
from tkinter import *
root = Tk()
c = Canvas(width=640,height=480)
inp = open("output.txt")
lines = inp.read().split("\n")
y=0

for line in lines:
    y+=1
    pixels = line.split("|")
    pixels.pop(-1)
    x=0
    for pixel in pixels:
        p = pixel.split(" ")
        r = int(p[0])
        g = int(p[1])
        b = 100
        try:
            rgb = r-50,g-50,b
            c.create_line(x,y,x+5,y+10,fill=get_rgb(rgb))
        except:
            rgb = r,g,b
            c.create_line(x,y,x+5,y+10,fill=get_rgb(rgb))
        x+=1
c.pack()
root.mainloop()
