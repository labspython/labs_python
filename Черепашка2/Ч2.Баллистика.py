import turtle
turtle.speed(0)
turtle.shape('turtle')
turtle.penup()
turtle.goto( -700, 0)
turtle.pendown()
turtle.left(45)
j = -1
while j < 3:
  j += 1
  i = 0
  x = (-700 + 398*j)
  y = 0
  while i < 3980:
    i += 1
    x += 0.1
    y += (0.1 - 0.0005*(x + 700 - 398*j))
    turtle.goto(x, y)
    
