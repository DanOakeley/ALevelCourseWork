import pygame
import random
# -- Global constants

# -- colours5
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,50,50)
GREEN = (50,255,50)


# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
done = False

# --Manages how fast screen refreshes
clock = pygame.time.Clock()

#--Classes
class Player(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        #set speed of sprite
        self.speed_x = 0
        self.speed_y = 0
        #call the construcitor
        super().__init__()
        #create the sprite and fill with colours
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #set the position of the sprites
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = size[1] //2
        #self.lives = 3
        #self.bullet_count = 50
    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
    def player_set_speed_x(self,val):
        self.speed_x = val
    def player_set_speed_y(self,val):
        self.speed_y = val

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x, y, powerup):
        #check if there is powerup active
        self.powerup = powerup
        if self.powerup == True:
            self.speed = 10
        elif self.powerup == False:
            self.speed = 5
        super().__init__()
        self.image = pygame.Surface([2,2])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x = self.rect.x + self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self,width,height):
        #set speed of sprite
        self.speed_x = 0
        self.speed_y = 0
        #set the width of the sprite
        self.width = 20
        self.height = 20
        #call the construcitor
        super().__init__()
        #create the sprite and fill with colours
        #pick a random number
        self.randomnumber = random.randrange(1,3)
        if self.randomnumber == 1:
            self.color = BLUE #speed will change as well in future
        elif self.randomnumber == 2:
            self.color = RED
        else:
            self.color = GREEN
        self.image = pygame.Surface([width,height])
        self.image.fill(self.color)
        #set the position of the sprites
        self.rect = self.image.get_rect()
        self.rect.x = size[0] - width
        self.rect.y = size[1] - int(random.randrange(15,480,1))
        #self.lives = 3
        #self.bullet_count = 50
    def update(self):
        self.rect.x = self.rect.x - 1
        if self.rect.x < -50:
            self.kill()
#        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
    def enemy_set_speed_x(self,val):
        self.speed_x = val
    def enemy_set_speed_y(self,val):
        self.speed_y = val
#--lists
all_sprites_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
bullet_hit_list = pygame.sprite.Group()
#--create player
player = Player(YELLOW,10,10)
all_sprites_list.add (player)

#--create enemies
NumberOfEnemies = 10
for i in range(NumberOfEnemies):
    enemy = Enemy(15,15)
    enemy_list.add (enemy)
    all_sprites_list.add (enemy)

# screenr refresh
clock = pygame.time.Clock()
# -- Game Loop
while not done:
    powerup = False
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.player_set_speed_x(-3)
            elif event.key == pygame.K_d:
                player.player_set_speed_x(3)
            elif event.key == pygame.K_w:
                player.player_set_speed_y(-3)
            elif event.key == pygame.K_s:
                player.player_set_speed_y(3)
            #creates bullets on press of space
            elif event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.x, player.rect.y, powerup)
                bullet_list.add (bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.player_set_speed_x(0)
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.player_set_speed_y(0)
        #endif
    #nextevent

    # -- Game logic goes after this comment
    all_sprites_list.update()
    bullet_list.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_list.draw (screen)
    bullet_list.draw (screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
