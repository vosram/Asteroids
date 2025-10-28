from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        # randomize the angle of split
        random_angle = random.uniform(20.0, 50.0)

        vel_vector1 = self.velocity.rotate(random_angle)
        vel_vector2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_astroid1.velocity = vel_vector1 * 1.2
        new_astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_astroid2.velocity = vel_vector2 * 1.2
        

        