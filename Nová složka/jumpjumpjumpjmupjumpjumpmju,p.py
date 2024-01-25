from turtle import*

platf=Turtle()
tr = Turtle()
tr.speed(0)
tr.color("hot pink")
bgcolor("black")
platf.color("white")


platf.begin_poly()#zem,######
platf.penup()
platf.forward(1000)
platf.left(90)
platf.forward(10)
platf.left(90)
platf.forward(1000)
platf.left(90)
platf.forward(10)
platf.end_poly()
platf.goto(500,-25)


plf = platf.get_poly()
register_shape("gr",plf)
platf.shape("gr")

tr.begin_poly()#hrac
tr.left(90)
tr.forward(-10)
tr.right(90)
tr.circle(10)
tr.end_poly()

rt = tr.get_poly()
register_shape("rtrt",rt)
tr.shape("rtrt")

def l():
    tr.setheading(180)
    tr.forward(7)

def r():
    tr.setheading(0)
    tr.forward(10)

mhr = 5

def j():
    global mhr
    if mhr==0:
        mhr = 5

def c():
    tr.clear()



onkeypress(l,"a")
onkey(l,"a")
onkeypress(r,"d")
onkey(r,"d")

onkey(j,"j")
onkey(c,"c")


listen()

while True:
    if mhr != 0:
        mhr -=float(0.2)
    
    yp = tr.ycor()

    if yp < -20:
        tr.sety(-19)
        mhr -= mhr
    print(mhr,"m")

    yp = tr.ycor()

    tr.sety(yp + mhr)

