import turtle
import random

turtle.tracer(False)

file = open("color.txt")

colorlist = []
for line in file:
    colorlist.append(line.strip())

turtle.setup(400, 400)
turtle.screensize(400, 400)

sizeofgrid = int(input("Grid size (n): \n")) # Best to see grid <= 5
size = 400 // sizeofgrid

turtle.pensize(0.5)
turtle.speed(1000)
turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.pencolor("black")

def draw_grid(oldpositionx, oldpositiony, size):
    turtle.penup()
    turtle.goto(oldpositionx, oldpositiony)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def draw_pic1(oldpositionx, oldpositiony, size):
    turtle.begin_fill()
    turtle.goto(oldpositionx + 0.5 * size, oldpositiony - 0.4 * size)
    turtle.goto(oldpositionx + 0.4 * size, oldpositiony - 0.7 * size)
    turtle.goto(oldpositionx, oldpositiony - 0.9 * size)
    turtle.goto(oldpositionx, oldpositiony)
    turtle.end_fill()

def draw_pic2(oldpositionx, oldpositiony, size):
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(oldpositionx, oldpositiony - 0.9 * size)
    turtle.pendown()
    turtle.goto(oldpositionx + 0.4 * size, oldpositiony - 0.7 * size)
    turtle.goto(oldpositionx + size, oldpositiony - 0.2 * size)
    turtle.goto(oldpositionx + size, oldpositiony - size)
    turtle.goto(oldpositionx + 0.65 * size, oldpositiony - 0.85 * size)
    turtle.goto(oldpositionx, oldpositiony - 0.9 * size)
    turtle.end_fill()

def draw_pic3(oldpositionx, oldpositiony, size):
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(oldpositionx, oldpositiony - 0.9 * size)
    turtle.pendown()
    turtle.goto(oldpositionx + 0.65 * size, oldpositiony - 0.85 * size)
    turtle.goto(oldpositionx + size, oldpositiony - size)
    turtle.goto(oldpositionx, oldpositiony - size)
    turtle.goto(oldpositionx, oldpositiony - 0.9 * size)
    turtle.end_fill()

def draw_kunai1(oldpositionx, oldpositiony, size):
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(oldpositionx + size / 2, oldpositiony - size / 2)
    for i in range(4):
        turtle.forward(size / 4)
        turtle.left(45)
        turtle.forward(size / 4)
        turtle.left(180 - 45)
        turtle.forward(size / 4)
        turtle.left(45)
        turtle.forward(size / 4)
        turtle.left(180 - 45)
        turtle.left(90)
    turtle.end_fill()

def draw_iphone15prm(oldpositionx, oldpositiony, size):
    turtle.begin_fill()
    width = size / 4
    height = size / 2
    corner = 15
    turtle.penup()
    turtle.goto(oldpositionx +  size / 2, oldpositiony  - size / 2 )
    turtle.pendown()
    for i in range(4):
        for i in range(2):
            turtle.circle(corner, 90)
            turtle.forward(height - 2 * corner)
            turtle.circle(corner, 90)
            turtle.forward(width - 2 * corner)
        turtle.right(90)
    turtle.penup()
    turtle.end_fill()

for i1 in range(sizeofgrid):
    for i2 in range(sizeofgrid):
        oldpositionx = -200 + i2 * size
        oldpositiony = 200 - i1 * size
        cell_size = random.randint(size // 2, size) # this must be from size / 2 because the function kunai and 15prm take the side equal to size/2 is maximum size
        decide = random.randint(1, 4)
        
        turtle.fillcolor(random.choice(colorlist))
        draw_grid(oldpositionx, oldpositiony, cell_size)
        if decide == 1:
            turtle.fillcolor(random.choice(colorlist))
            draw_pic1(oldpositionx, oldpositiony, cell_size)

            turtle.fillcolor(random.choice(colorlist))
            draw_pic2(oldpositionx, oldpositiony, cell_size)

            turtle.fillcolor(random.choice(colorlist))
            draw_pic3(oldpositionx, oldpositiony, cell_size)
        elif decide == 2:
            turtle.fillcolor(random.choice(colorlist))
            draw_kunai1(oldpositionx, oldpositiony, cell_size)
        elif decide == 3:
            turtle.fillcolor(random.choice(colorlist))
            draw_iphone15prm(oldpositionx, oldpositiony, cell_size)
        else:
            turtle.fillcolor(random.choice(colorlist))
            draw_kunai1(oldpositionx, oldpositiony, cell_size)

            turtle.fillcolor(random.choice(colorlist))
            draw_iphone15prm(oldpositionx, oldpositiony, cell_size)

turtle.tracer(True)
turtle.mainloop()