
from grid import *

# Draw a car
def draw_car(x, y):

    # car body
    leftEdge = x
    rightEdge = x + 70
    topEdge = y
    bottomEdge = y - 30
    myColor = [120, 120,120]
    draw_lrtb_rectangle_filled(leftEdge, rightEdge, topEdge,  bottomEdge, myColor)

    # wheel 1
    wheel_x = x + 15
    wheel_y = bottomEdge
    wheel_dia = 15
    draw_circle_filled(wheel_x + 15, wheel_y, wheel_dia, color.BLACK)

    # wheel 2

# Draw everything
def on_draw(delta_time):
    start_render()
    global car_x
    draw_car(car_x, 400)

    # Add one to the x value, making the car move right
    # Negative numbers move left. Larger numbers move faster.
    car_x += 2


# Create a value that our car will start at.
car_x = 0

# Call on_draw every 100th of a second.
schedule(on_draw, 1/60)
run()


