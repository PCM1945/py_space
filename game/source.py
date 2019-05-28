# ************space game*****************
# import libs
import pygame
import random


# ***********************game classes**************************************


class Ship(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.life = 100
        self.image = pygame.image.load(r'resources\ship_hero.png')
        self.hitbox = (self.x, self.y - self.height + self.width, self.height, 150)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y - self.height + self.width, self.height, 150)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        print("hero hit")
        return 1


class Projectile(object):
    def __init__(self, x, y, speed):
        self.speed = speed
        self.x = x
        self.y = y
        self.image = pygame.image.load(r'resources\ire.png')

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class EnemyShip(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.center =(self.x/2, self.y/2)
        self.image = pygame.image.load(r'resources\meteoro.gif')
        self.hitbox = (self.x, self.y - 100 + self.width, self.height, 100)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
        self.hitbox = (self.x, self.y - 100 + self.width, self.height, 100)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
        self.center = (self.x/2, self.y/2)

    def move(self):
        if self.x > -110 and self.speed > 0:
            self.x -= self.speed

    def hit(self):
        print("enemy hit")
        return 1


# ******************** end game classes
# initialize screen


pygame.init()
screen_width, screen_height = 1000, 900
screen = pygame.display.set_mode((screen_width, screen_height))

# ********* Player *********
# setting initial x,y player position
playerpos_x, playerpos_y = 100, 100
player_width, player_height = 150, 150
player_speed = 30
player_image = pygame.image.load(r'resources\ship_hero.png')

heroShip = Ship(playerpos_x, playerpos_y, player_width,
                player_height, player_speed)
# ****************************************************

# ********* Projectile *********
bullet_speed = 50
bullets = []
# ******************************

heroh = 0

# **********Enemy***************
enemy_speed = 20
new_x = 100  # initialising new_X
enemy_y = 800

# meteor = EnemyShip(650, 100, 111, 109, 10)
enemys = []
# *******************************

# *********general use variables********
# setting key array
keys = []
# bullet_count = 0

score = 0
font = pygame.font.SysFont("comicsans", 30, True)
# loop forever
while 1:
    # *********updates the screen*************
    # clear the screen before drawing again
    pygame.time.delay(100)
    screen.fill(1)
    # update the screen
    # screen.blit(heroShip.image, (heroShip.x, heroShip.y))
    heroShip.draw(screen)
    pygame.display.update()

    # *****generates random positions for the enemys to appear on the screen******************
    for x in range(5):
        pos_index = random.randint(1, 4)
        # print(pos_index)
        if pos_index == 1:
            new_x = 100
        if pos_index == 2:
            new_x = 300
        if pos_index == 3:
            new_x = 500
        if pos_index == 4:
            new_x = 700
        # print(new_x)
    for bullet in bullets:
        if bullet.x < 1000 and bullet.y > 0:
            # print(bullet.x)
            bullet.x += bullet.speed  # moves the bullet
        else:
            bullets.pop(bullets.index(bullet))  # removes the bullet
            # bullet_count -= 1
    # destroy the enemy if it is out of the screen
    for meteor in enemys:
        try:
            if meteor.x < -100:
                enemys.pop(enemys.index(meteor))
            else:
                meteor.move()
        except:
            print("error in enemy list")
    if len(enemys) < 5:
        enemys.append(EnemyShip(enemy_y, new_x, 111, 109, enemy_speed))
    # *********************enemy hit detection************************
    for meteor in enemys:
        for bullet in bullets:
            if bullet.y < meteor.hitbox[1] + meteor.hitbox[3] and bullet.y > meteor.hitbox[1]:  # Checks x coords
                if bullet.x > meteor.hitbox[0] and bullet.x < meteor.hitbox[0] + meteor.hitbox[2]:  # Checks y coords
                    bullets.pop(bullets.index(bullet))  # removes bullet from bullet list
                    if meteor.hit() == 1:  # if enemy get hit destroy object
                        try:
                            enemys.pop(enemys.index(meteor))
                        except:
                            print("error")
                        score += 10
    # ********************* Hero hit detection*************************
    for meteor in enemys:
        if heroShip.hitbox[1] < meteor.hitbox[1] + meteor.hitbox[3] and heroShip.hitbox[1] + heroShip.hitbox[3] > meteor.hitbox[1]:
            if heroShip.hitbox[0] + heroShip.hitbox[2] > meteor.hitbox[0] and heroShip.hitbox[0] < meteor.hitbox[0] + meteor.hitbox[2]:
                heroShip.hit()
                score -= 5
                if heroShip.hit() == 1:
                    heroh += 1
                    print(heroh)
    # ********************button event check***************************
    # check if the event is a key button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    keys = pygame.key.get_pressed()
    # print(bullet_count)
    if keys[pygame.K_UP] and heroShip.y > heroShip.speed:
        heroShip.y -= heroShip.speed
    if keys[pygame.K_DOWN] and heroShip.y < screen_width - heroShip.width - heroShip.speed:
        heroShip.y += heroShip.speed
    if keys[pygame.K_LEFT] and heroShip.x > heroShip.speed:
        heroShip.x -= heroShip.speed
    if keys[pygame.K_RIGHT] and heroShip.x < screen_height - heroShip.height - heroShip.speed:
        heroShip.x += heroShip.speed
    if keys[pygame.K_SPACE]:
        bullets.append(Projectile(heroShip.x + 150, heroShip.y + 100, bullet_speed))
        #  bullet_count += 1

    # **************** updates the screen with the  assets**********************************
    text = font.render("Score: " + str(score), 1, (255, 255, 255))  # Arguments are: text, anti-aliasing, color
    screen.blit(text, (390, 10))
    for meteor in enemys:
        meteor.draw(screen)
        pygame.display.update()
    for bullet in bullets:
        bullet.draw(screen)
        pygame.display.update()
