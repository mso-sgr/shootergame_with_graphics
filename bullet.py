import arcade

from spaceshooter.hitbox import Hitbox


class Bullet(arcade.Sprite):
    def __init__(self, image, scale, speed, damage):
        super().__init__(image, scale)

        # Initialize attributes
        self.speed = speed
        self.damage = damage

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
