# Importing pygame
from pygame_functions import *

os.chdir("D:\College\Second Year 2\Disciplinary Team Project\Monkey Motion")

# Configuring the screen parameters
screenSize(1000, 750)

# Dummy Player Sprite
player = makeSprite("images/Player.png")

# Enemy boss sprite
theBoss = makeSprite("images/Boss Sheet Right.png", 8)

# Showing the sprites and setting the coordinates
showSprite(theBoss)
moveSprite(theBoss, 200, 400, True)

showSprite(player)
moveSprite(player, 500, 700, True)

# The second and third frame of the boss sprite
# nextFrame = clock()
# frame = 0

# while True:
#     if clock() > nextFrame:
#         frame = (frame + 1) % 8
#         nextFrame += 80
#
#
# if keyPressed("right"):
#         changeSpriteImage(theBoss, 0 * 8 + frame)

for x in range(10, 1000):
        moveSprite(theBoss, x, 400)
        pause(1)

for x in range(10, 1000):
        moveSprite(theBoss, x, 200)
        pause(1)

for x in range(10, 1000):
        moveSprite(theBoss, x, 100)
        pause(1)

# Moving the boss to the player
if touching(theBoss, player):
        killSprite(player)
