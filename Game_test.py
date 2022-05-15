from secrets import choice
import turtle       # to create shape with canvas
import random     
import time

screen = turtle.Screen()    # defining screen 
screen.bgcolor("black")     # screen color to black
screen.title("Fysik spel")  # title of screen
screen.tracer(0)            # turn off tracer
counter = 0
wind_dir = [-1, 1]

balls_shape = "circle"
balls_colors = ["white", "orange", "green", "blue", "red"]
balls = []          # array with all balls

# creating as many balls as we need 
for i in range(10):                  # creating 5 balls
    balls.append(turtle.Turtle())   # appending them to the array

# appending fetures to each ball
for b in balls:
    b.shape(balls_shape)                    # all balls get the same shape
    b.color(random.choice(balls_colors))    # balls get different colors
    b.penup()                               # to not leave tracks
    b.speed(0)                              # speed for showing movement
    x = random.randint(-290, 290)           # random start position x
    y = random.randint(200, 400)            # random start position y
    b.goto(x, y)                            # moving ball to that position
    b.dy = 0                                # initial velocity y
    b.dx = random.randint(-1, 1)            # initial velocity x
    b.da = 3

gravity = 0.001
air_res = 0.9

# run
while True:
    screen.update()

    counter += 1 
    
    for b in balls:
        b.rt(b.da)                  # balls rotation
        b.dy -= gravity             # gravity in y-axis
        b.sety(b.ycor() + b.dy)     # changing y cord
        b.setx(b.xcor() + b.dx)     # changing x cord

        # kollision med väggar
        if b.xcor() > 300 or b.xcor() < -300:
            b.dx *= -1
            b.da *= -1

        if b.ycor() < -300:
            b.sety(-300)
            b.dy *= -0.9
            b.da *= -1

        if counter % 500 == 0:
            b.dx *= air_res
            b.dy *= air_res

    if counter >= 5000:   # 5000ms = 5s
        for b in balls:
            b.dx += 0.3 * random.choice(wind_dir)
            b.dy += 0.5 * random.choice(wind_dir)
            counter = 0
        print("wind time")

    # Collisions between balls
    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i].distance(balls[j]) < 20:
                #prev_dx, prev_dy = balls[i].dx, balls[i].dy
                balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy
                #balls[j].dx, balls[j],dy = prev_dx, prev_dys