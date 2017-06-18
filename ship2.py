import pygame

class Ship2():
    
    def __init__(self, screen):
        #initialize screen and ship starting position
        self.screen = screen
        
        #load ship image and its rect.
        self.image = pygame.image.load('images/frozenman.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each ship bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        #draw ship at current location
        self.screen.blit(self.image, self.rect)
