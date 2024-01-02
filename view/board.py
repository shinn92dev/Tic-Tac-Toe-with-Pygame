import pygame as pg
import sys
from random import randint

WINDOW_SIZE = 600


class TictactoeTool:
    def __init__(self, game):
        self.game = game
        self.board_image = self.get_image(path="../images/board.png", res=[WINDOW_SIZE] * 2)

    def draw(self):
        self.game.screen.blit(self.board_image, (0, 0))

    @staticmethod
    def get_image(path, res):
        img = pg.image.load(path)
        return pg.transform.smoothscale(img, res)

    def run(self):
        self.draw()


class TictactoeWindow:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode([WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.tic_tac_toe = TictactoeTool(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.tic_tac_toe.run()
            self.check_events()
            pg.display.update()
            self.clock.tick(60)


if __name__ == "__main__":
    game = TictactoeWindow()
    game.run()
