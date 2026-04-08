from turtle import *

def reg_polygon(turt, sides):
    turt.begin_fill()
    for i in range(sides):
        turt.fd(200/sides)
        turt.left(360/sides)
    turt.end_fill()

def square(turt):
    turt.pu()
    turt.goto(50,50)
    turt.pd()
    turt.goto(50,-50)
    turt.goto(-50,-50)
    turt.goto(-50,50)
    turt.goto(50,50)
    turt.write("square")

def trapezoid(turt):
    turt.pu()
    turt.goto(-50,50)
    turt.pd()
    turt.goto(-90,0)
    turt.goto(90,0)
    turt.goto(50,50)
    turt.goto(-50,50)
    turt.write("trapezoid")

def rectangle(turt):
    turt.pu()
    turt.goto(-5,5)
    turt.pd()
    turt.goto(8,5)
    turt.goto(8,-5)
    turt.goto(-5,-5)
    turt.goto(-5,5)
    turt.write("Rectangle")

def parallelogram(turt):
    turt.pu()
    turt.goto(4,2)
    turt.pd()
    turt.goto(3,0)
    turt.goto(0,0)
    turt.goto(1,2)
    turt.goto(4,2)
    turt.write("Parallelogram")

def irregular(turt):
    turt.pu()
    turt.goto(4,2)
    turt.pd()
    turt.goto(2,1)
    turt.goto(0,0)
    turt.goto(1,2)
    turt.goto(4,2)
    turt.write("Irregular Quad")





turt = Turtle()
turt.speed(0)
turt.ht()
turt.color("white")
screen = Screen()
screen.title("Polygons")
screen.bgcolor("black")

while True:
    sides = int(input("Think of a shape, then enter the amount of sides it has "))
    turt.clear()
    if sides < 3:
        turt.write("Polygons must have at least three sides")
    elif sides != 4:
        reg_polygon(turt,sides)
    else:
        sp = int(input("How many sides are parallel"))
        if sp == 0:
            irregular(turt)
        
        elif sp == 2:
            trapezoid(turt)

        elif sp == 4:
            side_len = int(input("How many sides are the same length? "))
            
            if side_len == 2:
                rectangle(turt)
            
            elif side_len == 4:
                square(turt)

            elif side_len == 0:
                    parallelogram(turt)
            



    








screen.exitonclick()

    
    