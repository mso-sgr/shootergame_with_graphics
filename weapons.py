from bullet import Bullet


class Weapon:
    def __init__(self, reload_time):
        self.reload_time = reload_time

    def shoot(self, x, y):
        pass


class DefaultWeapon(Weapon):
    def __init__(self):
        super().__init__(0.5)

    def shoot(self, x, y):
        bullet = Bullet(":resources:images/space_shooter/laserRed01.png", 1, 400, 30)
        bullet.center_x = x
        bullet.center_y = y + 10
        return bullet


WEAPON_DEFAULT = DefaultWeapon()
