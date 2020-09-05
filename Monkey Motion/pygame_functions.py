# pygame_functions

########################

# Imported library of pre-written pygame functions that simplify using Pygame
# Written by Steve Paget
# Documentation at www.github.com/stevepaget/pygame_functions

# CODE WILL BE REFERENCED WHERE APPROPRIATE

########################
import pygame, math, sys, os                                                        # LINES 14 - 101 SOURCED FROM STEVE PAGET

pygame.mixer.pre_init(44100, -16, 2, 512)                                           # Code initializing PyGame and PyGame Functions
pygame.init()
pygame.mixer.init()
spriteGroup = pygame.sprite.OrderedUpdates()
textboxGroup = pygame.sprite.OrderedUpdates()
gameClock = pygame.time.Clock()
musicPaused = False
hiddenSprites = pygame.sprite.OrderedUpdates()
screenRefresh = True
background = None

keydict = {"space": pygame.K_SPACE, "esc": pygame.K_ESCAPE, "up": pygame.K_UP, "down": pygame.K_DOWN, # Dictionary translating PyGame 'event key presses' for any key presses we decide to incorporate into the game
           "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "return": pygame.K_RETURN,
           "a": pygame.K_a,
           "b": pygame.K_b,
           "c": pygame.K_c,
           "d": pygame.K_d,
           "e": pygame.K_e,
           "f": pygame.K_f,
           "g": pygame.K_g,
           "h": pygame.K_h,
           "i": pygame.K_i,
           "j": pygame.K_j,
           "k": pygame.K_k,
           "l": pygame.K_l,
           "m": pygame.K_m,
           "n": pygame.K_n,
           "o": pygame.K_o,
           "p": pygame.K_p,
           "q": pygame.K_q,
           "r": pygame.K_r,
           "s": pygame.K_s,
           "t": pygame.K_t,
           "u": pygame.K_u,
           "v": pygame.K_v,
           "w": pygame.K_w,
           "x": pygame.K_x,
           "y": pygame.K_y,
           "z": pygame.K_z,
           "1": pygame.K_1,
           "2": pygame.K_2,
           "3": pygame.K_3,
           "4": pygame.K_4,
           "5": pygame.K_5,
           "6": pygame.K_6,
           "7": pygame.K_7,
           "8": pygame.K_8,
           "9": pygame.K_9,
           "0": pygame.K_0}
screen = ""


class Background():                                                             # Class for Background of screen
    def __init__(self):                                                         # Initializing the class
        self.colour = pygame.Color("black")

    def setColour(self, colour):                                                # Setting the colour of the background and updating the screen
        self.colour = parseColour(colour)
        screen.fill(self.colour)
        pygame.display.update()
        self.surface = screen.copy()


class newSprite(pygame.sprite.Sprite):                                          # Class for creating new Sprite
    def __init__(self, filename, frames=1):
        pygame.sprite.Sprite.__init__(self)                                     # Loading image and setting the height/width of it
        self.images = []
        img = loadImage(filename)
        self.originalWidth = img.get_width() // frames
        self.originalHeight = img.get_height()
        frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)      # Setting frame data for images
        x = 0
        for frameNo in range(frames):
            frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)  # Drawing image corresponding to frame data
            frameSurf.blit(img, (x, 0))
            self.images.append(frameSurf.copy())
            x -= self.originalWidth
        self.image = pygame.Surface.copy(self.images[0])

        self.currentImage = 0                                       # Setting attributes for dimensions of sprite image
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 1

    # Bananas Falling
    def update(self):                       # Method which updates y-co ordinate, allowing bananas to fall
        self.rect.y += 4                    # LINES 104 - 115 SOURCED FROM STEVE PAGET

    def addImage(self, filename):           # Adding image to class
        self.images.append(loadImage(filename))

    def move(self, xpos, ypos, centre=False):   # Allowing movement of sprite by readjusting x and y co-ords
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]

