from turtle import*
from random import*

ziziziz=(10)
j=Turtle()
j.color(input("color "))
bgcolor("black")
moov=(4)


ž=Turtle()
ž.sety(110)

while True:
    moov=input("1-fw 2-tl 3-tr ")

    if moov==("1"):
        j.forward(191)
    elif moov==("2"):
        number=input("tl __")
        j.left(int(number))
    elif moov==("3"):
        number=input("tr __")
        j.right(int(number))
    else:
        pass

    if j.xcor()>400 or j.xcor()<-400:
        exit()
    else:
        pass

    if j.ycor()>385 or j.ycor()<-385:
        exit()
    else:
        pass


    ž.color("red")
    ž.setheading(ž.towards(j))
    ž.forward(100)
    if ziziziz>ž.distance(j.pos()):
        exit()