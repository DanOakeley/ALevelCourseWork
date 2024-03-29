import pygame
import random
# -- Global constants

# -- colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,50,50)
GREEN = (50,255,50)
PINK = (255,105,180)
ORANGE = (255,165,0)
CYAN = (0,255,255)
GREY = (128,128,128)

# -- size
size = (1280,720)


# -- Declare variables
fontName = pygame.font.match_font('consolas')
score = 0
# -- open highscore file set the varible and close it
highscorefile = open("HighScore.txt","r")
highscore = (highscorefile.read())
highscorefile.close()
oldhighscore = int(highscore)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
screen = pygame.display.set_mode(size, pygame.RESIZABLE) #will be FULLSCREEN
#background
bg = pygame.image.load("Background.png") # link = https://www.dreamstime.com/dark-terrible-cave-game-illustration-background-path-crossing-tillable-horizontally-empty-place-rock-walls-side-image151625178
#sprite images
PlayerImage = pygame.image.load("player.png")
# -- Title of new window/screen
pygame.display.set_caption("My Window")


# -- Functions
def drawTextWhite (surf, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

def drawTextBlack (surf, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)

def drawTextCyan (surf, text, size, x, y):
    font = pygame.font.Font(fontName, size)
    text_surface = font.render(text, True, CYAN)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)


# -- Classes
class Player(pygame.sprite.Sprite):
    def __init__(self,width,height):
        #set speed of sprite
        self.speed_x = 0
        self.speed_y = 0
        #call the construcitor
        super().__init__()
        #create the sprite and fill with colours
        self.image = pygame.Surface([width,height])
        self.image = pygame.image.load("player1.png")# link = https://imgbin.com/download-png/8JF0pJBm
        #set the position of the sprites
        self.rect = self.image.get_rect()
        self.rect.x = width
        self.rect.y = size[1] //2
        self.lives = 3
        self.bullet_count = 50
        self.score = 0
    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
    def player_set_speed_x(self,val):
        self.speed_x = val
    def player_set_speed_y(self,val):
        self.speed_y = val
    def player_add_lives(self):
        self.lives = self.lives + 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x, y, powerup):
        super().__init__()
        #check if there is powerup active
        self.powerup = powerup
        if self.powerup == True:
            self.speed = 10
            self.image = pygame.Surface([6,6])
            self.image.fill(PINK)
        elif self.powerup == False:
            self.speed = 5
            self.image = pygame.Surface([3,3])
            self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        self.rect.x = self.rect.x + self.speed
        if self.rect.x > size[0]+50:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,width,height,health):
        #set speed of sprite
        self.speed_x = 0
        self.speed_y = 0
        #set the width of the sprite
        self.width = width
        self.height = height
        self.health = health
        #call the construcitor
        super().__init__()
        #create the sprite and fill with colours
        #pick a random number
        self.randomnumber = random.randrange(1,4)
        if self.randomnumber == 1:
            self.color = BLUE #speed will change as well in future
#            self.whichimage = pygame.image.load("Enemy1-Blue.png")
        elif self.randomnumber == 2:
            self.color = RED
#            self.whichimage = pygame.image.load("Enemy1-Pink.png")
        else:
            self.color = GREEN
#            self.whichimage = pygame.image.load("Enemy1-Green.png")
        self.image = pygame.Surface([width,height])
        self.image.fill(self.color)
#        self.image = self.whichimage # temp
        #set the position of the sprites
        self.rect = self.image.get_rect()
        self.rect.x = size[0] - width + int(random.randrange(0,100,10))
        self.rect.y = size[1] - int(random.randrange(15,size[1],1))
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
class Boss(pygame.sprite.Sprite):
    def __init__(self,width,height,health):
        #set speed of sprite
        self.speed_x = 0
        self.speed_y = 0
        #set the width of the sprite
        self.width = width
        self.height = height
        self.health = health
        #call the construcitor
        super().__init__()
        #create the sprite and fill with colours
        self.color = PINK
        self.image = pygame.Surface([width,height])
        self.image.fill(self.color)
#        self.image = self.whichimage # temp
        #set the position of the sprites
        self.rect = self.image.get_rect()
        self.rect.x = size[0] /2
        self.rect.y = size[1]
    def update(self):
        self.rect.x = self.rect.x - 1
        if self.rect.x < -50:
            self.kill()
#        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
    def Boss_set_speed_x(self,val):
        self.speed_x = val
    def Boss_set_speed_y(self,val):
        self.speed_y = val

