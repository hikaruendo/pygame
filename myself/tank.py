import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((853, 480))
SCREEN = Rect(0,0,853,480)
pygame.display.set_caption("tank")

bg = pygame.image.load("pic/space.jpg")

clock = pygame.time.Clock()


class mytank(object):
    def __init__(self, filename, x, y, width, height):
        self.image = pygame.image.load(filename)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        if self.left:
            screen.blit(self.image, (self.x, self.y))
        elif self.right:
            screen.blit(self.image, (self.x, self.y))
        elif self.up:
            screen.blit(self.image, (self.x, self.y))
        elif self.down:
            screen.blit(self.image, (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def hit(self):
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('auch!', 1, (255,0,0))
        screen.blit(text, (self.x + 20, self.y + 20))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(1)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()

class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 9 * facing
        

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    

class enemy(object):
    def __init__(self, filename, x, y, vx, vy):
        self.image = pygame.image.load(filename).convert_alpha()
        self.x = x
        self.y = y
        w = self.image.get_width()
        h = self.image.get_height()
        self.rect = Rect(x, y, w, h)
        self.vx = vx
        self.vy = vy
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        self.health = 10
        self.visible = True

    def draw(self, screen):
        self.move()
        if self.visible:
            screen.blit(self.image, self.rect)

            pygame.draw.rect(screen, (255,0,0), (self.rect[0], self.rect[1]-20, 50, 10))
            pygame.draw.rect(screen, (0,128,0), (self.rect[0], self.rect[1]-20, 50-(5*(10-self.health)), 10))

            self.hitbox = (self.rect[0] + 17, self.rect[1] + 2, 31, 57)

    def move(self):
        self.rect.move_ip(self.vx, self.vy)
        if self.rect.top < 0 or self.rect.bottom > SCREEN.height:
            self.vy = -self.vy
        self.rect = self.rect.clamp(SCREEN)

    def hit(self):
        if self.health > 1:
            self.health -= 1
        else:
            self.visible = False

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

def redrawGameWindow():
    screen.blit(bg, (0,0))
    me.draw(screen)
    you.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    group.clear(screen, bg)
    group.update()
    group.draw(screen)
    pygame.display.update()
    # dirty_rects = group.draw(screen)
    # pygame.display.update(dirty_rects)

    
# mainloop
font = pygame.font.SysFont("comicsans", 30, True)
me = mytank("pic/mytank.png", 20, 400, 81, 64)
you = enemy("pic/enetank.png", 750, 200, 0, 10)
shootLoop = 0
bullets = []
    
group = pygame.sprite.RenderUpdates()
Sprite.containers = group
rock = Sprite("pic/rock.png", 200, 200, 1, 3, 30)
rock1 = Sprite("pic/rock1.png", 200, 200, 1, 2, 60)
rock2 = Sprite("pic/rock2.png", 200, 200, 1, 1, 10)
clock = pygame.time.Clock()

while(1):
    clock.tick(30)
    
    if me.hitbox[1] < rock.rect[1] + rock.rect[3] and me.hitbox[1] +me.hitbox[3] > rock.rect[1]:
        if me.hitbox[0] + me.hitbox[2] > rock.rect[0] and me.hitbox[0] < rock.rect[0] + rock.rect[2]:
            me.hit()

    if me.hitbox[1] < rock1.rect[1] + rock1.rect[3] and me.hitbox[1] +me.hitbox[3] > rock1.rect[1]:
        if me.hitbox[0] + me.hitbox[2] > rock1.rect[0] and me.hitbox[0] < rock1.rect[0] + rock1.rect[2]:
            me.hit()

    if me.hitbox[1] < rock2.rect[1] + rock2.rect[3] and me.hitbox[1] +me.hitbox[3] > rock2.rect[1]:
        if me.hitbox[0] + me.hitbox[2] > rock2.rect[0] and me.hitbox[0] < rock2.rect[0] + rock2.rect[2]:
            me.hit()

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    for bullet in bullets:
        if bullet.y - bullet.radius < you.hitbox[1] + you.hitbox[3] and bullet.y + bullet.radius > you.hitbox[1]:
            if bullet.x + bullet.radius > you.hitbox[0] and bullet.x - bullet.radius < you.hitbox[0] + you.hitbox[2]:
                you.hit()
                bullets.pop(bullets.index(bullet))

        if bullet.x < 853 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(round(me.x + me.width//2), round(me.y + me.height//2), 6, (0,128,0), facing))

        shootLoop = 1

    if keys[pygame.K_LEFT] and me.x > me.vel:
        me.x -= me.vel
        me.left = True
        me.right = False

    elif keys[pygame.K_RIGHT] and me.x < 853 - me.vel:
        me.x += me.vel
        me.left = False
        me.right = True

    elif keys[pygame.K_UP] and me.y > me.vel:
        me.y -= me.vel
        me.up = True
        me.down = False

    elif keys[pygame.K_DOWN] and me.y < 480 - me.vel:
        me.y += me.vel
        me.up = False
        me.down = True

    redrawGameWindow()

pygame.quit()
