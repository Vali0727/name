
from math import*
from turtle import*
color("grey")
bgcolor("grey")

v= Turtle()
j= Turtle()

v.color("pink")
j.color("red")

a = input(" ,,jen celá, a")
úhel=input("výškA strany")


#podstava
v.forward(int(a))
v.left(90)
v.forward(int(a))
v.left(90)
v.forward(int(a))
v.left(90)
v.forward(int(a))

#výška
j.left(90)
j.forward(int(int(a)/int(2)))
j.left(90)
j.forward(int(úhel))

#hrana
c = int(sqrt(int(a)/2*int(a)/2+int(úhel)*int(úhel)))
print(c)
#první strana
v.setheading(v.towards(j))
v.forward(v.distance(j.pos()))
v.goto(0,0)
v.setheading(0)
v.left(90)
v.forward(int(a))
v.setheading(v.towards(j))
v.forward(v.distance(j.pos()))

v.goto(0,0)
v.setheading(0)
v.left(90)
j.setheading(j.towards(v))
j.left(180)
gam = j.heading()
mu = v.heading()
print("smery",gam,mu)
VADu = (gam-mu)
print("uhel",int(VADu))

#uhel u hlavniho 
v.forward(int(a))
v.setheading(v.towards(j))
v.forward(c)
v.left(180)
j.left(180)
mu = v.heading()
gam = j.heading()
print("gam",gam,"mu",mu)
hlavuh = (mu-gam)
print(hlavuh , mu , gam)
    
v.goto(0,0)
v.setheading(0)
v.left(90)
v.forward(int(a))

#druhej trojuhelnik
v.left(hlavuh)
v.forward(int(a))
j.setheading(j.towards(v))
j.forward(int(c))

v.left(hlavuh)
v.forward(int(a))
j.backward(int(c))
j.setheading(j.towards(v))
j.forward(int(c))

#posledni
j.backward(int(c))
v.penup()
v.goto(0,0)
v.setheading(0)
v.pendown()
v.right(90)
v.right(hlavuh)
v.forward(int(a))
j.setheading(j.towards(v))
j.forward(int(c))
input()
quit()
