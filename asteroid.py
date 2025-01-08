#asteroid class, don't get hit
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen, [255,255,255], self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        if(self.radius <= ASTEROID_MIN_RADIUS):
            self.kill()
            return
        else:
            angle = random.uniform(20,50)
            vector1 = (self.velocity.rotate(angle)) * 1.2 
            vector2 = (self.velocity.rotate(-angle)) * 1.2
            new_radius = (self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = vector1
            new_asteroid_2.velocity = vector2
            for group in self.groups():
                group.add(new_asteroid_1)
                group.add(new_asteroid_2)
            self.kill()
        
