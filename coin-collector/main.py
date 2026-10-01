"""
Coin Collector

Run with: python main.py

Controls:
Arrow keys to move.
R to start a new round after the round ends.
"""

import pygame

from game.game_engine import GameEngine
from game.renderer import WINDOW_SIZE


def main():
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Coin Collector")

    clock = pygame.time.Clock()

    font = pygame.font.SysFont(
        "consolas",
        22
    )

    engine = GameEngine()

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            # Restart round
            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_r
                and engine.round_over
            ):
                engine.reset_round()

        keys = pygame.key.get_pressed()

        engine.handle_input(keys)

        engine.update()

        engine.draw(
            screen,
            font
        )

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()