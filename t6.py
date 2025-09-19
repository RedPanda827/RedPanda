import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.penup()
t.speed(0)

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear

def NE():
    t.setheading(45)
    t.forward(10)
    
def NW():
    t.setheading(135)
    t.forward(10)
    
def SW():
    t.setheading(225)
    t.forward(10)
    
def SE():
    t.setheading(315)
    t.forward(10)
    
window.onkeypress( turn_right , '6')
window.onkeypress(turn_up , '8')
window.onkeypress(turn_left , '4')
window.onkeypress(turn_down , '2')
window.onkeypress(blank , 'Escape')
window.onkeypress(NE, '9')
window.onkeypress(NW, '7')
window.onkeypress(SW, '1')
window.onkeypress(SE, '3')

window.listen()

window.mainloop()
