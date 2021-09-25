import turtle
turtle.speed(0)
turtle.shape('turtle')
j = 3
while j > 0:
  j -= 1
  i = 360
  while i > 0:
    i -= 1
    turtle.forward(1)
    turtle.left(1)
  k = 360
  while k > 0:
    k -= 1
    turtle.forward(1)
    turtle.right(1)
  turtle.left(120)
