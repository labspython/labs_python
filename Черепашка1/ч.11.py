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
    turtle.forward(0.8)
    turtle.left(1)
  k = 180
  while k > 0:
    k -= 1
    turtle.forward(0.08)
    turtle.left(1)
