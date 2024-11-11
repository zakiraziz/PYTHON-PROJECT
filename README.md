# Turtle Graphics Fun with Shapes! 🐢🎨

This Python project uses the `turtle` module to create a colorful design with shapes like triangles and circles. It demonstrates basic drawing techniques, such as using loops, color fills, and shape positioning.

## Project Description

In this project, we:
- Draw a red-filled triangle. 
- Draw a blue-filled square.
- Draw a green-filled circle.
 
The shapes are created using loops, and the turtle is positioned at specific points to draw each shape sequentially. 
 
## Code

```python
from turtle import *

# Drawing a red-filled triangle
color('red')
begin_fill()
penup()
setpos(120, 0)
while True:
    backward(250)
    right(120)
    if abs(pos()) < 120:
        break
end_fill()

# Drawing a blue-filled square
color('blue')
begin_fill()
penup()
setpos(120, 0)
while True:
    forward(120)
    left(90)
    if abs(pos()) < 120:
        break
end_fill()

# Drawing a green-filled circle
color('green')
begin_fill()
setpos(0, 300)
circle(100)
end_fill()

# Resetting position
setpos(0, 0)
done()
