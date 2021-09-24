import turtle
turtle.speed(0)
turtle.shape('turtle')
turtle.left(90)
j = 0
while j < 10:
  j += 1
  i = 360
  while i > 0:
    i -= 1
    turtle.forward(1+(j / 5))
    turtle.left(1)
  k = 360
  while k > 0:
    k -= 1
    turtle.forward(1+(j / 5))
    turtle.right(1)
