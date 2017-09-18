import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button


from game_functions import check_event, update_game, update_bullets, create_fleet, update_aliens
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien invation')

    ship = Ship(ai_settings, screen)

    bullets = Group()
    aliens = Group()
    create_fleet(ai_settings, screen, ship, aliens)

    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, "Play")

    while True:
        check_event(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            update_bullets(ai_settings, screen, ship, aliens, bullets)
            update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        update_game(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()