import pygame
from pygame.locals import *
import sys

SCREEN = Rect(0, 0, 400, 400)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, vx, vy, angle=0):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(filename).convert_alpha()
        if angle != 0:
            self.image = pygame.transform.rotate(self.image, angle)
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect = Rect(x, y, w, h)
        self.vx = vx
        self.vy = vy
        self.angle = angle

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.left < 0 or self.rect.right > SCREEN.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCREEN.height:
            self.vy = -self.vy
        self.rect = self.rect.clamp(SCREEN)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    group = pygame.sprite.RenderUpdates()
    Sprite.containers = group
    player = Sprite("pic/mytank.png", 200, 200, 2, 0, 0)
    enemy = Sprite("pic/enetank.png", 200, 200, 0, 2, 0)
    enemy1 = Sprite("pic/enetank1.png", 200, 200, 2, 2, 10)
    clock = pygame.time.Clock()

    bg = pygame.Surface(SCREEN.size)
    bg.fill((0, 120,0))
    screen.blit(bg, (0, 0))
    pygame.display.update()

    while(1):
        clock.tick(30)
        group.clear(screen, bg)
        group.update()
        dirty_rects = group.draw(screen)
        pygame.display.update(dirty_rects)

        # screen.fill((0, 126, 0))
        # player.update()
        # enemy.update()
        # enemy1.update()

        # player.draw(screen)
        # enemy.draw(screen)
        # enemy1.draw(screen)
            
        # pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()


