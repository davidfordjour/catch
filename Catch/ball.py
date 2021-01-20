import pygame
from pygame.sprite import Sprite
from random import randint


class Ball(Sprite):
    """A class to represent a ball."""

    def __init__(self, ai_settings, screen):
        """Initialise the alien and set its starting position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ball image and set its rect attribute.
        self.image = pygame.image.load('images/ball.bmp')
        self.rect = self.image.get_rect()

        # Start each new ball at a random position at the top of the screen.
        self.rect.x = randint(0, 1200)
        self.rect.y = self.rect.height

        # Store the ball's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        """"Make the ball drop."""

        self.y += self.ai_settings.ball_drop_factor
        self.rect.y = self.y



    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)