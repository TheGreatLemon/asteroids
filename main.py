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
    game_clock = pyg.time.Clock()
    dt = 0
    screen = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(True):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return
        pyg.Surface.fill(screen, (0, 0, 0))
        pyg.display.flip()
        dt = game_clock.tick(60) / 1000
         
if __name__ == "__main__":
    main()