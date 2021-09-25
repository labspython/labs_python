import turtle 
turtle.shape('turtle')
k = 3
while k < 10:
  i = k
  while i > 0:
    i -= 1
    turtle.left((360 / k))
    turtle.forward(100+((k-3)*20)) 
  turtle.penup()
  turtle.forward(10)
  turtle.right(90)
  turtle.forward(20)
  turtle.left(90)
  turtle.pendown()
  k += 1
