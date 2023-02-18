import numpy as np
from PIL import Image
def translate_image(fileout,color):
    file = open(fileout,"w")
    img = Image.open("imgs/ves_j.png")
    mas = np.array(img).tolist()
    for line in mas:
        for pixel in line:
            file.write(str(pixel[color])+" ")
        file.write("\n")
translate_image("output.txt",1)