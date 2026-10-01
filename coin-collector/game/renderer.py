"""
renderer: all pygame drawing lives here, kept separate from game logic.
"""

import pygame

WIDTH, HEIGHT = 700, 500
WINDOW_SIZE = (WIDTH, HEIGHT)

COLOR_BG = (35, 45, 35)
COLOR_PLAYER = (80, 180, 255)
COLOR_TEXT = (255, 255, 255)
COLOR_OBSTACLE = (200, 70, 70)


def draw_scene(surface, player, coins, obstacles=None, lives=3):
    surface.fill(COLOR_BG)

    # Draw coins
    for coin in coins:
        pygame.draw.circle(
            surface,
            coin.color,
            (int(coin.x), int(coin.y)),
            coin.radius
        )

    # Draw obstacles
    if obstacles:
        for obstacle in obstacles:
            pygame.draw.rect(
                surface,
                COLOR_OBSTACLE,
                obstacle,
                border_radius=5
            )

    # Draw player
    pygame.draw.rect(
        surface,
        COLOR_PLAYER,
        player.get_rect(),
        border_radius=4
    )

    # Draw lives
    draw_text(
        surface,
        pygame.font.Font(None, 28),
        f"Lives: {lives}",
        (10, 40)
    )


def draw_text(surface, font, text, pos, color=COLOR_TEXT):
    surface.blit(font.render(text, True, color), pos)


def draw_banner(surface, font, text):
    surf = font.render(text, True, (255, 220, 80))
    rect = surf.get_rect(
        center=(
            surface.get_width() // 2,
            surface.get_height() // 2
        )
    )
    surface.blit(surf, rect)