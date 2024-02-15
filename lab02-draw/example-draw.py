"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.BONE)

# Get ready to draw
arcade.start_render()
#Cara
arcade.draw_circle_filled(360, 300, 280, arcade.color.AIR_SUPERIORITY_BLUE)
arcade.draw_circle_outline(360, 300, 280, arcade.color.BLACK, 5)
arcade.draw_circle_filled(360, 260, 240, arcade.color.ALMOND)
arcade.draw_circle_outline(360, 260, 240, arcade.color.BLACK, 5)

#ojos
arcade.draw_ellipse_filled(430, 490, 130, 150, arcade.color.ALMOND)
arcade.draw_ellipse_filled(300, 490, 130, 150, arcade.color.ALMOND)
arcade.draw_ellipse_outline(300, 490, 130, 150, arcade.color.BLACK, 5)
arcade.draw_ellipse_outline(430, 490, 130, 150, arcade.color.BLACK, 5)
arcade.draw_ellipse_filled(325, 490, 60, 80, arcade.color.BLACK)
arcade.draw_ellipse_filled(405, 490, 60, 80, arcade.color.BLACK)
arcade.draw_ellipse_filled(325, 490, 20, 40, arcade.color.ALMOND)
arcade.draw_ellipse_filled(405, 490, 20, 40, arcade.color.ALMOND)

#Boca
arcade.draw_arc_filled(365, 290, 300, 400, arcade.color.AUBURN, 180, 360)
arcade.draw_arc_outline(365, 290, 300, 400, arcade.color.BLACK, 180, 360, 10)
arcade.draw_line(210, 290, 520, 290, arcade.color.BLACK, 5)
arcade.draw_ellipse_filled(365, 130, 120, 80, arcade.color.FALU_RED)
arcade.draw_ellipse_filled(340, 170, 160, 140, arcade.color.FALU_RED)
arcade.draw_ellipse_filled(395, 170, 160, 140, arcade.color.FALU_RED)

#Bigotes
arcade.draw_line(180, 300, 300, 330, arcade.color.BLACK, 3)
arcade.draw_line(180, 350, 300, 350, arcade.color.BLACK, 3)
arcade.draw_line(180, 400, 300, 370, arcade.color.BLACK, 3)
arcade.draw_line(425, 330, 545, 300, arcade.color.BLACK, 3)
arcade.draw_line(425, 350, 545, 350, arcade.color.BLACK, 3)
arcade.draw_line(425, 370, 545, 400, arcade.color.BLACK, 3)


#Nariz
arcade.draw_circle_filled(365, 390, 50, arcade.color.RED)
arcade.draw_circle_outline(365, 390, 50, arcade.color.BLACK, 5)
arcade.draw_arc_filled(365, 390, 50, 50, arcade.color.AUBURN, 225, 45)


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

