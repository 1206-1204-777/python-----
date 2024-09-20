import pygame
import sys
import math

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GOLD = (255,216,192)
SILVER = (192,192,192)
COPPER = (192,112,46)

def main():
    pygame.init()
    pygame.didsplay.set_caption("図形")
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time,clock()
    
    tmr = 0
    
    while True:
        tmr += 1
        for event in pygame.event_get():
            if event.type == pygame.QUIET:
                pygame.quit()
                sys.exit()
                
        screen.fill(BLACK)
        
        pygame.draw.line(screen,RED,[0,0],[100,200],10)
        pygame.draw.lines(screen,BLUE,False,[[50,300],[150,400],[50,500]])


if __name__ == '__main__':
    main()