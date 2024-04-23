"""
Spaceshooter!

Description:
    A simple 2D space shooter game created using the Python Arcade library.
    In this game, the player controls a spaceship and must dodge and shoot asteroids
    to save the world.

Author:
    Markus Scherg
    markus.scherg@bs1-bt.de
"""
import arcade

from spaceshooter.game import Game


def main():
    """Main function"""
    window = Game(1920 , 1080, fullscreen=True)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()