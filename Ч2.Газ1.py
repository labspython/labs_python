from random import randint
import turtle
q = 99999
while q > 0:
  q -= 1
  number_of_turtles = 15
  steps_of_time_number = 1000
  pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
  for unit in pool:
      unit.penup()
      unit.speed(randint(0, 3))
      unit.goto(randint(-400, 400), randint(-400, 400))
      unit.seth(randint(0, 360))
  for i in range(steps_of_time_number):
      for j in range(len(pool)):
          angle1 = pool[j].heading()
          x, y = pool[j].pos()
      if x[j]< -400 or x[j]> 400:
          pool[j].seth(180 - (angle1[j]))
      elif y[j]< -400 or y[j]> 400:
          pool[j].seth(-angle1[j])
      pool[j].forward(10)
