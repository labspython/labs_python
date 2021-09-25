from random import randint

import turtle

number_of_turtles = 15
steps_of_time_number = 1000
pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]

q = 99999
while q > 0:
  q -= 1
  for unit in pool:
      unit.penup()
#       unit.speed(randint(0, 3))
      unit.goto(randint(-400, 400), randint(-400, 400))
      unit.seth(randint(0, 360))
  for i in range(steps_of_time_number):
      for j in range(len(pool)):
          angle1 = pool[j].heading()
          x, y = pool[j].pos()

  if x < -400 or x > 400:
    pool[j].seth((180 - (angle1)))
  elif y < -400 or y > 400:
    pool[j].seth(-angle1)
  pool[j].forward(10)
