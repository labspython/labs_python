import turtle as t

t.shape('turtle')
numbers_dict = {
    '0': [(0, 0), (270, 100), (270, 50), (270, 100), (270, 50), (0, 0)],
    '6': [(0, 0), (225, 71), (45, 50), (90, 50), (90, 50), (90, 50), (0, 0)],


    
 }

index = '060'

for number in index:
    list_coords = numbers_dict[number]
    start = list_coords[0]
    t.penup()
    angle, step = start
    t.left(angle)
    t.forward(step)
    t.pendown()
    for coords in list_coords[1:-1]:
      angle, step = coords
      t.left(angle)
      t.forward(step)
    t.penup()
    finish = list_coords[-1]
    angle, step = finish
    t.left(angle)
    t.forward(step)
    t.forward(100)
    
    
