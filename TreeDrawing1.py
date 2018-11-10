"""
Example "Arcade" library code.

This example shows how to use functions to draw a scene.
It does not assume that the programmer knows how to use classes yet.

A video walk-through of this code is available at:
https://vimeo.com/167296062

"""

# Library imports
from arcade import *

def draw_background():
    """
    This function draws the background. Specifically, the sky and ground.
    """
    # Draw the sky in the top two-thirds
    draw_lrtb_rectangle_filled(0, 600, 600, 400, color.SKY_BLUE)

    # Draw the ground in the bottom third
    draw_lrtb_rectangle_filled(0, 600, 400, 0, color.DARK_SPRING_GREEN)


def draw_bird(x, y):
    """
    Draw a bird using a couple arcs.
    """
    draw_arc_outline(x, y, 20, 20, color.BLACK, 0, 90)
    draw_arc_outline(x + 40, y, 20, 20, color.BLACK, 90, 180)


def draw_pine_tree(x, y):
    """
    This function draws a pine tree at the specified location.
    """
    # Draw the triangle on top of the trunk
    draw_triangle_filled(x + 40, y, x, y - 100, x + 80, y - 100, color.DARK_GREEN)

    # Draw the trunk
    draw_lrtb_rectangle_filled(x + 30, x + 50, y - 100, y - 140, color.DARK_BROWN)


def main():
    """
    This is the main program.
    """

    # Open the window
    open_window(600, 600, "Drawing With Functions")

    # Start the render process. This must be done before any drawing commands.
    start_render()

    # Call our drawing functions.
    draw_background()
    draw_pine_tree(50, 250)
    draw_pine_tree(350, 320)
    draw_bird(70, 500)
    draw_bird(470, 550)

    # Finish the render.
    # Nothing will be drawn without this.
    # Must happen after all draw commands
    finish_render()

    # Keep the window up until someone closes it.
    run()


if __name__ == "__main__":
    main()