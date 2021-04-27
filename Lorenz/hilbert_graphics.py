from graphics import *
import colorsys
import time
len = 1400
wn = GraphWin("Hilbert", len, len)

ord = 9
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
pos = [[], [], [], []]
for i in range(0, int(total/4)):
    x = Hilber(i)
    j = i + int(total/4)
    y = Hilber(j)

    off = + int(len/2)

    pos[0].append(Point(x[0] + off, -x[1] + off))
    pos[3].insert(0, Point(-x[0] + off, -x[1] + off))
    pos[1].append(Point(y[0] + off, -y[1] + off))
    pos[2].insert(0, Point(-y[0] + off, -y[1] + off))
#Main Loop
for v1 in range(0, 0):
    for v2 in range(0, 0*int(total/4)):
        #print(v1, v2)
        #point.setposition(pos[v1][v2])
        #wn.update()
        #pt = Point(pos[v1][v2][0] + int(len/2), -pos[v1][v2][1] + int(len/2))
        #pt.draw(wn)

        hue += 1/total
        if hue == 1:
            hue = 0
        color = colorsys.hsv_to_rgb(hue, 0.8, 1)

        #point.color(color)
        
    pt = Polygon(pos[v1])
    pt.setOutline('black')
    pt.setWidth(1)
    pt.draw(wn)


    if v1 == 3:
        wn.getMouse()
        wn.close()
        time.sleep(4)
        #point.shape("circle")
        #point.shapesize(0.2, 0.2)

pt = Polygon(pos[0] +pos[1] +pos[2] +pos[3])
pt.setOutline('black')
pt.setWidth(1)
pt.draw(wn)
wn.getMouse()
wn.close()