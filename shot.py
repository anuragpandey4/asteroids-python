from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH   
import pygame

class Shot(CircleShape):
    def __init__(self,x,y,radius=SHOT_RADIUS):
        super().__init__(x,y,radius)

    def draw(self,surface):
        pygame.draw.circle(surface, "white", (int(self.position.x), int(self.position.y)), int(self.radius), LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt         