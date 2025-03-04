import turtle

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('yellow')

t = turtle.Turtle()
t.speed(0)
t.setheading(135)
t.fillcolor('cyan')
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.goto(0,0)
t.pendown()

t.setheading(45)
t.fillcolor('brown')
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()

t.hideturtle()

#this changes turtle location
t.penup()
t.goto(25,-100)
t.pendown()

#change direction of turtle
t.setheading(0)

# t.forward(25)
# t.penup()
# t.forward(25)
# t.pendown()
# t.forward(25)
# t.penup()
# t.forward(25)
# t.pendown()
# t.forward(25)
# t.penup()
# t.forward(25)
# t.pendown()
# t.forward(25)
# t.penup()
# t.forward(25)
#
# t.penup()
# t.goto(-200,100)
# t.pendown()
#
# t.dot()
# t.penup()
# t.forward(25)
# t.pendown()
# t.dot()
# t.penup()
# t.forward(25)
# t.pendown()
# t.dot()
# t.penup()
# t.forward(25)
# t.pendown()
# t.dot()
#
# t.penup()
# t.goto(-200,0)
# t.pendown()
# t.pencolor('green')
# t.pensize(8)
# t.goto(-200,-100)
# t.pensize(1)
#
# t.penup()
# t.goto(-200,0)
# t.pendown()
#
# t.pencolor('pink')
# t.fillcolor('pink')
# t.begin_fill()
# t.circle(25)
# t.setheading(90)
# t.circle(25)
# t.setheading(180)
# t.circle(25)
# t.setheading(270)
# t.circle(25)
# t.end_fill()
#
# t.penup()
# t.goto(-200,-15)
# t.pendown()
# t.setheading(0)
# t.fillcolor('yellow')
# t.begin_fill()
# t.circle(15)
# t.end_fill()
#
# #triagle
# t.penup()
# t.goto(0,125)#1
# t.pendown()
# t.pencolor('red')
# t.fillcolor('khaki')
# t.begin_fill()
# t.goto(100,125)#2
# t.goto(50,175)#3
# t.goto(0,125)#1
# t.end_fill()
#
# t.penup()
# t.goto(-100,-200)#1
# t.pendown()
# t.pensize(5)
# t.fillcolor('sienna1')
# # t.setheading(180)
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# t.fillcolor('purple')
# t.begin_fill()
# t.circle(50,120)
# t.end_fill()
# t.fillcolor('green')
# t.begin_fill()
# t.circle(50,120)
# t.end_fill()
# t.fillcolor('dodgerblue')
# t.begin_fill()
# t.circle(50,120)
# t.end_fill()
#
# t.penup()
# t.goto(-200,200)#1
# t.pendown()
#
# t.write("Hello",font=("Arial",30,"bold italic"),align="center")
#
#
#


#No code after this line
turtle.done()