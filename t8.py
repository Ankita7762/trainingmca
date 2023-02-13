from turtle import * # improt turtle module

s = Screen()
s.setup(400,400)
s.bgcolor('black')

speed('fastest')
pencolor('yellow')

for i in range(5):
     left(72)
     for i in range(5):
        forward(100)
        rt(144)
     
hideturtle()
mainloop()     
