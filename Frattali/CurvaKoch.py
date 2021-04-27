import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Data for plotting
fig, ax = plt.subplots()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
plt.gca().set_aspect('equal', adjustable='box')

ax.axis('off')

line, = ax.plot([], [], lw=3)
line.set_linewidth(0.4)

def init():
    line.set_data([], [])
    return line,

ORD = 2
#INIT = [(-0.9, 0), (0, 0.9) ,(0.9, 0), (0, -0.9),(-0.9, 0) ]
INIT = [(-1, 0), (1, 0)]
#INIT = [(-0.6, -0.3), (0, 1), (0.6, -0.3),(-0.6, -0.3) ]
STRUCT = [(-0.2, 0), (0, 0.3), (0.2, 0)]

points = INIT

def Koch_1(points):
    new = []
    for i in range(0, len(points) -1):
        foot = points[i]
        head = points[i + 1]
        
        #base vector
        v = (head[0] - foot[0], head[1] - foot[1])
        ort_v = (-v[1], v[0])
        offsetx = (foot[0] + head[0])/2
        offsety = (foot[1] + head[1])/2

        new.append(foot)    
        #structure rotation, riscalation and translation
        for j in range(0, len(STRUCT)):
            tempx = v[0] * STRUCT[j][0] + ort_v[0] * STRUCT[j][1] + offsetx
            tempy = v[1] * STRUCT[j][0] + ort_v[1] * STRUCT[j][1] + offsety
            new.append((tempx, tempy))

    new.append(points[-1])
    return new

i = 0
while i < ORD:
    points = Koch_1(points)
    i += 1
x = []
y = []
for i in range(0, len(points)):
    x.append(points[i][0])
    y.append(points[i][1])

def animate(i):
    points = Koch_1(points)
    x = []
    y = []
    for i in range(0, len(points)):
        x.append(points[i][0])
        y.append(points[i][1])
        line.set_data(x, y)
    return line,

#anim = FuncAnimation(fig, animate, init_func=init,frames=ORD, interval=1, blit=True)
#anim.save('Hilbert_curve1.gif', writer='imagemagick', dpi=200)


ax.plot(x, y)
plt.show()