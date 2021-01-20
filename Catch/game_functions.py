import sys
import pygame
from ball import Ball
from time import sleep


def check_keydown_events(event, ai_settings, screen, hand):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        hand.moving_right = True
    elif event.key == pygame.K_LEFT:
        hand.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, hand):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, hand)




        elif event.type == pygame.KEYUP:
            check_keyup_events(event, hand)


def update_screen(ai_settings, screen, hands, balls):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_colour)
    hands.blitme()
    balls.draw(screen)

    pygame.display.flip()   # Make the most recently drawn screen visible


def create_ball(ai_settings, screen, balls):
    """Create a ball and a hand"""
    ball = Ball(ai_settings, screen)
    ball.rect.x = ball.x
    ball.rect.y = ball.rect.y
    balls.add(ball)

def ball_missed(ai_settings, stats, screen, hands, balls):
    """Respond to ball being missed."""


    if stats.balls_left > 0:
        # Decrement balls_left.
        stats.balls_left -= 1

        # empty list of balls.
        balls.empty()

        create_ball(ai_settings, screen, balls) # Create a new ball and center
        hands.center_hands()

        # Pause.
        sleep(1)

    else:
        stats.game_active = False


def check_ball_bottom(ai_settings, stats, screen, balls, hands):
    """Check if any balls have reached the bottom of the screen."""
    screen_rect = screen.get_rect()

    for ball in balls.sprites():
        if ball.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ball is missed.
            ball_missed(ai_settings, stats, screen, hands, balls)
            break







def update_ball(ai_settings, screen, balls, hands, stats):
    """Update position of ball"""
    balls.update()

    check_catches(ai_settings, screen, balls, hands)
    check_ball_bottom(ai_settings, stats, screen, balls, hands)


def check_catches(ai_settings, screen, balls, hands):
    """Check if the ball has been caught."""

    if pygame.sprite.spritecollideany(hands, balls):
        balls.empty()

        if len(balls) == 0:
            create_ball(ai_settings, screen, balls)



