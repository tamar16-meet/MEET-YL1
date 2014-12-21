import turtle

turtle.hideturtle()
turtle.speed(0)

turtle.getscreen().listen()

color="red"
def brush_b_circle(x,y):
    
    turtle.begin_fill()
    #turtle.color("blue")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(20)
    turtle.end_fill()

def brush_r_square(x,y):
    turtle.begin_fill()
    #turtle.color("red")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+50,y)
    turtle.goto(x+50,y+50)
    turtle.goto(x,y+50)
    turtle.goto(x,y)
    turtle.end_fill()
'''
def brush_r_circle(x,y):
    turtle.begin_fill()
    turtle.color("red")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(20)
    turtle.end_fill()

def brush_b_square(x,y):
    turtle.begin_fill()
    turtle.color("blue")
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+50,y)
    turtle.goto(x+50,y+50)
    turtle.goto(x,y+50)
    turtle.goto(x,y)
    turtle.end_fill()

'''


turtle.onclick(brush_b_circle,btn=1, add=True)
turtle.onscreenclick(brush_b_circle,btn=1, add=True)

turtle.onclick(brush_b_square,btn=3, add=True)
turtle.onscreenclick(brush_b_square,btn=3, add=True)

def change_to_red():
    turtle.color("red")
    turtle.pencolor("red")
turtle.onkeypress(change_to_red, "r")

def change_to_blue():
    turtle.color("blue")
    turtle.pencolor("blue")
turtle.onkeypress(change_to_blue, "b")
    
    


#turtle.onclick(brush_r_circle,"up", add=True)
    #turtle.onscreenclick(brush_r_circle,"up", add=True)

    #turtle.onclick(brush_r_square,"up", add=True)
    #turtle.getscreen().onkeypress(brush_r_square,"Up")
    #turtle.getscreen().listen()
    #turtle.onscreenclick(brush_r_square,"up", add=True)


#What I actually did is 4 keys on the the keyboard that each one of them does other function
#1. circle blue 2.square red 3.circle red 4.square red
# but of course function 2,3 didnt work
#sorry:( i dont know..






