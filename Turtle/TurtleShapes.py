"""
Lower the pen to a piece of paper
Move the pen along a straight line
Turn 90 degrees to right
Move the pen along a straight line
Turn 90 degrees to right
Move the pen along a straight line
Turn 90 degrees to right
Move the pen along a straight line
Turn 90 degrees to right
Raise the pen from the paper


Move the pen along a straight line for 200

Lower the pen to a piece of paper
Move the pen along a straight line for 100
Turn 90 degrees to right
Move the pen along a straight line for 50
Turn 90 degrees to right
Move the pen along a straight line for 100
Turn 90 degrees to right
Move the pen along a straight line for 50
Raise the pen from the paper

Move the pen along a straight line for 150

Lower the pen to a piece of paper
Move the pen along a straight line for 100
Turn 45 degrees to right
Move the pen along a straight line for 50
Turn 90 degrees to right
Turn 45 degrees to right
Move the pen along a straight line for 100
Turn 45 degrees to right
Move the pen along a straight line for 50
Turn 45 degrees to right
Raise the pen from the paper

Move the pen along a straight line for 200

Lower the pen to a piece of paper
Draw a circle radius 50
Turn 90 degrees to right
Raise the pen from the paper
Move the pen along a straight line for 25
Turn 90 degrees to right
Turn 90 degrees to right
Turn 90 degrees to right
Lower the pen to a piece of paper
Draw a circle radius 25
"""

from turtle import *

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

penup()
goto(200,0)
pendown()

forward(100)
right(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)
right(90)

penup()
goto(200,200)
pendown()

forward(100)
right(45)
forward(50)
right(90)
right(45)
forward(100)
right(45)
forward(50)
right(45)

penup()
goto(100,150)
pendown()

circle(50)
right(90)
right(90)
right(90)
penup()
forward(25)
pendown()
right(90)

circle(25)

done()
