import turtle
import colorsys
p= turtle.Turtle()
turtle.bgcolor("black")
p.speed(0) 
p.width(5)
turtle.colormode(1.0)
def draw_pookalam(radius,numcirc):
    h = 0  
    for i in range(numcirc):
        p.circle(radius)
        p.right(360 / numcirc) 
        h += 1 / numcirc
        color = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        p.pencolor(color)
radius = 80
numcirc = 36
draw_pookalam(radius, numcirc)
p.hideturtle()
turtle.done()
