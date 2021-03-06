from secrets import choice
import turtle       # to create shape with canvas
import random

# friktion är inte implementerat i spelet

screen = turtle.Screen()    # defining screen 
screen.bgcolor("black")     # screen color to black
screen.title("Fysik spel")  # title of screen
screen.tracer(0)            # turn off tracer
counter = 0                 
wind_dir = [-1, 1]

balls_shape = ["circle"]
balls_colors = ["white", "orange", "green", "blue", "red"]
balls = []          # array with all balls
used_x_cords = []
start_x = -290

# creating balls 
for i in range(10):                  # skapar 10 bollar, det är lagom antal bollar för att de ska skapas utan problem
    balls.append(turtle.Turtle())   # appending them to the array

# appending fetures to each ball
for b in balls:
    b.shape(random.choice(balls_shape))     # all balls get the same shape
    b.color(random.choice(balls_colors))    # balls get different colors
    b.penup()                               # to not leave tracks
    b.speed(0)                              # speed for showing movement
    x = start_x         
    while x in used_x_cords and x <= 240:
        x += 40
    used_x_cords.append(x)
    y = random.randint(100, 400)            # random start position y
    b.goto(x, y)                            # moving ball to that position
    b.dy = 0                                # initial velocity y
    b.dx = random.randint(-1, 1)            # initial velocity x
    b.da = 1

# vel_loss är hastighetsförlusten i y-led som framkommer på grund av gravitationskraft
vel_loss = 0.001    # K = U <=> (mv^2)/2 = mgh <=> v = (2gh)^1/2

# air_res är procentuel variabel som är lika med 90% av nuvarande hastighet i x/y led, de 10% är på grund av energi förlust
air_res = 0.9       # v = D/b, D är luftmotståndskraften, b är konstanden som beror på tvärsnittsarean, 
                    # luftens densitet och den dimentionlösa koeficenten

# run
while True:
    screen.update()

    counter += 1                    # to count time
    
    for b in balls:
        b.rt(b.da)                  # balls rotation
        b.dy -= vel_loss            # vel_loss in y-axis
        b.sety(b.ycor() + b.dy)     # changing y cord
        b.setx(b.xcor() + b.dx)     # changing x cord

        # elastiskt kollision med väggar och marken
        # vid kollission ändrar bollarna riktning
        if b.xcor() > 300 or b.xcor() < -300:
            b.dx *= -1
            b.da *= -1

        if b.ycor() < -300:
            b.sety(-300)
            b.dy *= -1
            b.da *= -1

        # lyckades inte implementera leapfrog så i stället körde luftmotstånd beroende på tidsändringen
        if counter % 300 == 0:      # ca. air resistance every 0.3 sec
            b.dx *= air_res
            b.dy *= air_res

    # Wind force
    if counter >= 3000:   # 3000ms = 3s
        for b in balls:
            b.dx += 0.3 * random.choice(wind_dir)
            b.dy += 0.5 * random.choice(wind_dir)
            counter = 0
        print("wind time")

    # Collisions between balls
    # det blir en totalt elastisk kollision mellan bollarna
    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            if balls[i].distance(balls[j]) < 25:
                balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy
