import turtle as t

import random

t.shape('turtle')
t.speed(10)

for x in range(10):
    a = random.randint(1,360)
    t.setheading(a)
    t.forward(100)
