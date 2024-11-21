import turtle

#SETTING UP SCREEN
screen = turtle.Screen()
#BACKGROUND COLOR
screen.bgcolor("black")  

# Create a turtle
my_turtle = turtle.Turtle()
#SHAPE OF TURTLE
my_turtle.shape("circle")  
#COLOR OF TURTLE
my_turtle.color("white")  
#SPEED OF TURTLE 
my_turtle.speed(2)    

#DRAWING THE FIRST SQUARE
for _ in range(4):
    my_turtle.forward(100)  
    my_turtle.left(90)      

#MOVING THE TURTLE TO A NEW POSITION
my_turtle.penup()         
my_turtle.goto(100, 0)     
my_turtle.pendown()        

#DRAWING THE SECOND SQUARE
for _ in range(4):
    # MOV THE TURTLE FORWARD BY 100 UNITS
    my_turtle.forward(100)  
    #TRUING THE TURTLE LEFT BY 90 DEGREE 
    my_turtle.left(90)      

#KEEPING THE WINDOW OPEN UNTIL ITS CLICKED
screen.exitonclick()
import turtle

#SETTING UP SCREEN
screen = turtle.Screen()
#BACKGROUND COLOR
screen.bgcolor("black")  

# Create a turtle
my_turtle = turtle.Turtle()
#SHAPE OF TURTLE
my_turtle.shape("circle")  
#COLOR OF TURTLE
my_turtle.color("white")  
#SPEED OF TURTLE 
my_turtle.speed(2)    

#DRAWING THE FIRST SQUARE
for _ in range(4):
    my_turtle.forward(100)  
    my_turtle.left(90)      

#MOVING THE TURTLE TO A NEW POSITION
my_turtle.penup()         
my_turtle.goto(100, 0)     
my_turtle.pendown()        

#DRAWING THE SECOND SQUARE
for _ in range(4):
    # MOV THE TURTLE FORWARD BY 100 UNITS
    my_turtle.forward(100)  
    #TRUING THE TURTLE LEFT BY 90 DEGREE 
    my_turtle.left(90)      

#KEEPING THE WINDOW OPEN UNTIL ITS CLICKED
screen.exitonclick()
