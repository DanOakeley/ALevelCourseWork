import pygame
# -- Global constants

# -- colours5
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)


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
        self.rect.x = size[0] //2
        self.rect.y = size[1] - height -40
        self.lives = 3
        self.bullet_count = 50
    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
    def player_set_speed_x(self,val):
        self.speed_x = val
    def player_set_speed_y(self,val):
        self.speed_y = val

class Bullet(pygame.sprite.Sprite):
    def __init__(self,color,speed):
        self.speed = speed
        super().__init__()
        self.image = pygame.Surface([2,2])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 20
        self.rect.y = player.rect.y

    def update(self):
        self.rect.y = self.rect.y + self.speed

#--lists
all_sprites_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
bullet_hit_group = pygame.sprite.Group()
#--create player
player = Player(YELLOW,10,10)
all_sprites_group.add (player)

# screenr refresh
clock = pygame.time.Clock()
# -- Game Loop
while not done:
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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player.player_set_speed_x(0)
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player.player_set_speed_y(0)
        #endif
    #nextevent

    # -- Game logic goes after this comment
    all_sprites_group.update()
    # -- Screen background is BLACK
    screen.fill(BLACK)

    # -- Draw here
    all_sprites_group.draw (screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()

    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
