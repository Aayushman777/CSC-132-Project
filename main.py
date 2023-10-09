import pygame, sys
from object import *
from frog import *

# main game
class Game:
    def __init__(self, screen_dimensions, screen_caption, screen_color):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_mode(screen_dimensions)
        pygame.display.set_caption(screen_caption)
        self.screen_color = screen_color
        self.DISPLAY = pygame.display.get_surface()

        # sprite group (stores created sprites and puts them on screen)
        self.object_group = pygame.sprite.Group() # grouping background objects/sprites
        self.car_group = pygame.sprite.Group() # grouping cars
        self.river_group = pygame.sprite.Group() # grouping logs and turtles
        self.frog_group = pygame.sprite.Group() # grouping frog variations

        self.all_groups = [self.object_group, self.car_group, self.river_group, self.frog_group]

        self.assetSetup()

    # display assets
    def assetSetup(self):
        Object((0,0), (672,768), "assets/background.png", self.object_group)
        
        for x in range(14):
            Object((x*48, 384), (48,48), "assets/grass/purple.png", self.object_group) # purple grass dividing river and road
            Object((x*48, 672), (48,48), "assets/grass/purple.png", self.object_group) # purple grass stretching along starting row
        for x in range(28):
            Object((x*24, 72), (24, 72), "assets/grass/green.png", self.object_group)

        self.frog = Frog((336,672), (48,48), "assets/frog/frog_up.png", self.frog_group)


    # main game loop
    def run(self):
        while True:
            self.clock.tick(60) # frame rate

            self.frog.keyups = []          
            for event in pygame.event.get():                
                if event.type == pygame.QUIT:   # close the game when quit
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    self.frog.keyups.append(event.key)

            # update sprites
            for group in self.all_groups:
                for sprite in group:
                    sprite.update()            ################ISSUE###########   for loop has weird coloring in VS Code for some reason
                    
                group.draw(self.DISPLAY) # draw updated group on screen
            pygame.display.update()

game = Game((672,768), "Frogger", (0,0,0)) # dimensions = 14x16 tiles with each tile 48x48 pixels
game.run()
