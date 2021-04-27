import matplotlib
import matplotlib.pyplot as plt
import colorsys
import numpy as np
import time
from PIL import Image

im = Image.open("to.jpg")
col, row = im.size
data = np.zeros((row*col, 5))
pixels = im.load()
print(pixels)

len = min(row, col)
RESOLUTION = 1000
fact = RESOLUTION/len

ord = 8
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

hue = 0

posx = [[], [], [], []]
posy = [[], [], [], []]
for i in range(0, int(total/4)):
    x = Hilber(i)
    j = i + int(total/4)
    y = Hilber(j)

    posx[0].append(x[0])
    posx[3].insert(0, -x[0])
    posx[1].append(y[0])
    posx[2].insert(0, -y[0])

    posy[0].append(x[1])
    posy[3].insert(0, x[1])
    posy[1].append(y[1])
    posy[2].insert(0, y[1])

pos_x = posx[0] + posx[1] + posx[2] + posx[3]
pos_y = posy[0] + posy[1] + posy[2] + posy[3]
value = v1 + v2 + v3 + v4

fig, ax = plt.subplots()
ax.plot(pos_x, pos_y)
fig.savefig("test.png")
plt.show()

# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# .venv\scripts\activate