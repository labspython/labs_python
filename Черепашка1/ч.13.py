import turtle

turtle.shape('turtle')
n = input()
g = int(n)
i = g
while i > 0:
  i -= 1
  turtle.forward(400)
  turtle.right(180*(1 - (1 / g)))

