# Library imports
from arcade import *

# Constants - variables that do not change
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 850


# Open the window
open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing With Functions")
set_background_color(color.YELLOW_ORANGE)

def drawGrid():
    x = 0
    for y in range(0, 850, 50):
        draw_line(x + 25, y, 800, y , color.BLACK)
        if y == 0:
            draw_text(str(y), x, y, color.BLACK, 12, width=5, align="centre")
        else:
            draw_text(str(y), x, y - 4, color.BLACK, 12, width=5, align="centre")

    y = 0
    for x in range(0, 850, 50):
        draw_line(x, y + 10, x, 800, color.BLACK)
        if x == 0:
            draw_text(str(x), x, y, color.BLACK, 12, width=5, align="centre")
        else:
            draw_text(str(x), x - 8, y, color.BLACK, 12, width=5, align="centre")

