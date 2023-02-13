from turtle import * # improt turtle module

speed('fastest')
pencolor('red')

for i in range(100):
    forward(i*3+5)
    left(90)

hideturtle()
mainloop()     
