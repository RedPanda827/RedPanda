import turtle as t


t.bgcolor('black')
t.shape("turtle")
t.color('yellow')

t.penup()
t.goto(100.100)

t.pendown()

angle = 90

for x in range(50):
    t.forward(x)
    t.left(angle)

t.done()
