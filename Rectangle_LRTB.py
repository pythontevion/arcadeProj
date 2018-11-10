#This example shows how to draw a LRTB Rectangle

from grid import *

# Start the render process. This must be done before any drawing commands.
start_render()

drawGrid()

leftEdge = 200
rightEdge = 600
topEdge = 500
bottomEdge = 100
myColor = [20,20,20]

draw_lrtb_rectangle_filled(leftEdge, rightEdge, topEdge, bottomEdge, myColor)


"""
leftEdge:	    x position of left edge of rectangle.
rightEdge:	    x position of right edge of rectangle.
topEdge:	    y position of top edge.
bottomEdge:	    y position of bottom edge.
myColor:	    color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
"""


"""
Finish the render.
Nothing will be drawn without this.
Must happen after all draw commands
"""

finish_render()

# Keep the window up until someone closes it.
run()