class Collectable(pygame.sprite.Sprite):
    def __init__(self,x, y, type):
        self.width = 20
        self.height = 20
        self.x = x
        self.y = y
        self.type = type
#        self.rect.x = random.randrange(10,600)
#        self.rect.y = random.randrange(10,700)
#        self.type = random.randrange(1,3)
        #call the constructor
        super().__init__()
        #type1 = more bullets(ORANGE) type2 = more lives(CYAN) type3 = increased speed & size of bullet(PINK)
        if self.type == 1:
            self.color = ORANGE
        if self.type == 2:
            self.color = CYAN
        if self.type == 3:
            self.color = PINK
        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(self.color)
        #set the position of the sprites
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def typefunction(self,g):
        if self.type == 1:
            g.player.bullet_count = g.player.bullet_count + 20
            #g.playerBulletUpdate(20)
        if self.type == 2:
            g.player.player_add_lives()
        if self.type == 3:
            g.BulletPowerUp = True

class Walls(pygame.sprite.Sprite):
    def __init__(self):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = GREY
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(self.color)

class Game(object):
    def __init__(self):
        self.game_over = False
        self.BulletPowerUp = False
        #--lists
        self.all_sprites_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.boss_list = pygame.sprite.Group()
        self.bullet_list = pygame.sprite.Group()
        self.collectable_list = pygame.sprite.Group()
        #bullet_hit_list = pygame.sprite.Group()
        #--create player
        self.player = Player(10,10)
        self.all_sprites_list.add (self.player)
        self.SpawnCollectable()
        #self.collectable = Collectable(200,200,3)
        self.all_sprites_list.add(self.collectable)
        self.collectable_list.add(self.collectable)
        self.spawnEnemies()
    def SpawnCollectable(self):
        self.randomnumberX = random.randrange(200,750)
        self.randomnumberY = random.randrange(10,700)
        self.randomnumberTYPE = random.randrange(1,4)
        self.collectable = Collectable(self.randomnumberX,self.randomnumberY,self.randomnumberTYPE)
        self.all_sprites_list.add(self.collectable)
        self.collectable_list.add(self.collectable)
    def spawnEnemies(self):
        #--create enemies
        NumberOfEnemies = 10
        for i in range(NumberOfEnemies):
            enemy = Enemy(30,30,25)
            self.enemy_list.add (enemy)
            self.all_sprites_list.add (enemy)
    def spawnBoss(self):
        #--create boss
        boss = Boss(100,100,300)
        self.boss_list.add (boss)
        self.all_sprites_list.add (boss)

    def events(self):
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                return(done)
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_ESCAPE):
                    MainMenu()
                    done = True
                    return(done)
                if (event.key == pygame.K_a):
                    self.player.player_set_speed_x(-3)
                elif event.key == pygame.K_d:
                    self.player.player_set_speed_x(3)
                elif event.key == pygame.K_w:
                    self.player.player_set_speed_y(-3)
                elif event.key == pygame.K_s:
                    self.player.player_set_speed_y(3)
                #creates bullets on press of space
                elif event.key == pygame.K_SPACE:
                    if self.player.bullet_count > 0:
                        bullet = Bullet(self.player.rect.x+100, self.player.rect.y+20, self.BulletPowerUp)
                        self.bullet_list.add (bullet)
                        self.player.bullet_count = self.player.bullet_count -1
                    else:
                        print("no bullets")# to be replaced by sound effect
                        self.BulletPowerUp = False
                    #bullet count to go here in future
            elif event.type == pygame.KEYUP:
                if (event.key == pygame.K_a) or (event.key == pygame.K_d):
                    self.player.player_set_speed_x(0)
                if (event.key == pygame.K_w) or (event.key == pygame.K_s):
                    self.player.player_set_speed_y(0)
            #endif
        #nextevent
    def rungame(self):
        BossHitCounter = 0
        #-- Game logic goes after this comment
        self.bullet_list.update()
        # -- check for collisions player and ememy
        self.player_hit_list = pygame.sprite.spritecollide(self.player, self.enemy_list, True)

        for foo in self.player_hit_list:
            self.player.player_set_speed_x(0)
            self.player.player_set_speed_y(0)
            self.player.rect.x = self.player_oldx
            self.player.rect.y = self.player_oldy
            self.player.lives = self.player.lives -1
        self.player_oldx = self.player.rect.x
        self.player_oldy = self.player.rect.y
        # -- check if player hits wall
        # -- check for bullet hits with enemies
        bullet_hit_list = pygame.sprite.groupcollide(self.bullet_list, self.enemy_list, True, True)
        for foo in bullet_hit_list:
            self.player.score = self.player.score + 1

        # -- check for bullet hits with BOSS

        Boss_bullet_hit_list = pygame.sprite.groupcollide(self.bullet_list, self.boss_list,True, False)
        for foo in Boss_bullet_hit_list:
            BossHitCounter = BossHitCounter + 1
        if BossHitCounter >=10:
            self.player.score = self.player.score + 20
            BossHitCounter = 0

        # -- check collectable collisions
        pygame.sprite.groupcollide(self.collectable_list,self.enemy_list, True, False)
        self.collectable_hit_list = pygame.sprite.spritecollide(self.player, self.collectable_list, True)
        for foo in self.collectable_hit_list:
            self.collectable.typefunction(self)
        #end game if out of Lives
        if self.player.lives == 0:
            self.game_over = True
        self.all_sprites_list.update()
        #boarders
        if (self.player.rect.x <=0) or (self.player.rect.x >=1155):
            self.player.player_set_speed_x(0)
        if (self.player.rect.y <=0) or (self.player.rect.y >=635):
            self.player.player_set_speed_y(0)
