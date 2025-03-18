# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame as pyg
from constants import * 

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pyg.init()
    screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pyg.Surface.fill(screen, (0, 0, 0))
        pyg.display.flip()
         
if __name__ == "__main__":
    main()