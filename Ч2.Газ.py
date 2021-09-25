from random import randint
import turtle


number_of_turtles = 10
steps_of_time_number = 1000


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(randint(0, 1))
    unit.goto(randint(-600, 600), randint(-350, 350))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(randint(-70, 70))
        unit.left(randint(0, 180))
