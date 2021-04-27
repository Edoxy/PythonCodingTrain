import turtle
import colorsys
import numpy as np
import time
len = 800
wn = turtle.Screen()
wn.title("Finestra")
wn.setup(width=len, height=len)
wn.bgcolor(0, 0, 0)
wn.tracer(0)

point = turtle.Turtle()
point.shape("circle")
point.shapesize(0.2, 0.2)

ord = 8
n = 2 ** ord
total = n * n
print(total)

def Hilber(i):
    pos = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
    #offset quadrante
    #punto
    dim = len / (2 * 2**ord)
    x = pos[i%4][0] * dim
    y = pos[i%4][1] * dim


    for j in range(1, ord):
        index = int(i / (4**j)) % 4

        m = len /(2 * (2 ** (ord - j)))
        #print("for i = ", i, "\n j =", j, "\nindex =", index, "\nm = ", m, "\n")

        if index==0:
            temp = y
            y = -x
            x = -temp

            x -= m
            y += m
        elif index == 1 :
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

hue = 0

i = 0
#Main Loop
while True:
    pos = Hilber(i)
    point.setposition(pos)
    wn.update()

    hue += 3/(total)
    if hue == 1:
        hue = 0
    if i == total:
        time.sleep(4)
        i = 0
        wn.clearscreen()
        wn.bgcolor(0, 0, 0)
        time.sleep(1)
        wn.tracer(0)
        point.shape("circle")
        point.shapesize(0.2, 0.2)

    i +=1
    
    color = colorsys.hsv_to_rgb(hue, 0.8, 1)

    point.color(color)
