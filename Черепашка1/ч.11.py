import turtle
turtle.speed(0)
turtle.shape('turtle')
turtle.left(90)
j = 0
while j < 5:
  j += 1
  i = 180
  while i > 0:
    i -= 1
    turtle.forward(0.5)
    turtle.left(1)
  turtle.left(90)
  turtle.forward(5)
  turtle.left(90)
