#Dm 2cnd turtlle Race

#import libaries
import random
import turtle
#Make s finsih line
#make my 5 turtles
#make turtle 1 
t1 = turtle.Turtle()
t1.color("red")
t1.shape("turtle")
t1.turtlesize(stretch_wid=2, stretch_len=2)

#make turtle 2 
t2 = turtle.Turtle()
t2.color("purple")
t2.shape("turtle")
t2.turtlesize(stretch_wid=2, stretch_len=2)
t2.pensize(3)
#make turtle 3 
t3 = turtle.Turtle()
t3.color("green")
t3.shape("turtle")
t3.turtlesize(stretch_wid=2, stretch_len=2)
t3.pensize(3)
#make turtle 4
t4 = turtle.Turtle()
t4.color("brown")
t4.shape("turtle")
t4.turtlesize(stretch_wid=2, stretch_len=2)
t4.pensize(3)
#make turtle 5
t5 = turtle.Turtle()
t5.color("pink")
t5.shape("turtle")
t5.turtlesize(stretch_wid=2, stretch_len=2)
t5.pensize(3)
#randomize speed for each turtle 
t1 .forward(random.randint (1,500))
t2.forward(random.randint (1,500))
t3.forward(random.randint (1,500))
t4.forward(random.randint (1,500))
t5 .forward(random.randint (1,500))
#check what turtle one
#display " this (turtle who won) won"
turtle.done