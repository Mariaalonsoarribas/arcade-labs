import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_grass():
    """ Draw the ground """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.AIR_SUPERIORITY_BLUE)


def draw_snow_person(x, y):
    """ Draw a snow person """

    # Draw a point at x, y for reference
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # coche
    arcade.draw_rectangle_filled(x - 15, 60 + y, 300,100,  arcade.color.RED_BROWN)
    arcade.draw_rectangle_filled(x + 0, 150+y, 200,100,  arcade.color.RED_BROWN)

    # ruedas
    arcade.draw_circle_filled(x - 80, 20 + y, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 80, 20 + y, 50, arcade.color.BLACK)

    # ventanas
    arcade.draw_rectangle_filled(x - 50, 150 + y, 80, 60, arcade.color.AIR_FORCE_BLUE)
    arcade.draw_rectangle_filled(x + 50, 150 + y, 80, 60, arcade.color.AIR_FORCE_BLUE)

def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_grass()
    draw_snow_person(on_draw.snow_person1_x, 140)
    draw_snow_person(450, 180)

    # Add one to the x value, making the snow person move right
    # Negative numbers move left. Larger numbers move faster.
    on_draw.snow_person1_x += 5


# Create a value that our on_draw.snow_person1_x will start at.
on_draw.snow_person1_x = 150


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.DARK_BLUE)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()