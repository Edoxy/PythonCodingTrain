import turtle
import colorsys


wn = turtle.Screen()
wn.bgcolor(0, 0, 0)
wn.title("Finestra")
wn.setup(width=1400, height=1200)
wn.tracer(0)

point = turtle.Turtle()
point.shape("circle")
point.shapesize(0.2, 0.2)

x = -0
y = -3
z = -0
point.goto(z *20 -400, y *20)

a = 12
b = 27
c =8.0/4.0
hue = 0

#Main Loop
while True:
    wn.update()
    dt = 0.0005
    dx = a * (y - x) * dt
    dy = (x * (b - z) - y) * dt
    dz = (x * y - c * z) * dt

    x += dx
    y += dy
    z += dz

    hue += 0.5 /80000
    if hue == 1:
        hue = 0
    
    color = colorsys.hsv_to_rgb(hue, 0.8, 1)

    point.color(color)
    point.setx(z * 20 -400)
    point.sety(y * 20)

#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#.venv\scripts\activate