#    def playerBulletUpdate(self,amount):
#        self.amount = amount
#        self.player.bullet_count = self.player.bullet_count + self.amount
    def displayframe(self,screen):
        # -- Screen background is BLACK
        screen.fill(BLACK)
        screen.blit(bg,[0,0])
        global score
        global highscore
        if self.game_over:
            highscore = int(highscore)
            score = int((self.player.score))
            if score > highscore:
                highscore = score
                #highscore = int(highscore)
                highscorefile = open("HighScore.txt","w")
                highscorefile.write(str(highscore))
                highscorefile.close()
            GameOverScreen()
        if not self.game_over:
            # -- Draw here
            self.all_sprites_list.draw (screen)
            self.bullet_list.draw (screen)
            drawTextWhite(screen, "Lives:" + str(self.player.lives), 18, size[0]-40, 10)
            drawTextWhite(screen, "Bullets Remaining:" + str(self.player.bullet_count), 18,size[0]-190,10)
            drawTextWhite(screen, "Score:" + str(self.player.score), 18,size[0]-350,10)
            drawTextWhite(screen, "HighScore:" + str(highscore), 18, size[0]-470,10)
            # -- flip display to reveal new position of objects
            pygame.display.flip()
def GameOverScreen():
    # --Manages how fast screen refreshes
    clock = pygame.time.Clock()
    #Menu variables
    global score
    global highscore
    global oldhighscore
    GameOverScreenDone = False
    Title = "Game Over !!!!"
    MenuLine1 = "Pick an Option:"
    MenuLine2 = "[1] Open Main Menu"
    MenuLine3 = "[2] Quit"
    ScoreIntro = "Score: "
    HighscoreIntro = "Highscore: "
    NewHighScore1 = "Congratulations"
    NewHighScore2 = " You Got A New High Score!!!!"
    #Menu loop
    while not GameOverScreenDone:
        for event in pygame.event.get():
            GameOverScreenDone = False
            #--Quit conditon if press ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    GameOverScreenDone = True
                    MainMenu()
               #endif
                if event.key == pygame.K_2:
                   GameOverScreenDone = True
                   pygame.quit()
                #endif
            #endif

        # -- Screen background is BLACK
        screen.fill (WHITE)
        # -- Draw here
        pygame.draw.rect(screen, BLACK, (0,0,size[0],150))
        drawTextWhite(screen, str(Title), 50, 200, 50)
        drawTextCyan(screen, str(HighscoreIntro), 50, 1000, 50)
        drawTextCyan(screen, str(highscore), 50, 1175, 50)
        drawTextBlack(screen, str(ScoreIntro), 75, 750, 200)
        drawTextBlack(screen, str(score), 75, 1000, 200)
        drawTextBlack(screen, str(MenuLine1), 20,100, 170)
        drawTextBlack(screen, str(MenuLine2), 20, 115, 220)
        drawTextBlack(screen, str(MenuLine3), 20, 60, 240)
        if int(score) > int(oldhighscore):
            pygame.draw.rect(screen, CYAN, (15,390,1248,200))
            drawTextBlack(screen, str(NewHighScore1), 80, 620, 400)
            drawTextBlack(screen, str(NewHighScore2), 80, 620, 500)

        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # -- clock ticks over
        clock.tick(60)
    #End While

