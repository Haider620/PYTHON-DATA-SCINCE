from turtle import *

speed('fastest')
pencolor('green')

for i in range(100):
    fd(i*3+5)
    print(i*5+5)
    lt(90)

mainloop()

