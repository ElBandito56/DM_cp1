#Dm maze generator 2cnd 
#import random and turtle
import random
import turtle
#define and set my variables
#make function to randomize the maze so that its diffrent everytime using random to randomise the floor and walls position



def generatemaze():
    rows = [
        [],
        [],
        [],
        [],
        [],
        []
    ]

    collums= [
        [],
        [],
        [],
        [],
        [],
        []
    ]
    for row in rows:
       for i in range(6):
           row.append(random.randint(0,1))
    for collum in collums:
       for i in range(6):
           row.append(random.randint(0,1))
    return rows,collums
    

def draw_maze(grid):
    turtle.speed(0)
turtle.penup()
turtle.pensize(3)
turtle.goto(x = 0, y = 0)
turtle.pendown()
for i in range(4):
    turtle.forward(60)
    if turtle.ycor() == 360 or turtle.ycor == 0:
        turtle.penup()
        turtle.forward(60)
        turtle.pendown()
        turtle.forward(240)
        turtle.right(90)   
turtle.penup()
turtle.done

#make a function to check if the maze is solveable by checking if it has an opening and a closing    
#make a function to print said maze in tutrtle 
