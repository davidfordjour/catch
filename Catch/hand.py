import pygame

class Hand():

    def __init__(self, ai_settings, screen):
        """Initialise the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/hand.bmp')   # Load the hand and its rect.
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx  # Start each new ship at the bottom of the screen.
        self.rect.bottom = self.screen_rect.bottom    # Bottom of hand equals the bottom of the screen.

        self.centerx = float(self.rect.centerx)  # Store a decimal value for the ship's center
        self.centery = float(self.rect.centery)

        self.moving_right = False   # Movement flag
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.hand_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.hand_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.hand_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.hand_speed_factor

        self.rect.centerx = self.centerx    # Update rect object from self.center.
        self.rect.centery = self.centery


    def blitme(self):
        """Draw the hand at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_hands(self):
        """Center the hand on the screen."""
        self.center = self.screen_rect.centerx