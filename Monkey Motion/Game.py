from pygame_functions import *				# Importing all functions and classes from pygame_functions
import random								# Importing random class for RNG

os.chdir("D:\College\Second Year 2\Disciplinary Team Project\Monkey Motion")		# Changing directory for correct pathing on files

screenSize(1400, 650, 70, 40)			# Setting the window size and x and y position on screen of a computer
setBackgroundColour([64,102,209])		# Setting background colour

monkey = makeSprite("images/hero.png")		# Loading Monkey image
moveSprite(monkey, 280, 500)				# Setting position
showSprite(monkey)							# Displaying the object on screen


										# Old code from previous versions of the game
										# Spawned two clouds that moved downwards and changed positions randomly past a certain height
										# ***Could not get it to work on this version***
'''
def cloud():
		global cloud_y
		global cloud_x
		global cloud_x2
		global cloud_y2
		screen.blit(cloudImg, (cloud_x, cloud_y))
		screen.blit(cloudImg, (cloud_x2, cloud_y2))
		cloud_y += 4
		cloud_y2 += 4
		if cloud_y > displayHeight and cloud_y2 > displayHeight:
				cloud_x = random.randint(-20, displayWidth-800)
				cloud_x2 = random.randint(750, displayWidth-450)
				cloud_y = random.randint(-288, -211)
				cloud_y2 = random.randint(-288, -211)
'''

cloud = newSprite("images/bigcloud.png")				# Creating cloud sprites and placing them on screen
cloud_2 = newSprite("images/bigcloud.png")
moveSprite(cloud, -20, -100)
moveSprite(cloud_2, 900, -100)
showSprite(cloud)
showSprite(cloud_2)

banana_list = pygame.sprite.Group()						# Creating new group of sprites to be inserted into
def bananaSpawn():
    for i in range(random.randint(20,25),random.randint(30,35)):		# Creating a method to spawn a varied number of bananas between the ranges of 20 - 35
        banana_copy = newSprite("images/banana.png")
        moveSprite(banana_copy, random.randrange(0,1350), random.randrange(-475,-50))
        showSprite(banana_copy)
        banana_list.add(banana_copy)									# Adding each banana created into the group banana_list


xpos = 0				# X position of Monkey
xspeed = 0				# Variables created for speed and acceleration of monkey
raccel = 0
laccel = 0

timer = 30				# Timer for the bananas to spawn & reset
banana_count = 0		# Counter for banana
score = 90				# Score tracking hits received from enemy

enemy_list = pygame.sprite.Group()			# Creating new group of sprites for enemy
for i in range(12):							# Adding 12 enemy sprites
    enemy_copy = Block("images/unhero2.png")								# Importing sprites and setting location to orbit in circular motion
    moveSprite(enemy_copy, random.randrange(1400), random.randrange(700))
    enemy_copy.radius = random.randrange(500,1300)

    enemy_copy.angle = random.random() * 2 * math.pi

    enemy_copy.speed = -0.008
    showSprite(enemy_copy)
    enemy_list.add(enemy_copy)

while True:							# While loop to keep pygame running
    if keyPressed("right"):			# Adding left and right acceleration for left and right movement when keys are pressed
        raccel = -0.3
    else:
        raccel = 0

    if keyPressed("left"):
        laccel = +0.3
    else:
        laccel = 0

    if xpos<0:						# Preventing monkey sprite from going off-screen
        xspeed = 1
        moveSprite(monkey,0,500)
    elif xpos>1300:
        xspeed = -1
        moveSprite(monkey,1300,500)

    banana_hit=pygame.sprite.spritecollide(monkey, banana_list, True)		# If a collision occurs between the monkey and a banana, the sprite will be killed
    #if pygame.sprite.collide_rect(monkey, banana_list):					*** Code not in use as we had difficulties getting the banana score system to work***
    #    ++banana_count
    #    print (banana_count)
    banana_list.update()

    enemy_hit=pygame.sprite.spritecollide(monkey, enemy_list, True)			# If a collision occurs between monkey and enemy, the sprite will be killed
    enemy_list.update()

    timer += 0.1				# Timer for respawning the bananas once they reach the end of the screen
    if timer > 30:
        timer = 0
        bananaSpawn()

    xpos += xspeed					# Adding speed to the monkey so that it's always moving and never static
    moveSprite(monkey, xpos, 500)
    xspeed -= 0.1 + raccel			# Acceleration for both movements
    xspeed += 0.1 - laccel
    tick(60)						# Running the game at 60 frames per second
