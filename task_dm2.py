from drawman import *
from time import sleep

def f(x):
    return x*x

drawman_scale(20)

x=-10.0
to_point(x,f(x))
pen_down()
while x<=10:
    to_point(x,f(x))
    x+=0.1
pen_up()

sleep(10)
