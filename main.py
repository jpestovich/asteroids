from constants import *
from circleshape import *
from player import *
import pygame

def main():
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    pygame.init()
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
        player.update(dt)
        player.draw(screen)
        pygame.display.update()
        dt = clock.tick(60) / 1000
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()i
