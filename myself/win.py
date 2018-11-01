import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Test")
    font = pygame.font.Font(None, 55)

    while (1):
        screen.fill((255,0,0))
        pygame.draw.line(screen, (0,95,0), (0,0), (80,80), 10)
        pygame.draw.rect(screen, (0,80,0), Rect(10,10,80,50))
        pygame.draw.ellipse(screen, (0,100,0), (200,150,10,80))
        text = font.render("TEST", True, (255,255,255))
        screen.blit(text, [200, 150])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()