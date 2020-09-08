import turtle


p=turtle.Turtle()
p.speed(0.5)
p.color("#34495e","#3498db")

p.begin_fill()
p.forward(200)
p.left(90)
p.forward(200)
p.left(90)
p.forward(200)
p.left(90)
p.forward(200)

for i in range(100):
    p.left(170.5)
    p.forward(200)
    p.left(90)
    p.forward(200)
    p.left(90)
    p.forward(200)
    p.left(90)
    p.forward(200)
p.end_fill()    
turtle.done()
