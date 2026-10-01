"""
GameEngine: owns the player, coins, obstacles, lives, and round timer.
"""

import random
import pygame

from game.player import Player
from game.coin import Coin
from game.collection import check_collection
from game.renderer import WIDTH, HEIGHT


NUM_COINS = 6

COIN_TYPES = [
    (1, (184, 115, 51)),   # Bronze
    (3, (192, 192, 192)),  # Silver
    (5, (230, 190, 60)),   # Gold
]


class GameEngine:
    def __init__(self):
        self.round_duration = 30
        self.reset_round()

    def reset_round(self):
        self.player = Player(
            x=WIDTH / 2,
            y=HEIGHT / 2
        )

        self.coins = [
            self._random_coin()
            for _ in range(NUM_COINS)
        ]

        self.score = 0
        self.lives = 3

        self.round_start_time = pygame.time.get_ticks()
        self.remaining_time = self.round_duration

        self.round_over = False

        self.safe_x = WIDTH / 2
        self.safe_y = HEIGHT / 2

        self.collision_cooldown = 0

        self.obstacles = [
            pygame.Rect(150, 120, 120, 30),
            pygame.Rect(430, 200, 120, 30),
            pygame.Rect(250, 350, 160, 30),
        ]

    def _random_coin(self):
        x = random.randint(30, WIDTH - 30)
        y = random.randint(30, HEIGHT - 30)

        value, color = random.choice(COIN_TYPES)

        return Coin(
            x=x,
            y=y,
            radius=12,
            value=value,
            color=color,
        )

    def handle_input(self, keys_pressed):
        if self.round_over:
            return

        dx = dy = 0

        if keys_pressed[pygame.K_UP]:
            dy -= self.player.speed

        if keys_pressed[pygame.K_DOWN]:
            dy += self.player.speed

        if keys_pressed[pygame.K_LEFT]:
            dx -= self.player.speed

        if keys_pressed[pygame.K_RIGHT]:
            dx += self.player.speed

        self.player.move(dx, dy, WIDTH, HEIGHT)

    def update(self):
        if self.round_over:
            return

        # Update timer
        elapsed_time = (
            pygame.time.get_ticks() - self.round_start_time
        ) / 1000

        self.remaining_time = max(
            0,
            self.round_duration - elapsed_time
        )

        # End round when timer reaches zero
        if self.remaining_time <= 0:
            self.remaining_time = 0
            self.round_over = True
            return

        # Collect coins
        collected = check_collection(
            self.player,
            self.coins
        )

        for coin in collected:
            self.score += coin.value
            self.coins.remove(coin)

        # Reduce collision cooldown
        if self.collision_cooldown > 0:
            self.collision_cooldown -= 1

        # Check obstacle collision
        player_rect = self.player.get_rect()

        if self.collision_cooldown == 0:
            for obstacle in self.obstacles:
                if player_rect.colliderect(obstacle):

                    self.lives -= 1

                    self.player.reset_position(
                        self.safe_x,
                        self.safe_y
                    )

                    self.collision_cooldown = 30

                    break

        # End round when lives reach zero
        if self.lives <= 0:
            self.lives = 0
            self.round_over = True

    def draw(self, surface, font):
        from game import renderer

        renderer.draw_scene(
            surface,
            self.player,
            self.coins,
            self.obstacles,
            self.lives,
            self.remaining_time,
            self.round_over,
            font
        )

        renderer.draw_text(
            surface,
            font,
            f"Score: {self.score}",
            (10, 10)
        )