class Block(newSprite):                 # Creating class for enemies
    def __init__(self, filename, frames=1):         # Lines 116, 117 and 119 and 130-154 original code from previous versions
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = loadImage(filename)
        self.originalWidth = img.get_width() // frames
        self.originalHeight = img.get_height()

        frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)  # SEE LINE 84 FOR FRAME DATA
        x = 0
        for frameNo in range(frames):
            frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
            frameSurf.blit(img, (x, 0))
            self.images.append(frameSurf.copy())
            x -= self.originalWidth
        self.image = pygame.Surface.copy(self.images[0])

        self.currentImage = 0                    # Setting parameters of the image loaded
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.scale = 1

                                                # The "center" the sprite will orbit
        self.center_x = 0
        self.center_y = 0

        self.radius = 0

                                                # How fast to orbit, in radians per frame
        self.speed = 0.05

    # Rotation
    def update(self):                           # Self-incrementing circular motion/rotation
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y + 1

        self.angle += self.speed

        if self.rect.y>700:
            self.rect.y = self.radius * math.cos(self.angle) + self.center_y + 1 # LINES 156 - 284 SOURCED FROM STEVE PAGET

    def addImage(self, filename):               # Adding image to class
        self.images.append(loadImage(filename))

    def move(self, xpos, ypos, centre=False):   # Allowing movement corresponding to x and y co-ordinates
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]

def loadImage(fileName, useColorKey=False):     # Method to allow loading Imagery
    if os.path.isfile(fileName):
        image = pygame.image.load(fileName)
        image = image.convert_alpha()
        # Return the image
        return image
    else:
        raise Exception("Error loading image: " + fileName + " - Check filename and path?")


def screenSize(sizex, sizey, xpos=None, ypos=None, fullscreen=False):           # Method creating the window of the game to be run on
    global screen
    global background
    if xpos != None and ypos != None:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (xpos, ypos + 50)
    else:
        windowInfo = pygame.display.Info()
        monitorWidth = windowInfo.current_w
        monitorHeight = windowInfo.current_h
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % ((monitorWidth - sizex) / 2, (monitorHeight - sizey) / 2)
    if fullscreen:
        screen = pygame.display.set_mode([sizex, sizey], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode([sizex, sizey])
    background = Background()
    screen.fill(background.colour)
    pygame.display.set_caption("Graphics Window")
    background.surface = screen.copy()
    pygame.display.update()
    return screen


def moveSprite(sprite, x, y, centre=False):         # Re-adjusts position of sprite object on screen
    sprite.move(x, y, centre)
    if screenRefresh:
        updateDisplay()

def killSprite(sprite):                             # Kills the sprite
    sprite.kill()
    if screenRefresh:
        updateDisplay()

def touching(sprite1, sprite2):                     # Returns true value if two sprites are touching
    collided = pygame.sprite.collide_mask(sprite1, sprite2)
    return collided

def setBackgroundColour(colour):                    # Sets background colour
    background.setColour(colour)
    if screenRefresh:
        updateDisplay()

def showSprite(sprite):                             # Displays sprite object on screen
    spriteGroup.add(sprite)
    if screenRefresh:
        updateDisplay()


def makeSprite(filename, frames=1):                 # Creates the sprite object using a loaded image
    thisSprite = newSprite(filename, frames)
    return thisSprite

def pause(milliseconds, allowEsc=True):             # Method to freeze the application
    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()
    waittime = current_time + milliseconds
    updateDisplay()
    while not (current_time > waittime or (keys[pygame.K_ESCAPE] and allowEsc)):
        pygame.event.clear()
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_ESCAPE] and allowEsc):
            pygame.quit()
            sys.exit()
        current_time = pygame.time.get_ticks()

def updateShapes():             # Update images on screen
    pygame.display.update()

def end():                      # Exit the application
    pygame.quit()

def keyPressed(keyCheck=""):    # Detects key inputs
    global keydict
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if sum(keys) > 0:
        if keyCheck == "" or keys[keydict[keyCheck.lower()]]:
            return True
    return False

def tick(fps):                  # Decides the amount of frames that will pass in one second
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_ESCAPE]):
        pygame.quit()
        sys.exit()
    gameClock.tick(fps)
    return gameClock.get_fps()

def updateDisplay():            # Updates the screen including sprite objects and textboxs as well as detecting key press to exit game
    global background
    spriteRects = spriteGroup.draw(screen)
    textboxRects = textboxGroup.draw(screen)
    pygame.display.update()
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_ESCAPE]):
        pygame.quit()
        sys.exit()
    spriteGroup.clear(screen, background.surface)
    textboxGroup.clear(screen, background.surface)

def parseColour(colour):        # Detects valid colour has been chosen
    if type(colour) == str:
        # check to see if valid colour
        return pygame.Color(colour)
    else:
        colourRGB = pygame.Color("white")
        colourRGB.r = colour[0]
        colourRGB.g = colour[1]
        colourRGB.b = colour[2]
        return colourRGB

def setAutoUpdate(val):         # Refreshing the screen
    global screenRefresh
    screenRefresh = val
