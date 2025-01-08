import sys
from constants import *
from circleshape import *
from player import *
from asteroidfield import *
from shot import *
import pygame

def main():
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # shots = pygame.sprite.Group()
    pygame.init()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #set fps
    clock = pygame.time.Clock()
    dt = 0 
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)
    #while loop for game time
    while(True):
        #prevent problems with exiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #set background here
        pygame.Surface.fill(screen, (0,0,0))
        # UPDATABLE player.update(dt)
        player.shots.update(dt)
        for shot in player.shots:
            shot.draw(screen)
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if(item.collision(player)):
                print("Game Over!")
                sys.exit()
            for shot in player.shots:
                if(item.collision(shot)):
                    item.split()
                    shot.kill()
        # DRAWABLE player.draw(screen)
        for item in drawable:
            item.draw(screen)
        pygame.display.update()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
