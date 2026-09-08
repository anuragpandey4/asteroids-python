import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        
    def draw(self,surface): 
        pygame.draw.circle(surface, "white", (int(self.position.x), int(self.position.y)), int(self.radius), LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # 1. Generate random angle between 20 and 50
        angle = random.uniform(20, 50)

        # 2. Rotate velocity in both directions
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)

        # 3. Compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # 4. Spawn 2 new asteroids at current position
        ast1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_radius)

        # 5. Scale speeds up by 1.2
        ast1.velocity = vel1 * 1.2
        ast2.velocity = vel2 * 1.2

            
        