from Player import *
from Enemy2 import *
from PowerUp import *
from Screen import *
import sys
from pygame import mixer


pygame.init()
mixer.init()

clock = pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

FPS = 60

speed = 0.8

screen = Screen(WIDTH, HEIGHT)
Screen = screen.draw_screen()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


#All files imported
Background_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Space_Background.jpg'
Background2_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Space_Background2.jpg'
Background3_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Space_Background3.jpg'
Play_Button_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Play Button.jpg'
Option_Button_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Option Button.jpg'
Continue_Button_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Continue Button.jpg'
Main_Menu_Button_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Main Menu Button.jpg'
Player_1_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Player 1.png'
Blaster_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Blaster.png'
Asteroid1_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Asteroid1.png'
Enemy1_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Enemy1.png'
Music_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Songs//Interstellar Main Theme.mp3'
Music_File_2 = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Songs//Cold Womb Descent.mp3'
Volume_OFF_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//OFF.png'
Volume_2_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Volume 2.png'
Volume_4_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Volume 4.png'
Volume_6_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Volume 6.png'
Volume_8_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Volume 8.png'
Volume_10_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Volume 10.png'
How_To_Play_Button_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//How To Play Button.jpg'
Instruction_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Instructions.png'
Asteroid_Image_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Asteroid.png'
Pause_Title_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Pause Title.png'
Quit_Button_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Quit Button.jpg'
Play_Again_Button_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Play Again Button.jpg'
Game_Over_Title_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Game Over Title.png'
PowerUP_Def_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//PowerUp Def.png'
Ability_Shield_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//PowerUp Shield.png'
Black_Hole_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Black Hole.png'
Game_Title_File = 'C://Users//joeyf//Documents//Sandbox//Python Projects//Galaxian_Space_Fighter//Images//Game Title.png'

#Initialize Mixer to play music
mixer.music.load(Music_File)
mixer.music.set_volume(0.7)
mixer.music.play(-1)

myFont = pygame.font.SysFont("monospace", 35)
myFont2 = pygame.font.SysFont("Oynx", 50)

print((pygame.font.get_fonts()))

#Buttons' Position on screen
PBx, PBy = ((WIDTH/2)-225/2), 200
OBx, OBy = ((WIDTH/2)-225/2), 300
HTPx, HTPy = ((WIDTH/2)-225/2), 400
VolButtonX, VolButtonY = (120, 500)


total_blaster = 1


#All objects created
Background = Image(Background_File, [0,0])
Background2 = Image(Background2_File, [0,0])
Background3 = Image(Background3_File, [0,0])
#Pixel Size: 225 x 70
Play_Button = Image(Play_Button_File, [PBx,PBy])
Menu_Button = Image(Main_Menu_Button_File, [PBx,PBy])
#Pixel Size: 225 x 70
Option_Button = Image(Option_Button_File, [OBx,OBy])
How_To_Play = Image(How_To_Play_Button_File, [HTPx, HTPy])
Instruction = Image(Instruction_File, [380, 50])
Asteroid_Image = Image(Asteroid_Image_File, [0, 170])
Continue_Button = Image(Continue_Button_File, [OBx, OBy])
Quit_Button = Image(Quit_Button_File, [HTPx, HTPy])
Play_Again_Button = Image(Play_Again_Button_File, [OBx, OBy])
Pause_Title = Image(Pause_Title_File, [PBx-225, PBy - 150])
Game_Over_Title = Image(Game_Over_Title_File, [PBx-225, PBy - 150])
Black_Hole = Image(Black_Hole_File, [580,30])
Game_Title = Image(Game_Title_File, [125, 20])



#Initializing Volume BUTTONS
OFF_Button = Image(Volume_OFF_File, [VolButtonX, VolButtonY])
Vol2_Button = Image(Volume_2_File, [VolButtonX+100, VolButtonY])
Vol4_Button = Image(Volume_4_File, [VolButtonX+200, VolButtonY])
Vol6_Button = Image(Volume_6_File, [VolButtonX+300, VolButtonY])
Vol8_Button = Image(Volume_8_File, [VolButtonX+400, VolButtonY])
Vol10_Button = Image(Volume_10_File, [VolButtonX+500, VolButtonY])


pygame.display.set_caption('Galaxian Space Fighter')


