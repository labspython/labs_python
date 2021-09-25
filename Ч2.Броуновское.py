import turtle
from random import *
turtle.shape('turtle')
turtle.speed(0)
i = 999999
while i > 0:
  i -= 1
  k = float(randint(20, 50))
  j = float(randint(0, 359))
  turtle.forward(k)	
  turtle.left(j)
