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

# Finish drawing
arcade.finish_render()

# Run the commands and keep the window open.
arcade.run()
