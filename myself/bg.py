import pygame
from pygame.locals import *
import sys
def main():
    (w,h) = (400,400)
    (x,y) = (w//2, h//2)
    pygame.init()
    pygame.display.set_mode((w, h), 0, 32)#FULLSCREEN)
    screen = pygame.display.get_surface()
    # bg = pygame.image.load("pic/s.jpg").convert_alpha()
    # player = pygame.image.load("pic/standing.png").convert_alpha()
    # rect_bg = bg.get_rect()
    # rect_player = player.get_rect()
    # rect_player.center = (300, 100)

    while (1):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            x-=1
        if pressed_key[K_RIGHT]:
            x+=1
        if pressed_key[K_UP]:
            y-=1
        if pressed_key[K_DOWN]:
            y+=1
        
        pygame.display.update()
        pygame.time.wait(30)
        screen.fill((0,20,0,0))
        # screen.blit(bg, rect_bg)
        # screen.blit(player, rect_player)

        pygame.draw.circle(screen, (0, 200, 0), (x, y), 20)
 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                if event.key == K_LEFT:
                    x -= 10
                if event.key == K_RIGHT:
                    x += 10
                if event.key == K_UP:
                    y -= 10
                if event.key == K_DOWN:
                    y += 10
                

if __name__ == "__main__":
    main()
                    