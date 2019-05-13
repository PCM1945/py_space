# ************space game*****************
# import libs
import pygame


class Ship(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.image.load("resources\ship_hero.png")

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class Projectile(object):
    def __init__(self, x, y, speed):
        self.speed = speed
        self.x = x
        self.y = y
        self.image = pygame.image.load("resources\ire.png")

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class EnemyShip(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pygame.image.load("resources\meteoro.png")

# initialize screen
pygame.init()
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# ********* Player *********
# setting initial x,y player position
playerpos_x, playerpos_y = 100, 100
player_width, player_height = 150, 150
player_speed = 20
player_image = pygame.image.load("resources\ship_hero.png")

heroShip = Ship(playerpos_x, playerpos_y, player_width,
                player_height, player_speed)

# ********* Projectile *********
bullet_speed = 20
bullets = []
# setting key array
keys = []
enemypos = [680, 100]
vel = 20
# loading player resource
enemy = pygame.image.load("resources\meteoro.gif")

# loop forever
while 1:
    # clear the screen before drawing again
    pygame.time.delay(100)
    screen.fill(1)
    # draw the screen elements
    screen.blit(heroShip.image, (heroShip.x, heroShip.y))
    screen.blit(enemy, enemypos)
    # update the screen
    pygame.display.update()
    for bullet in bullets:
        if bullet.x < 1000 and bullet.y > 0:
            bullet.x += bullet.speed  # moves the bullet
        else:
            bullets.pop(bullets.index(bullet))  # removes the bullet

    # check if the event is a key button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and heroShip.y > heroShip.speed:
        heroShip.y -= heroShip.speed
    if keys[pygame.K_DOWN] and heroShip.y < screen_width - heroShip.width - heroShip.speed:
        heroShip.y += heroShip.speed
    if keys[pygame.K_LEFT] and heroShip.x > heroShip.speed:
        heroShip.x -= heroShip.speed
    if keys[pygame.K_RIGHT] and heroShip.x < screen_height - heroShip.height - heroShip.speed:
        heroShip.x += heroShip.speed
    if keys[pygame.K_SPACE]:
        print("fire")
        bullets.append(Projectile(heroShip.x+ 150, heroShip.y + 100, bullet_speed))

    for bullet in bullets:
        bullet.draw(screen)
        pygame.display.update()