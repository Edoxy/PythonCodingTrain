import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

len = 600

ord = 8
n = 2 ** ord
total = n * n


fig = plt.figure(facecolor='black')
ax = plt.axes(xlim=(-len/2, len/2), ylim=(-len/2, len/2))
#produce un grafico con la stessa scala
plt.gca().set_aspect('equal', adjustable='box')
#cancella gli assi
ax.axis('off')

line, = ax.plot([], [], lw=3)
line.set_linewidth(0.4)
line.set_color('white')

def init():
    line.set_data([], [])
    return line,

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
#Main Loop
posx = posx[0] + posx[1] + posx[2] + posx[3]
posy = posy[0] + posy[1] + posy[2] + posy[3]

x = []
y = []
j = 0
def animate(i):
    for j in range(0, 64):
        x.append(posx[64*i + j])
        y.append(posy[64*i + j])
    line.set_data(x, y)
    return line,

#anim = FuncAnimation(fig, animate, init_func=init,frames=int(total/64), interval=20, blit=True)
#anim.save('Hilbert_curve1.gif', writer='imagemagick', dpi=200)
line.set_data(posx, posy)
fig.savefig('test.jpg', dpi = 900)