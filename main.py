 turtle import *
color('red')
begin_fill()
penup()
setpos(120,0)
while True:
    backward(250)
    right(120)
    if abs(pos()) < 120:
        break
end_fill()

color('blue')
begin_fill()
penup()
setpos(120,0)
while True:
    forward(120)
    left(90)
    if abs(pos()) < 120:
        break
end_fill()
color('green')
begin_fill()
setpos(0,300)
circle(100)
end_fill()
setpos(0,0)
done()