def MainMenu():
    # --Manages how fast screen refreshes
    clock = pygame.time.Clock()
    #Menu variables
    MainMenuDone = False
    Title = "Main Menu"
    MenuLine1 = "Pick an Option:"
    MenuLine2 = "[1] Start Game"
    MenuLine3 = "[2] Open Help Page"
    MenuLine4 = "[3] Quit"
    #Menu loop
    while not MainMenuDone:
        for event in pygame.event.get():
            MainMenuDone = False
            #--Quit conditon if press ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    MainMenuDone = True
                    MainGame()
               #endif
                if event.key == pygame.K_2:
                   MainMenuDone = True
                   HelpPage()
                #endif
                if event.key == pygame.K_3:
                    MainMenuDone = True
                    pygame.quit()
                #endif
            #endif

        # -- Screen background is BLACK
        screen.fill (WHITE)
        # -- Draw here
#        screen.blit(Player.)
        pygame.draw.rect(screen, ORANGE, (0,0,size[0],150))
        drawTextBlack(screen, str(Title), 50, 150, 50)
        drawTextBlack(screen, str(MenuLine1), 20,100, 170)
        drawTextBlack(screen, str(MenuLine2), 20, 145, 220)
        drawTextBlack(screen, str(MenuLine3), 20, 167, 240)
        drawTextBlack(screen, str(MenuLine4), 20, 112, 260)

        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # -- clock ticks over
        clock.tick(60)
    #End While

def HelpPage():
    # --Manages how fast screen refreshes
    clock = pygame.time.Clock()
    #Menu variables
    HelpMenuDone = False
    Title = "Help Menu"
    MenuLine1 = " [1] Back to Main Menu"
    MenuLine2 = "[2] quit"
    Instructions1 = "Player Controls:"
    Instructions2 = "[W] to move up"
    Instructions3 = "[S] to move down"
    Instructions4 = "[A] to move left"
    Instructions5 = "[S] to move right"
    Instructions6 = "[SPACE] to shoot"
    #Menu loop
    while not HelpMenuDone:
        for event in pygame.event.get():
            HelpMenuDone = False
            #--Quit conditon if press ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    HelpMenuDone = True
                    MainMenu()
               #endif
                if event.key == pygame.K_2:
                   HelpMenuDone = True
                   pygame.quit()
                #endif
            #endif

        # -- Screen background is BLACK
        screen.fill (WHITE)
        # -- Draw here
        pygame.draw.rect(screen, YELLOW, (0,0,size[0],150))
        pygame.draw.rect(screen, BLUE, (430,270,300,250))
        drawTextBlack(screen, str(Title), 50, 150, 50)
        drawTextBlack(screen, str(MenuLine1), 20,120, 170)
        drawTextBlack(screen, str(MenuLine2), 20, 53, 220)
        drawTextWhite(screen, str(Instructions1), 20, 600, 280)
        drawTextWhite(screen, str(Instructions2), 20, 600, 310)
        drawTextWhite(screen, str(Instructions3), 20, 600, 340)
        drawTextWhite(screen, str(Instructions4), 20, 600, 370)
        drawTextWhite(screen, str(Instructions5), 20, 600, 400)
        drawTextWhite(screen, str(Instructions6), 20, 600, 430)

        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # -- clock ticks over
        clock.tick(60)
    #End While

def MainGame():
    # -- counter setup
    counter = 0
    # -- Exit game flag set to false
    done = False

    # --Manages how fast screen refreshes
    clock = pygame.time.Clock()

    # -- create an instance of the game
    game = Game()
#    game.spawnEnemies()
#    game.SpawnCollectables()
    # -- Game Loop
    while not done:
        Bullet.powerup = False

        # -- process user inputs
        done = game.events()

        # -- update objects and control collisions
        game.rungame()

        #draw the current screen
        game.displayframe(screen)
        # -- The clock ticks over
        clock.tick(60)
        #counter for spawning enemies
        counter = counter + 1
        if counter %800 == 0:
            game.spawnEnemies()
        if counter%1250 == 0:
            game.SpawnCollectable()
        if counter %400 ==0:
            game.spawnBoss()
    #End While - End of game loop
    pygame.quit()

MainMenu()
pygame.quit()
