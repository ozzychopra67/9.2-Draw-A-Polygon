from turtle import *

def reg_polygon(turt, sides):
    turt.begin_fill()
    for i in range(sides):
        turt.fd(200/sides)
        turt.left(360/sides)
    turt.end_fill()

def 




turt = Turtle()
turt.speed(0)
turt.ht()
turt.color("teal")
screen = Screen()
screen.title("Polygons")
screen.bgcolor("black")

while True:
    sides = int(input("Think of a shape, then enter the amount of sides it has "))
    turt.clear()
    if sides < 3:
        turt.write("Polygons must have at least three sides")
    elif sides != 4:
        regular_polygon(pen,sides)
    else:
        sp = int(input("How many sides are parallel"))
        if sp == "0":
        
        elif sp == "2":

        elif sp == 4:
            side_len = int(input("How many sides are the same length (2 or 4)? "))
            
            if side_len == 2:
            
            elif side_len == 4:
                



    








screen.exitonclick()

    
    