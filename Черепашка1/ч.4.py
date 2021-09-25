import turtle

turtle.shape('turtle')
turtle.penup()
turtle.goto(-300, -300)
turtle.pendown()
k = 0
while k < 10:
  i = 0
  while i < 4:
    i += 1
    turtle.forward((300 -60*k))
    turtle.left(90)
  turtle.penup()
  turtle.forward(30)
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  turtle.pendown()
  k += 1
