import math
import arcade
import weapons

from hitbox import Hitbox


class SpaceShip(arcade.Sprite):
    def __init__(self, image, scale, speed, hp_max):
        super().__init__(image, scale)

        # Initialize attributes
        self.speed = speed
        self.hp_max = hp_max
        self.hp_current = hp_max
        self.weapon = weapons.WEAPON_DEFAULT

        # Initialize hitbox
        self.hitbox = Hitbox(self.center_x, self.center_y, 0.7 * self.width / 2)

    def set_position(self, x, y):
        self.center_x = x
        self.center_y = y

        self.hitbox.set_position(self.center_x, self.center_y)

    def move(self, x, y):
        self.center_x += self.speed * x
        self.center_y += self.speed * y

        self.hitbox.set_position(self.center_x, self.center_y)

    def shoot(self):
        return self.weapon.shoot(self.center_x, self.center_y)
