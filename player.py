#new player class inherited from CircleShape
from circleshape import *
from constants import *
from shot import *
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.shots = pygame.sprite.Group()
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        self.screen = screen
        pygame.draw.polygon(self.screen, [255,255,255], self.triangle(), 2)
    
    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-(dt))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-(dt))
        if keys[pygame.K_SPACE]:
            if (self.timer == 0):
                self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position)
        velocity = pygame.Vector2(0,1)
        velocity = velocity.rotate(self.rotation)
        velocity = velocity * PLAYER_SHOOT_SPEED
        shot.velocity =velocity
        self.shots.add(shot)
        self.timer = PLAYER_SHOOT_COOLDOWN
