import pygame

from game.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    GAME_TITLE
)


class Game:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()

        self.running = True


    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False


    def update(self):
        # Future systems:
        # - AI commanders
        # - unit movement
        # - combat
        # - morale
        pass


    def draw(self):
        self.screen.fill((40, 100, 40))

        pygame.display.flip()


    def run(self):

        while self.running:

            self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(FPS)


        pygame.quit()