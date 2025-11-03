#Dm 2cnd turtlle Race

#import libaries
import random
import turtle
#Make s finsih line
finish  = turtle.Turtle()
finish.penup()
finish.goto(x=500,y=500)
finish.pendown()
finish.pensize(15)
finish.hideturtle()
finish.right(90)
finish.forward(1000)

#make my 5 turtles
#make turtle 1 
t1 = turtle.Turtle()
t1.color("red")
t1.shape("turtle")
t1.turtlesize(stretch_wid=2, stretch_len=2)
t1.penup()
t1.goto(x=-490,y= 500)
t1.pendown()

#make turtle 2 
t2 = turtle.Turtle()
t2.color("purple")
t2.shape("turtle")
t2.turtlesize(stretch_wid=2, stretch_len=2)
t2.pensize(3)
t2.penup()
t2.goto(x=-490,y= 250)
t2.pendown()
#make turtle 3 
t3 = turtle.Turtle()
t3.color("green")
t3.shape("turtle")
t3.penup()
t3.goto(x=-490,y= 0)
t3.pendown()
t3.turtlesize(stretch_wid=2, stretch_len=2)
t3.pensize(3)
#make turtle 4
t4 = turtle.Turtle()
t4.color("brown")
t4.shape("turtle")
t4.turtlesize(stretch_wid=2, stretch_len=2)
t4.pensize(3)
t4.penup()
t4.goto(x=-490,y= -250)
t4.pendown()
#make turtle 5
t5 = turtle.Turtle()
t5.color("pink")
t5.shape("turtle")
t5.turtlesize(stretch_wid=2, stretch_len=2)
t5.pensize(3)
t5.penup()
t5.goto(x=-490,y= -500)
t5.pendown()
#randomize speed for each turtle 
while True:
    t1 .forward(random.randint (10,50))
    t2.forward(random.randint (10,50))
    t3.forward(random.randint (10,50))
    t4.forward(random.randint (10,50))
    t5 .forward(random.randint (10,50))
    finish_line = 500
#check what turtle one
    if t1 > finish_line:
        print("The red turtle won")
        break
    elif t2 > finish_line:
        print('the purple turtle won')
        break
    elif t3 > finish_line:
        print("the green turtle won")
        break
    elif t4 > finish_line:
        print('the brown turtle won')
        break
    elif t5 > finish_line:
        print("the pink turtle one")
        break
    else:
        continue
               
    #display " this (turtle who won) won"
turtle.done()
   