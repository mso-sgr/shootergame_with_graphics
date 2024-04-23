import random
import arcade
import weapons

from spaceshooter.asteroids import BigAsteroid
from spaceshooter.spaceship import SpaceShip


class Game(arcade.Window):
    def __init__(self, screen_width: int, screen_height: int, screen_title="Spaceshooter!", fullscreen=False):
        super().__init__(screen_width, screen_height, screen_title, fullscreen)

        # Attributes of the Game class
        self.spaceship = None
        self.asteroids = []
        self.bullets = []
        self.powerups = []

        # some additional attributes
        self.min_asteroids = 3  # minimal number of asteroids to be in the game
        self.destroyed_asteroids = 0
        self.gameover = False

        # Dictionary to keep track of key states
        self.key_states = {}

        # Debugging
        self.debug = True

    def setup(self):
        """
            This method is called once before the game starts.
            It can be seen as an addition to the __init__ method.
            Call this method manually to restart the game.
        """
        # Initialize spaceship
        self.spaceship = SpaceShip(":resources:images/space_shooter/playerShip1_orange.png", 1, 400, 200)
        self.spaceship.set_position(self.width / 2, self.spaceship.height)
        self.spaceship.weapon = weapons.WEAPON_DEFAULT

        self.destroyed_asteroids = 0
        self.asteroids = []
        self.bullets = []
        self.powerups = []

        self.gameover = False

    def update(self, delta_time: float):
        # Called each frame

        if self.gameover:
            return

        # Move spaceship if LEFT or RIGHT is pressed
        if self.is_key_pressed(arcade.key.RIGHT):
            self.spaceship.move(delta_time, 0)
        elif self.is_key_pressed(arcade.key.LEFT):
            self.spaceship.move(-delta_time, 0)

        # Move Asteroids
        for asteroid in self.asteroids:
            asteroid.move(0, -delta_time)

        # Move bullets
        for bullet in self.bullets:
            bullet.move(0, delta_time)

        # Handle Collisions
        self.handle_collisions()

        # Remove Asteroids that are out of screen
        new_asteroids = [asteroid for asteroid in self.asteroids if asteroid.center_y < 0]
        if len(new_asteroids) != 0:
            print(f"Gameover - Score: {self.destroyed_asteroids}")
            self.gameover = True

        # spawn new asteroid if there are less than 3
        if len(self.asteroids) < self.min_asteroids:
            self.spawn_asteroid()

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw spaceship, asteroids and bullets
        self.spaceship.draw()
        for asteroid in self.asteroids:
            asteroid.draw()
        for bullet in self.bullets:
            bullet.draw()

        # Draw Hitboxes if in debug mode
        if self.debug:
            self.spaceship.hitbox.draw()

            for a in self.asteroids:
                a.hitbox.draw()

            for b in self.bullets:
                b.hitbox.draw()

    def on_key_press(self, key, modifiers):
        self.key_states[key] = True

        # CTRL either fires the current weapon or restarts the game
        if key == arcade.key.LCTRL or key == arcade.key.RCTRL:
            if not self.gameover:
                self.bullets.append(self.spaceship.shoot())
            else:
                self.setup()

        # Escape key exits the game
        if key == arcade.key.ESCAPE:
            self.close()

    def on_key_release(self, key, modifiers):
        self.key_states[key] = False

    def is_key_pressed(self, key):
        return self.key_states.get(key, False)

    def spawn_asteroid(self):
        x = random.randint(0, self.width)
        y = random.randint(self.height, self.height + 350)
        t = random.randint(1, 3)

        if t < 3:
            # Spawn big asteroid
            hp = random.randint(20, 200)
            speed = random.randint(40, 180)
            asteroid = BigAsteroid(":resources:images/space_shooter/meteorGrey_big2.png", 1, speed, 30, hp)
            asteroid.set_position(x, y)
            self.asteroids.append(asteroid)
        else:
            # Spawn small asteroid
            hp = random.randint(20, 40)
            speed = random.randint(80, 200)
            asteroid = BigAsteroid(":resources:images/space_shooter/meteorGrey_med1.png", 1, speed, 30, hp)
            asteroid.set_position(x, y)
            self.asteroids.append(asteroid)

    def handle_collisions(self):
        colliding_asteroids = []
        colliding_bullets = []

        # TODO: check if collisions occur and act accordingly

        self.asteroids = [asteroid for asteroid in self.asteroids if asteroid not in colliding_asteroids]
        self.bullets = [bullet for bullet in self.bullets if bullet not in colliding_bullets]
