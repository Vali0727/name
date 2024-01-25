#dobry myslim


from turtle import*
import random
v = Turtle()
x = Turtle()
tekxt = Turtle()

bgcolor("black")
x.color("green")
v.color("hot pink")
tekxt.color("light blue")

pingv = 0
micv = 0
miclp = 0
score = 0

v.begin_poly()#tvar1
v.penup()
v.forward(10)
v.left(90)
v.forward(100)
v.left(90)
v.forward(10)
v.left(90)
v.forward(100)
v.end_poly()
v.goto(-200,0)

x.penup()#tvar2
x.begin_poly()
x.circle(10)
x.end_poly()

xs=x.get_poly()
register_shape("nevim",xs)
x.shape("nevim")#dokoncit tvar2

ch=v.get_poly()
register_shape("nivem",ch)
v.shape("nivem")#dokoncit tvar1

def f():#nahoru
    v.backward(10)

onkeypress(f,"a")
onkey(f,"a")

def b():#dolu
    v.forward(10)

onkeypress(b,"d")
onkey(b,"d")

x.speed(0)#rychle otaceni
x.setheading(180+ random.randrange(10,20))#koment dole

listen()
x.left(180)
while True:
    x.forward(5)#mic

    if x.xcor()<-215:#hovno
        quit()
    elif x.ycor() < v.ycor() and x.ycor() > v.ycor()-120 and x.xcor()<-200:
        if x.heading()>181:
            x.left(90 + random.randrange(1,10))
        else:
            x.right(90 + random.randrange(1,10))

        tekxt.clear()#skore
        score = score+1
        tekxt.write(score)
        x.setx(-200)
    

    if x.ycor() > 340 or x.ycor()<-320: #nahore a dole
        x.left(90 + random.randrange(1,10))
        if x.ycor()<0:
            x.sety(-310)
        else:
            x.sety(330)


    if x.xcor() > 340:#vpravo
        x.left(90 + random.randrange(1,10))
        x.setx(330)

    print(int(v.ycor()))
    #kdyz je mic 180° tak to je v prdeli