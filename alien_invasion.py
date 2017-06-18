import pygame
from settings import Settings
from ship import Ship
from ship2 import Ship2
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    #initiate game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #make a ship
    ship = Ship(ai_settings, screen)
    #make a group to store bullets
    bullets = Group()
    #group of aliens
    aliens = Group()
    #make an alien
    alien = Alien(ai_settings, screen)
    
    gf.create_fleet(ai_settings, screen, ship, aliens)
    

    
    #main game loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
run_game()
            
