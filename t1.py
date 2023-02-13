from turtle import * # improt turtle module

speed('fastest')

side = 10
size = 50

# create a hexagon
for i in range(side):
    forward(size)
    left(360/size)
    write(i)

hideturtle()
mainloop()     
