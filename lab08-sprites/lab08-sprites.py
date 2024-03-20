""" Sprite Sample Program """

import random
import arcade
import math

SPRITE_SCALING_PLAYER = 0.9
SPRITE_SCALING_CEREBRO = 0.15
SPRITE_SCALING_BOMBA = 0.3
MOVEMENT_SPEED = 5
CEREBRO_COUNT = 50
BOMBA_COUNT = 35


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Cerebro(arcade.Sprite):

    def __init__(self, scaling):
        """ Constructor. """
        super().__init__("cerebro.png", scaling)

        self.circle_angle = 0
        self.circle_radius = 0
        self.circle_speed = 0.008
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        """ Update the cerebro's position. """
        self.center_x = self.circle_radius * math.sin(self.circle_angle) + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) + self.circle_center_y
        self.circle_angle += self.circle_speed
class Bomba(arcade.Sprite):

    def __init__(self, scaling):
        """ Constructor. """
        super().__init__("bomba.png", scaling)

        self.circle_angle = 0
        self.circle_radius = 0
        self.circle_speed = 0.008
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):
        self.center_x = self.circle_radius * math.sin(self.circle_angle) + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) + self.circle_center_y
        self.circle_angle += self.circle_speed

class Player(arcade.Sprite):
    """ Player Class """

    def update(self):
        """ Move the player """
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.cerebro_list = None
        self.bomba_list = None
        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)
        self.background = arcade.load_texture(":resources:images/cybercity_background/foreground.png")

        self.background_music = arcade.load_sound("gta-san-andreas-f.mp3")
        arcade.play_sound(self.background_music, volume=0.9)
        self.sound_good = arcade.load_sound("mario-bros-woo-hoo.mp3")
        self.sound_bad = arcade.load_sound("choque.mp3")

    def setup(self):
        """ Set up the game and initialize the variables. """
        self.player_list = arcade.SpriteList()
        self.cerebro_list = arcade.SpriteList()
        self.bomba_list = arcade.SpriteList()
        self.score = 0

        self.player_sprite = Player("zombie_fall.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for _ in range(CEREBRO_COUNT):
            cerebro = Cerebro(SPRITE_SCALING_CEREBRO)
            cerebro.circle_center_x = random.randrange(SCREEN_WIDTH)
            cerebro.circle_center_y = random.randrange(SCREEN_HEIGHT)
            cerebro.circle_radius = random.randrange(10, 200)
            cerebro.circle_angle = random.random() * 2 * math.pi
            self.cerebro_list.append(cerebro)

        for _ in range(BOMBA_COUNT):
            bomba = Bomba(SPRITE_SCALING_BOMBA)
            bomba.circle_center_x = random.randrange(SCREEN_WIDTH)
            bomba.circle_center_y = random.randrange(SCREEN_HEIGHT)
            bomba.circle_radius = random.randrange(10, 200)
            bomba.circle_angle = random.random() * 2 * math.pi
            self.bomba_list.append(bomba)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        # Dibuja la imagen de fondo
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        self.cerebro_list.draw()
        self.bomba_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):
        """ Movement and game logic """
        self.cerebro_list.update()
        cerebro_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.cerebro_list)
        self.bomba_list.update()
        bomba_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bomba_list)

        for cerebro in cerebro_hit_list:
            cerebro.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.sound_good)
        for bomba in bomba_hit_list:
            bomba.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.sound_bad)

    def on_update(self, delta_time):
        """ Movement and game logic """
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