#How to play function
def HowToPlay():
    x, y = 50, 50
    click = False
    HowtoPlay = True
    Menu_Button = Image(Main_Menu_Button_File, [x, y])

    while HowtoPlay:
        clock.tick(FPS)

        Screen.fill(WHITE)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(x, y, 225, 70)

        if button_1.collidepoint(mx, my):
            if click:
                Main_Menu()


        pygame.draw.rect(Screen, WHITE, button_1)


        Screen.blit(Background.image, Background.rect)
        Screen.blit(Menu_Button.image, Menu_Button.rect)
        Screen.blit(Instruction.image, Instruction.rect)
        Screen.blit(Asteroid_Image.image, Asteroid_Image.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    HowtoPlay = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        
#Option function
def Options():
    Option = True
    click = False

    while Option:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        clock.tick(FPS)

        Screen.fill(WHITE)

        mx, my = pygame.mouse.get_pos()

        #Create button objects
        button_1 = pygame.Rect(PBx, PBy, 225, 70)
        button_2 = pygame.Rect(VolButtonX, VolButtonY, 70, 70)
        button_3 = pygame.Rect(VolButtonX+100, VolButtonY, 70, 70)
        button_4 = pygame.Rect(VolButtonX+200, VolButtonY, 70, 70)
        button_5 = pygame.Rect(VolButtonX+300, VolButtonY, 70, 70)
        button_6 = pygame.Rect(VolButtonX+400, VolButtonY, 70, 70)
        button_7 = pygame.Rect(VolButtonX+500, VolButtonY, 70, 70)

        if button_1.collidepoint(mx, my):
            if click:
                Option = False
                Main_Menu()
        if button_2.collidepoint(mx, my):
            if click:
                mixer.music.set_volume(0)
        if button_3.collidepoint(mx, my):
            if click:
                mixer.music.set_volume(0.2)
        if button_4.collidepoint(mx, my):
            if click:
                mixer.music.set_volume(0.4)
        if button_5.collidepoint(mx, my):
            if click:
                mixer.music.set_volume(0.6)
        if button_6.collidepoint(mx, my):
            if click:
                mixer.music.set_volume(0.8)
        if button_7.collidepoint(mx, my):
            if click:
                mixer.music.set_volume(1)

        #Draw button
        pygame.draw.rect(Screen, WHITE, button_1)
        pygame.draw.rect(Screen, WHITE, button_2)
        pygame.draw.rect(Screen, WHITE, button_3)
        pygame.draw.rect(Screen, WHITE, button_4)
        pygame.draw.rect(Screen, WHITE, button_5)
        pygame.draw.rect(Screen, WHITE, button_6)
        pygame.draw.rect(Screen, WHITE, button_7)

        #Blit the button images
        Screen.blit(Background3.image, Background3.rect)
        Screen.blit(Menu_Button.image, Menu_Button.rect)
        Screen.blit(OFF_Button.image, OFF_Button.rect)
        Screen.blit(Vol2_Button.image, Vol2_Button.rect)
        Screen.blit(Vol4_Button.image, Vol4_Button.rect)
        Screen.blit(Vol6_Button.image, Vol6_Button.rect)
        Screen.blit(Vol8_Button.image, Vol8_Button.rect)
        Screen.blit(Vol10_Button.image, Vol10_Button.rect)

        pygame.display.update()

#Game over: end the game
def GameOver(PlayerSprite, AsteroidSprite, EnemySprite):
    collide_1 = pygame.sprite.groupcollide(PlayerSprite, AsteroidSprite, 1, 1)
    collide_2 = pygame.sprite.groupcollide(PlayerSprite, EnemySprite, 1, 1)

    if collide_1 or collide_2:
        return True

#Game over screen function
def GameOverScreen():
    GameOver = True
    click = False
    Menu_Button = Image(Main_Menu_Button_File, [HTPx, HTPy + 100])

    while GameOver:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(OBx, OBy, 225, 70)
        button_2 = pygame.Rect(HTPx, HTPy, 225, 70)
        button_3 = pygame.Rect(HTPx, HTPy + 100, 225, 70)

        if button_1.collidepoint(mx, my):
            if click:
                GameOver = False
                Game()

        if button_2.collidepoint(mx, my):
            if click:
                sys.exit()
        if button_3.collidepoint(mx, my):
            if click:
                GameOver = False
                PlayMusic1()
                Main_Menu()

        Screen.fill(WHITE)

        pygame.draw.rect(Screen, WHITE, button_1)
        pygame.draw.rect(Screen, WHITE, button_2)
        pygame.draw.rect(Screen, WHITE, button_3)
        Screen.blit(Play_Again_Button.image, Play_Again_Button.rect)
        Screen.blit(Quit_Button.image, Quit_Button.rect)
        Screen.blit(Game_Over_Title.image, Game_Over_Title.rect)
        Screen.blit(Menu_Button.image, Menu_Button.rect)

        text = "Score: "
        score = str(Score)
        label = myFont2.render(text, 1, BLACK)
        label2 = myFont2.render(score, 1, BLACK)
        Screen.blit(label, (75, OBy))
        Screen.blit(label2, (75, HTPy))

        pygame.display.update()

#Pause function
def pause():
    click = False
    pause = True

    while pause:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(OBx, OBy, 225, 70)
        button_2 = pygame.Rect(HTPx, HTPy, 225, 70)

        if button_1.collidepoint(mx, my):
            if click:
                pause = False
        if button_2.collidepoint(mx, my):
            if click:
                sys.exit()

        #Screen.fill(WHITE)

        pygame.draw.rect(Screen, WHITE, button_1)
        pygame.draw.rect(Screen, WHITE, button_2)
        Screen.blit(Continue_Button.image, Continue_Button.rect)
        Screen.blit(Quit_Button.image, Quit_Button.rect)
        Screen.blit(Pause_Title.image, Pause_Title.rect)
        pygame.display.update()

#Randomly spawn viruses on left, right or top side of screen
def LeftRandPos():
    x_pos = random.randint(-600, -50)
    y_pos = random.randint(0, 650/2)
    return x_pos, y_pos

def RightRandPos():
    x_pos = random.randint(850, 1400)
    y_pos = random.randint(0, 650/2)
    return x_pos, y_pos

def TopRandPos():
    x_pos = random.randint(0, 750)
    y_pos = random.randint(-100, -50)
    return x_pos, y_pos

#The game function
def Game():
    global Score
    game_over = False

    total_asteroid = 3
    total_enemy = 1
    total_PowerUPs = 1

    IncreaseSpeed = False
    Spawn = False

    global x_pos, y_pos

    x_pos = random.randint(0, 750)
    y_pos = random.randint(-600, -50)
    xPOW = -100
    yPOW = 250

    # Player's Position on Screen
    x, y = ((WIDTH / 2) - 50 / 2), HEIGHT - 50

    #Create object to store different types of sprites
    Player_Sprites = pygame.sprite.Group()
    Blaster_Sprites = pygame.sprite.Group()
    Asteroids_Sprites = pygame.sprite.Group()
    Enemy_Sprites = pygame.sprite.Group()
    PowerUp_Sprites = pygame.sprite.Group()
    Abilities_Sprites = pygame.sprite.Group()

    Player_1 = Player(Player_1_File, [x, y])
    enemy1 = Enemy2(Enemy1_File, [400, -100])

    Player_Sprites.add(Player_1)
    Enemy_Sprites.add(enemy1)

    Shield_Ends = 400
    Shield_Activated = False
    Shield_Timer = 0
    Counter = 0
    Score = 0
    
    #Game starts
    while not game_over:

        clock.tick(FPS)

        Counter += 1
        #print(Counter)

        #Determines when to spawn
        if (int(Counter) % 200 == 0 and not (Counter <= 1)):
            Spawn = True

        #Spawn roids and virus when Spawn = True (Makes game progressively harder)
        if (int(Counter) % 500 == 0 and not (Counter <= 1)):
            total_asteroid += 1
            total_enemy += 1
        if (int(Counter) % 500 == 0 and not (Counter <= 1)):
            IncreaseSpeed = True
            Asteroids_Sprites.update(IncreaseSpeed)
        IncreaseSpeed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
        #Adds roid if list if list is less than total (True when a roid is killed or despawns)
        if len(Asteroids_Sprites) < total_asteroid:
            for i in range(total_asteroid - len(Asteroids_Sprites)):
                x_pos, y_pos = TopRandPos()
                enemy = Enemy(Asteroid1_File, [x_pos, y_pos])
                Asteroids_Sprites.add(enemy)
            
        #A function to change amount of blasters
        if len(Blaster_Sprites) < total_blaster:
            for i in range(total_blaster):
                blaster = Blaster(Blaster_File, [x, y])
                Blaster_Sprites.add(blaster)

        #Spawns viruses in random spots
        if len(Enemy_Sprites) < total_enemy:
            for i in range(total_enemy - len(Enemy_Sprites)):
                randVal = random.randint(1,3)

                if randVal == 1:
                    x_pos, y_pos = LeftRandPos()
                if randVal == 2:
                    x_pos, y_pos = TopRandPos()
                if randVal == 3:
                    x_pos, y_pos = RightRandPos()

                enemy1 = Enemy2(Enemy1_File, [x_pos, y_pos])
                Enemy_Sprites.add(enemy1)

        #Spawn a powerUP in a random spot
        if len(PowerUp_Sprites) < total_PowerUPs and Shield_Activated == False:
            for i in range(total_PowerUPs - len(PowerUp_Sprites)):
                xPOW = random.randint(-600, -50)
                yPOW = random.randint(0, 650 / 2)
                PowerUP_Def = PowerUP(PowerUP_Def_File, [xPOW, yPOW])
                PowerUp_Sprites.add(PowerUP_Def)

        #A, B, E, F checks if a collision occurs between two sprites. If true, depsawn sprite if parameter = 1
        E = pygame.sprite.groupcollide(Blaster_Sprites, Asteroids_Sprites, 1, 1)

        F = pygame.sprite.groupcollide(Blaster_Sprites, Enemy_Sprites, 1, 1)

        if E:
            Score += 1
        if F:
            Score += 2

        A = pygame.sprite.groupcollide(Blaster_Sprites, PowerUp_Sprites, 1, 1)
        B = pygame.sprite.groupcollide(Player_Sprites, PowerUp_Sprites, 0, 1)

        #Gives player powerup if true
        if A or B:
            Ability_Shield = Abilities(Ability_Shield_File, [x, y])
            Abilities_Sprites.add(Ability_Shield)
            Shield_Activated = True

        #Activate shield
        if Shield_Activated == True:
            Shield_Timer += 1
            C = pygame.sprite.groupcollide(Abilities_Sprites, Enemy_Sprites, 0, 1)
            D = pygame.sprite.groupcollide(Abilities_Sprites, Asteroids_Sprites, 0, 1)
            if C:
                Score += 2
            if D:
                Score += 1

        #Shield timer. Deactivates when timer = 0
        if Shield_Timer == Shield_Ends:
            Shield_Activated = False
            Shield_Timer = 0
            Abilities_Sprites.remove(Ability_Shield)


        # Calls all "update()" functions from the object's class (Polymorphism)
        Blaster_Sprites.update(Player_1.rect.x, Player_1.rect.y)
        Player_Sprites.update()
        Asteroids_Sprites.update(IncreaseSpeed)
        Enemy_Sprites.update(Player_1.rect.x, Player_1.rect.y)
        PowerUp_Sprites.update(Spawn)
        Abilities_Sprites.update(Player_1.rect.x, Player_1.rect.y)
        #Set Spawn = False after it updates (Pretty much an on/off switch)
        Spawn = False

        #Draw Screen and sprites onto screen
        Screen.fill(WHITE)
        Screen.blit(Background.image, Background.rect)
        Blaster_Sprites.draw(Screen)
        Asteroids_Sprites.draw(Screen)
        Enemy_Sprites.draw(Screen)
        Player_Sprites.draw(Screen)
        PowerUp_Sprites.draw(Screen)
        Abilities_Sprites.draw(Screen)

        #Score text
        text = "Score: " + str(Score)
        label = myFont.render(text, 1, YELLOW)
        Screen.blit(label, (WIDTH - 250, HEIGHT - 40))
        #Screen.blit(Black_Hole.image, Black_Hole.rect)

        #update game
        pygame.display.update()

        if (GameOver(Player_Sprites, Asteroids_Sprites, Enemy_Sprites)):
            game_over = True
            GameOverScreen()

#Play different music functions
def PlayMusic1():
    mixer.music.load(Music_File)
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)

