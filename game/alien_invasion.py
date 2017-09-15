import pygame
from settings import Settings
from ship import Ship
from game_stats import GameStats

from game_functions import check_event, update_game, update_bullets, create_fleet, update_aliens
from pygame.sprite import Group

def run_game():
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption('Alien invation')

    ship = Ship(ai_setting, screen)

    bullets = Group()
    aliens = Group()
    create_fleet(ai_setting, screen, ship, aliens)

    stats = GameStats(ai_setting)
    while True:
        check_event(ai_setting, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            update_bullets(ai_setting, screen, ship, aliens, bullets)
            update_aliens(ai_setting, stats, screen, ship, aliens, bullets)
        update_game(ai_setting, screen, ship, aliens, bullets)

run_game()