# This example shows how to draw a Triangle

# Library imports
from grid import *

# Start the render process. This must be done before any drawing commands.
start_render()

drawGrid()

firstX = 200
firstY = 200
secondX = 500
secondY = 600
thirdX = 200
thirdY = 700
myColor = [20,20,20]

# Start the render process. This must be done before any drawing commands.
start_render()

drawGrid()

draw_triangle_filled(firstX, firstY, secondX, secondY, thirdX, thirdY, myColor)

"""
firstX:	        x position of first point of triangle.
firstY:	        y position of first point of triangle.
secondX:	    x position of second point of triangle.
secondY:	    y position of second point of triangle.
thirdX          x position of third point of triangle.
thirdY          y position of third point of triangle.
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