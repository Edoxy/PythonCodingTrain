import turtle
#from Tkinter import *
import colorsys
import numpy as np
import time
from PIL import Image

im = Image.open("yoda.jpeg")
col, row = im.size
data = np.zeros((row*col, 5))
pixels = im.load()
print(pixels)

len = min(row, col)
RESOLUTION = 1000
fact = RESOLUTION/len

wn = turtle.Screen()
wn.title("Finestra")
wn.setup(width=len * fact, height=len * fact)
wn.bgcolor(0, 0, 0)
wn.tracer(0)

ord = 9
n = 2 ** ord
total = n * n
print(total)

def Hilber(i):
    pos = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
    # offset quadrante
    # punto
    dim = len / (2 * 2**ord)
    x = pos[i % 4][0] * dim
    y = pos[i % 4][1] * dim

    for j in range(1, ord):
        index = int(i / (4**j)) % 4

        m = len / (2 * (2 ** (ord - j)))
        # print("for i = ", i, "\n j =", j, "\nindex =", index, "\nm = ", m, "\n")

        if index == 0:
            temp = y
            y = -x
            x = -temp

            x -= m
            y += m
        elif index == 1:
            x -= m
            y -= m
        elif index == 2:
            x += m
            y -= m
        elif index == 3:
            temp = y
            y = x
            x = temp

            x += m
            y += m

    return (x, y)





i = 0
v1 = []
v2 = []
v3 = []
v4 = []

offsetx = int(len/2)
# Main Loop
while i != total/4:
    pos = Hilber(i)
    j = int(i + total/4)
    pos2 = Hilber(j)
    # print(pixels[pos[0], pos[1]])

    i += 1
    v1.append(pixels[(pos[0] - offsetx), (offsetx-pos[1])])
    v4.insert(0, pixels[(-pos[0] - offsetx), (offsetx-pos[1])])
    v2.append(pixels[(pos2[0] - offsetx), (offsetx-pos2[1])])
    v3.insert(0, pixels[(-pos2[0] - offsetx), (offsetx-pos2[1])])


p1 = turtle.Turtle()
p1.penup()
p1.color("white")
p1.shapesize(1, 1)
p1.pensize(2)

hue = 0

pos = [[], [], [], []]
for i in range(0, int(total/4)):
    x = Hilber(i)
    j = i + int(total/4)
    y = Hilber(j)

    pos[0].append(x)
    pos[3].insert(0, (-x[0], x[1]))
    pos[1].append(y)
    pos[2].insert(0, (-y[0], y[1]))

pos_ = pos[0] + pos[1] + pos[2] + pos[3]
value = v1 + v2 + v3 + v4

i = 0
while True:
    p1.setposition((pos_[i][0] * fact, pos_[i][1] * fact))
    p1.pendown()
    wn.update()

    hue += 1/total
    if hue == 1:
        hue = 0

    i += 1
    if i == total:
        i = 0
        time.sleep(3)
        ts = turtle.getscreen()
        ts.getcanvas().postscript(file = "ris.eps")
        wn.clear()
        wn.bgcolor(0, 0, 0)
        wn.tracer(0)
        p1.shape("circle")
        p1.shapesize(0.2, 0.2)

    # color = colorsys.hsv_to_rgb(value[i])
    p1.color(value[i][0] / 360, value[i][1] / 360, value[i][2]/360)


# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# .venv\scripts\activate
