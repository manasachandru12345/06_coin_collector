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


def draw_scene(
    surface,
    player,
    coins,
    obstacles=None,
    lives=3,
    remaining_time=30,
    round_over=False,
    font=None
):
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
    if font:
        draw_text(
            surface,
            font,
            f"Lives: {lives}",
            (10, 40)
        )

        # Draw timer
        draw_text(
            surface,
            font,
            f"Time: {int(remaining_time)}",
            (10, 70)
        )

        # Draw round-over information
        if round_over:
            draw_round_over(
                surface,
                font,
                lives
            )


def draw_text(
    surface,
    font,
    text,
    pos,
    color=COLOR_TEXT
):
    surface.blit(
        font.render(text, True, color),
        pos
    )


def draw_banner(surface, font, text):
    surf = font.render(
        text,
        True,
        (255, 220, 80)
    )

    rect = surf.get_rect(
        center=(
            surface.get_width() // 2,
            surface.get_height() // 2
        )
    )

    surface.blit(surf, rect)


def draw_round_over(surface, font, lives):
    if lives <= 0:
        title = "GAME OVER"
    else:
        title = "TIME UP!"

    title_surf = font.render(
        title,
        True,
        (255, 220, 80)
    )

    title_rect = title_surf.get_rect(
        center=(
            surface.get_width() // 2,
            surface.get_height() // 2 - 30
        )
    )

    surface.blit(title_surf, title_rect)

    restart_surf = font.render(
        "Press R to start a new round",
        True,
        (255, 255, 255)
    )

    restart_rect = restart_surf.get_rect(
        center=(
            surface.get_width() // 2,
            surface.get_height() // 2 + 20
        )
    )

    surface.blit(restart_surf, restart_rect)