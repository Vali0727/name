from turtle import*


pendown()

color(input("barva "))

while True:

    def rerede(x, y):

        setheading(towards(x,y))
        goto(x,y)

    onrelease(rerede)

    listen()
    onkey(begin_fill, "s")
    onkey(end_fill, "d")