def PlayMusic2():
    mixer.music.load(Music_File_2)
    mixer.music.set_volume(0.1)
    mixer.music.play(-1)

#Main Menu function
def Main_Menu():
    click = False
    MainMenu = True

    while MainMenu:


        clock.tick(FPS)

        Screen.fill(WHITE)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(PBx, PBy, 225, 70)
        button_2 = pygame.Rect(OBx, OBy, 225, 70)
        button_3 = pygame.Rect(HTPx, HTPy, 225, 70)

        if button_1.collidepoint(mx, my):
            if click:
                MainMenu = False
                mixer.music.stop()
                PlayMusic2()
                Game()

        if button_2.collidepoint(mx, my):
            if click:
                MainMenu = False
                Options()
        if button_3.collidepoint(mx, my):
            if click:
                MainMenu = False
                HowToPlay()

        pygame.draw.rect(Screen, WHITE, button_1)
        pygame.draw.rect(Screen, WHITE, button_2)
        pygame.draw.rect(Screen, WHITE, button_3)

        Screen.blit(Background2.image, Background2.rect)
        Screen.blit(Play_Button.image, Play_Button.rect)
        Screen.blit(Option_Button.image, Option_Button.rect)
        Screen.blit(How_To_Play.image, How_To_Play.rect)
        Screen.blit(Game_Title.image, Game_Title.rect)

        #Set click = False again when click = true and not on buttons
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

#boots game
Main_Menu()
