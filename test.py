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
    pixels = line.split(" ")
    pixels.pop(-1)
    x=0
    for pixel in pixels:
        rgb = 0,0,int(pixel)
        c.create_line(x,y,x+1,y,fill=get_rgb(rgb))
        x+=1
c.pack()
root.mainloop()