import pygame
from settings import Settings
import game_functions as gf
from hand import Hand
from pygame.sprite import Group
from game_stats import GameStats

def run_game():     # Initialise game and create a screen object.
    pygame.init()   # Initialises background settings for Pygame.
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    hands = Hand(ai_settings, screen)      # Make a hand.
    balls = Group()

    gf.create_ball(ai_settings, screen, balls)


    while True:  # Start the main loop for the game.
        gf.check_events(ai_settings, screen, hands)

        if stats.game_active:
            hands.update()
            gf.update_ball(ai_settings, screen, balls, hands, stats)

        gf.update_screen(ai_settings, screen, hands, balls)

run_game()
