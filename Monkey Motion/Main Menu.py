import pygame
import os

os.chdir('D:\College\Second Year 2\Disciplinary Team Project\Monkey Motion')

pygame.init()

display_width = 1400    #Screen Size
display_height = 650

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
bright_red = (200,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Monkey Motion')
clock = pygame.time.Clock()

pygame.mixer.music.load('Menu Music.mp3') #Loads in music
pygame.mixer.music.play(-1)

titImg = pygame.image.load('images/Title.png') #Loads in background image

crashed = False

def tit(x,y):#Defines the background
    gameDisplay.blit(titImg,(-25,-400))

def text_objects(text, font): #Defines a simple text object to pull
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac, action=None): #Defines a button class which can be used to quickly make buttons
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():  #Sets up the quit function to exit the game
    pygame.quit()
    quit()

def game_intro(): #Code for the main menu screen

    intro = True

    while intro: #While loop that sets up the quit function
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(titImg,(-25,-400))


        mouse = pygame.mouse.get_pos()

        button("Start",700,350,100,50,bright_red,red,level_select) #Buttons made from the class allows you to visit different pages
        button("Help",700,450,100,50,bright_red,red,game_controls)
        button("Quit",700,550,100,50,bright_red,red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_controls(): #Code for the controls menu

    gcont = True

    while gcont: #While loop that sets up the quit function
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(titImg,(-25,-400))

        mouse = pygame.mouse.get_pos()

        mainText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = text_objects("To control the monkey, you must use the motion sensors to move left to right.", mainText) #Code pulled from the define class above to set up the text
        TextRect.center = ((display_width/2),(520))
        gameDisplay.blit(TextSurf, TextRect)
        mainText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = text_objects("You must dodge obstacles and gather bananas and progress through the level.", mainText)
        TextRect.center = ((display_width/2),(550))
        gameDisplay.blit(TextSurf, TextRect)
        mainText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = text_objects("Press the ESC key to quit the game.", mainText)
        TextRect.center = ((display_width/2),(580))
        gameDisplay.blit(TextSurf, TextRect)


        button("Back",1200,500,100,50,bright_red,red,game_intro)#Code lets you return to main menu

        pygame.display.update()
        clock.tick(15)

def level_select(): #Code used to set up the level select menu

    select = True

    while select: #While loop that sets up the quit function
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(titImg,(-25,-400))


        mouse = pygame.mouse.get_pos()

        button("WIP",700,350,100,50,bright_red,red,level_1)
        button("Level 2",700,450,100,50,bright_red,red,level_2) #Code lets you progress to the game code
        button("Level 3",700,550,100,50,bright_red,red,level_3)
        button("Back",1200,500,100,50,bright_red,red,game_intro) #Code lets you return to main men

        pygame.display.update()
        clock.tick(15)

def level_1():

    global pause

def level_2():

    import Game #Import accesses the game files

def level_3():

    import Boss #Import accesses the game files

game_intro()
game_controls()
level_select()
level_1()
level_2()
level_3()
pygame.quit()
quit()
