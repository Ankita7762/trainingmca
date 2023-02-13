from turtle import *

pencolor('blue')
pensize(3)
fillcolor('red')
speed('fastest')

for i in range(10,0,-1):
    circle(i * 10)
    left(25)

hideturtle()
mainloop()


    