import turtle



turt = turtle.Turtle()
turt.speed(20)
turt.color("LightBlue")
turt.penup()
turt.goto(50,50)
turt.pendown()
turt.forward(200)
def drawbranch(length):
    if length > 5:
        for i in range (3):
            turt.forward(length)
            turt.forward(length)


