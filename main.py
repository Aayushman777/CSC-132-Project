import pygame, sys


# game class that takes in all screen variables and initializes them
class Game:
    def __init__(self, screen_dimensions, screen_caption, screen_color):
        pygame.init()
        pygame.display.set_mode(screen_dimensions)
        pygame.display.set_caption(screen_caption)

        self.screen_color = screen_color
        self.display = pygame.display.get_surface()

        # sprite group (stores created sprites and puts them on screen)
        self.object_group = pygame.sprite.Group() # grouping background objects/sprites
        self.car_group = pygame.sprite.Group() # grouping cars
        self.river_group = pygame.sprite.Group() # grouping logs and turtles
        self.frog_group = pygame.sprite.Group() # grouping frog variations

        self.all_groups = [self.object_group, self.car_group, self.river_group, self.frog_group]

    # main game loop
    def run(self):
        while True:
            self.display.fill(self.screen_color) # set background color

            # close the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() # JUST A PRECAUTION MAKING SURE THE PROGRAM CLOSES

            # update sprites
            for group in self.all_groups:
                for sprite in group:
                    sprite.update()             ################ISSUE###########   for loop not working for some reason
                    
                group.draw(self.display) # draw group on screen

game = Game((700,800), "Frogger", (0,0,0)) # dimensions = 14x16 tiles with each tile 50x50 pixels
game.run
