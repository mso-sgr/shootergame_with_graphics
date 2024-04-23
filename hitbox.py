import arcade


class Hitbox:
    def __init__(self,x, y, r):
        self.center_x = x
        self.center_y = y
        self.radius = r

    def set_position(self, x,y):
        self.center_x = x
        self.center_y = y

    def collides_with(self, other):
        # TODO: check whether the two hitboxes collide
        pass

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.radius, arcade.color.BLUE)
