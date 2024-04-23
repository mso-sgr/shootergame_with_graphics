import math

import arcade

from spaceshooter.hitbox import Hitbox


class Asteroid(arcade.Sprite):
    def __init__(self, image, scale, speed, damage, hp):
        if type(self) is Asteroid:
            raise Exception("Asteroid is an abstract class and cannot be instantiated directly.")
        super().__init__(image, scale)

        # Initialize attributes of class Asteroid
        self.speed = speed
        self.damage = damage
        self.hp_max = hp
        self.hp_current = hp

        # Initialize hitbox
        self.hitbox = Hitbox(self.center_x, self.center_y, 0.7 * self.width / 2)

    def set_position(self, x, y):
        """Sets the position of the asteroid"""
        self.center_x = x
        self.center_y = y

        self.hitbox.set_position(self.center_x, self.center_y)

    def move(self, x, y):
        """Adjusts the position of the asteroid"""
        self.center_x += self.speed * x
        self.center_y += self.speed * y

        self.hitbox.set_position(self.center_x, self.center_y)


class BigAsteroid(Asteroid):
    def __init__(self, image, scale, speed, damage, hp):
        super().__init__(image, scale, speed, damage, hp)


class SmallAsteroid(Asteroid):
    def __init__(self, image, scale, speed, damage, hp):
        super().__init__(image, scale, speed, damage, hp)
