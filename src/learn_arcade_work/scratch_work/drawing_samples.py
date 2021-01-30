"""
Title: Sunset on a scenic lawn

This is a sample drawing script.
"""
import arcade

arcade.open_window(600, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.EARTH_YELLOW)

# Begin drawing
arcade.start_render()

# Drawing code goes here

# Draw some grass
arcade.draw_lrtb_rectangle_filled(
    left=0, right=599, top=300, bottom=0, color=arcade.csscolor.GREEN
)

# Tree 1
# Draw a tree stump on top of the grass
arcade.draw_lrtb_rectangle_filled(
    left=100, right=120, top=350, bottom=300, color=arcade.csscolor.SIENNA
)
# Draw a top on top of the tree
arcade.draw_circle_filled(
    center_x=110, center_y=350, radius=30, color=arcade.csscolor.DARK_GREEN
)

# Tree 2
# Note that the ellipses are specified by their center and
# by the dimensions of the rectangle they are contained in.
arcade.draw_lrtb_rectangle_filled(
    left=200, right=220, top=350, bottom=300, color=arcade.csscolor.SIENNA
)
arcade.draw_ellipse_filled(
    center_x=210,
    center_y=370,
    width=60,
    height=80,
    color=arcade.csscolor.DARK_GREEN,
)

# Tree 3
arcade.draw_lrtb_rectangle_filled(
    left=300,
    right=320,
    top=350,
    bottom=300,
    color=arcade.csscolor.SIENNA,
)
arcade.draw_arc_filled(
    center_x=310,
    center_y=340,
    width=60,
    height=80,
    start_angle=0,
    end_angle=180,
    color=arcade.csscolor.DARK_GREEN,
)

# Tree 4
arcade.draw_lrtb_rectangle_filled(
    left=400,
    right=420,
    top=350,
    bottom=300,
    color=arcade.csscolor.SIENNA,
)
arcade.draw_triangle_filled(
    x1=410,
    y1=400,
    x2=380,
    y2=340,
    x3=440,
    y3=340,
    color=arcade.csscolor.DARK_GREEN,
)

# Tree 5
arcade.draw_lrtb_rectangle_filled(
    left=500,
    right=520,
    top=350,
    bottom=300,
    color=arcade.csscolor.SIENNA,
)
arcade.draw_polygon_filled(
    ((510, 400), (490, 360), (480, 320), (540, 320), (530, 360)),
    arcade.csscolor.DARK_GREEN,
)

# Draw a sun
CIRCLE_CENTER_X = 510
CIRCLE_CENTER_Y = 500
RAY_WIDTH = 3
RAY_RADIUS = 75
COLOR_SUN = arcade.csscolor.ORANGE_RED

arcade.draw_circle_filled(
    center_x=CIRCLE_CENTER_X,
    center_y=CIRCLE_CENTER_Y,
    radius=40,
    color=COLOR_SUN,
)
# Left ray
arcade.draw_line(
    start_x=CIRCLE_CENTER_X,
    start_y=CIRCLE_CENTER_Y,
    end_x=CIRCLE_CENTER_X - RAY_RADIUS,
    end_y=CIRCLE_CENTER_Y,
    color=COLOR_SUN,
    line_width=RAY_WIDTH,
)
# Right ray
arcade.draw_line(
    start_x=CIRCLE_CENTER_X,
    start_y=CIRCLE_CENTER_Y,
    end_x=CIRCLE_CENTER_X + RAY_RADIUS,
    end_y=CIRCLE_CENTER_Y,
    color=COLOR_SUN,
    line_width=RAY_WIDTH,
)
# Top ray
arcade.draw_line(
    start_x=CIRCLE_CENTER_X,
    start_y=CIRCLE_CENTER_Y,
    end_x=CIRCLE_CENTER_X,
    end_y=CIRCLE_CENTER_Y + RAY_RADIUS,
    color=COLOR_SUN,
    line_width=RAY_WIDTH,
)
# Bottom ray
arcade.draw_line(
    start_x=CIRCLE_CENTER_X,
    start_y=CIRCLE_CENTER_Y,
    end_x=CIRCLE_CENTER_X,
    end_y=CIRCLE_CENTER_Y - RAY_RADIUS,
    color=COLOR_SUN,
    line_width=RAY_WIDTH,
)
# Diagonal rays
arcade.draw_line(
    start_x=CIRCLE_CENTER_X,
    start_y=CIRCLE_CENTER_Y,
    end_x=CIRCLE_CENTER_X + 0.5 * RAY_RADIUS,
    end_y=CIRCLE_CENTER_Y + 0.5 * RAY_RADIUS,
    color=COLOR_SUN,
    line_width=RAY_WIDTH,
)
arcade.draw_line(
    start_x=CIRCLE_CENTER_X,
    start_y=CIRCLE_CENTER_Y,
    end_x=CIRCLE_CENTER_X - 0.5 * RAY_RADIUS,
    end_y=CIRCLE_CENTER_Y - 0.5 * RAY_RADIUS,
    color=COLOR_SUN,
    line_width=RAY_WIDTH,
)
arcade.draw_line(
    start_x=CIRCLE_CENTER_X,
    start_y=CIRCLE_CENTER_Y,
    end_x=CIRCLE_CENTER_X + 0.5 * RAY_RADIUS,
    end_y=CIRCLE_CENTER_Y - 0.5 * RAY_RADIUS,
    color=COLOR_SUN,
    line_width=RAY_WIDTH,
)
arcade.draw_line(
    start_x=CIRCLE_CENTER_X,
    start_y=CIRCLE_CENTER_Y,
    end_x=CIRCLE_CENTER_X - 0.5 * RAY_RADIUS,
    end_y=CIRCLE_CENTER_Y + 0.5 * RAY_RADIUS,
    color=COLOR_SUN,
    line_width=RAY_WIDTH,
)

# Add some text
arcade.draw_text(
    text="Arbor Day - Plant a Tree!",
    start_x=150,
    start_y=230,
    color=arcade.csscolor.BLACK,
    font_size=24,
)

# Finish drawing
arcade.finish_render()

# Run the commands and keep the window open.
arcade.run()
