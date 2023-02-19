import random


def get_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'
from tkinter import *
root = Tk()
c = Canvas(width=640,height=480)
y=0
for line in range(480):
    y+=1
    x=0
    for pixel in range(640):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb = r,g,b
        c.create_oval(x,y,x+10,y+10,fill=get_rgb(rgb))
        x+=1
c.pack()
root.mainloop()