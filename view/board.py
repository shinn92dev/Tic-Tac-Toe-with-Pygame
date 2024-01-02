import pygame as pg
import sys
from random import randint

WINDOW_SIZE = 600


class TictactoeWindow:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            pg.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = TictactoeWindow()
    game.run()