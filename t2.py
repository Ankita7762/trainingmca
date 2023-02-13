from turtle import *

speed('fastest')
pencolor('red')

gap = 3
angal = 32
for i in range(100):
    fd(i*gap)  # 11
    lt(angal)
    
    hideturtle()
    mainloop()