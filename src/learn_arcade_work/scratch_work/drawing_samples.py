"""
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
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

# Draw a tree stump on top of the grass
arcade.draw_lrtb_rectangle_filled(100, 120, 350, 300, arcade.csscolor.SIENNA)

# Draw a top on top of the tree
arcade.draw_circle_filled(110, 350, 30, arcade.csscolor.GREEN)

# Finish drawing
arcade.finish_render()

# Run the commands and keep the window open.
arcade.run()
