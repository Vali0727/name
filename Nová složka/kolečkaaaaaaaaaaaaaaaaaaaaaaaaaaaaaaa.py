from turtle import*
from random import*

colore = input("color ") #terminál
colore2 = input("color1 " + colore + " color2 ")
colore3 = input("color1 " + colore + " color2 " + colore2 + " color3 ")
print(colore + " " + colore2 + " " + colore3)
bgcolore = input("bg color ") #terminál

color(colore)
bgcolor(bgcolore)
setx(0)
sety(0)
speed(3)

while True:

    color(colore)
    pendown()
    begin_fill()
    circle(randrange(75,125))
    end_fill()
    penup()
    sety (randrange(-200,200))
    setx (randrange(-200,200))

    color(colore2)
    pendown()
    begin_fill()
    circle(randrange(75,125))
    end_fill()
    penup()
    sety (randrange(-200,200))
    setx (randrange(-200,200))

    color(colore3)
    pendown()
    begin_fill()
    circle(randrange(75,125))
    end_fill()
    penup()
    sety (randrange(-200,200))
    setx (randrange(-200,200))

    colore = input("color ") #terminál
    colore2 = input("color2 ") #terminál
    colore3 = input("color3 ") #terminál
    print(colore + " " + colore2 + " " + colore3)

done()