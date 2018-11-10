# This example shows how to draw an arc

# Library imports
from grid import *

# Start the render process. This must be done before any drawing commands.
start_render()

drawGrid()

xPos = 300
yPos = 300
width = 50
height = 50
startAngle = 0
endAngle = 270
myColor = [20,20,20]
lineWidth = 2
tiltAngle = 0

draw_arc_outline(xPos, yPos,    # center of arc
                 width,         # width
                 height,        # height
                 myColor,       # color of ouline
                 startAngle,    # start angle
                 endAngle,      # end angle
                 lineWidth,     # line width
                 tiltAngle      # tilted
                 )

"""
center_x:	    x position that is the center of the arc.
center_y:	    y position that is the center of the arc.
width:	        width of the arc.
height:	        height of the arc.
myColor:	    color, specified in a list of 3 or 4 bytes in RGB or RGBA format.
startAngle:	    start angle of the arc in degrees.
endAngle:	    end angle of the arc in degrees.
lineWidth:	    width of line in pixels.
tiltAngle:	    angle the arc is tilted.


Finish the render.
Nothing will be drawn without this.
Must happen after all draw commands
"""

finish_render()

# Keep the window up until someone closes it.
run()