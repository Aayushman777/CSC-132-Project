import pygame
from object import *

class Frog(Object):
    def __init__(self, position, size, image, group):
        super().__init__(position, size, image, group)
        
        self.keyups = []

    def moveFrog(self):
        x = self.position[0]
        y = self.position[1]

        if pygame.K_UP in self.keyups:
            self.image_directory = "assets/frog/frog_up.png"
            y -= 48

        if pygame.K_DOWN in self.keyups:
            self.image_directory = "assets/frog/frog_down.png"
            y += 48

        if pygame.K_LEFT in self.keyups:
            self.image_directory = "assets/frog/frog_left.png"
            x -= 48

        if pygame.K_RIGHT in self.keyups:
            self.image_directory = "assets/frog/frog_right.png"
            x += 48

        if x <= -48 or x > 48*14 or y > 48*16:
            self.killFrog()
            return

        self.position = (x,y)

    def killFrog(self):
        self.position = (336, 672)
        self.image_directory = "assets/frog/frog_up.png"
        self.setImage()

    def update(self):
        self.setImage()
        self.moveFrog()
