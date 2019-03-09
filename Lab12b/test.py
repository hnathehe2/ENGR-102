from turtle import *

def drawsquare ():
    # Start square
    forward (100)
    left ( 90 )
    forward ( 100 )
    left ( 90 )
    forward ( 100 )
    left ( 90 )
    # Close square
    forward ( 100 )
    # Return turtle to original orientation
    left ( 90 )
# Draw a square using our function
drawsquare ()
# Pick up pen - no drawing
up ()
# Move turtle
forward ( 150 )
# Draw another square using our function
down () # put pen down first
drawsquare ()
# Finished
done ()