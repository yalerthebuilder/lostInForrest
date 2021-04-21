import pygame
import os
import sys
import random

pygame.init()

white = (255, 255, 255)

# run the game at 60 frames per second
FPS = 60
velocity = 10
person_width = 5
person_height = 5

# direction
choices = ["up", "down", "left", "right"]

# color
alpha = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)


# sound
pygame.mixer.init(44100, -16, 2, 2048)
game_sound = pygame.mixer.Sound("sound/spooky.mp3")
game_sound.set_volume(0.01)
celebration_sound = pygame.mixer.Sound("sound/auld.mp3")
collision_sound_loader = pygame.mixer.Sound("sound/hitWall.mp3")


def displayGameWindow(gameWindow, forrestImage, player_one_container, player_two_container, person_One_Image, person_Two_Image, ):
    """

    :param forrestImage: forrest image
    :param person_Two_Image: display person one image
    :param person_One_Image: display person two image
    :param gameWindow: game window
    :param player_one_container: player_one position
    :param player_two_container: player_two position
    :return: NONE

    """
    gameWindow.fill(white)
    gameWindow.blit(forrestImage, (0, 0))
    gameWindow.blit(person_One_Image, (player_one_container.x, player_one_container.y))
    gameWindow.blit(person_Two_Image, (player_two_container.x, player_two_container.y))
    pygame.display.update()


def displayGameOverWindow(gameWindow, gameOverImage,stepCounter):
    """

    :param stepCounter:
    :param gameWindow: window to display games
    :param gameOverImage: the image to display after game is over
    :return: NONE

    """
    game_sound.stop()
    pygame.mixer.Sound.play(celebration_sound)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render(str(stepCounter)+ " steps", True, red, alpha)
    textRect = text.get_rect()
    start_time = pygame.time.get_ticks()
    pygame.display.set_caption("Congrats, You've beat the game")
    while pygame.time.get_ticks() < start_time+3000:
        gameWindow.fill(white)
        gameWindow.blit(gameOverImage, (0, 0))
        gameWindow.blit(text, textRect)
        pygame.display.update()
    sys.exit()


def player_one_random_movement(player_one_Container, width, height):
    """

    :param height: window height
    :param width: window width
    :param player_one_Container: player 1 location update after move a step
    :return: NONE
    """
    choice = random.choice(choices)

    if choice == "left":
        if player_one_Container.x >= 5:
            player_one_Container.x -= velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)

    if choice == "right" and player_one_Container.x <= width - 50:
        if player_one_Container.x <= width - 50:
            player_one_Container.x += velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)

    if choice == "up":
        if player_one_Container.y >= 5:
            player_one_Container.x -= velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
        player_one_Container.y -= velocity

    if choice == "down":
        if player_one_Container.y <= height - 50:
            player_one_Container.y += velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)


def player_two_random_movement(player_two_Container, width, height):
    """

    :param player_two_Container:  player two container
    :param height: window height
    :param width: window width
    :return: NONE

    """
    choice = random.choice(choices)
    if choice == "left":
        if player_two_Container.x >= 5:
            player_two_Container.x -= velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)

    if choice == "right" and player_two_Container.x <= width - 50:
        if player_two_Container.x <= width - 50:
            player_two_Container.x += velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)

    if choice == "up":
        if player_two_Container.y >= 5:
            player_two_Container.x -= velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
        player_two_Container.y -= velocity

    if choice == "down":
        if player_two_Container.y <= height - 50:
            player_two_Container.y += velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)


def player_one_movement(key_pressed, player_one_container, stepCounter, width, height):
    """

    :param height: window height
    :param width: window width
    :param stepCounter: counter for steps
    :param key_pressed: when user enter a key
    :param player_one_container: player 1 position
    :return: NONE

    """
    stepCounter += 1
    print(stepCounter)
    # move left
    if key_pressed[pygame.K_a]:
        if player_one_container.x >= 5:
            player_one_container.x -= velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
    # move right
    if key_pressed[pygame.K_d]:
        if player_one_container.x <= width - 50:
            player_one_container.x += velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
    # move up
    if key_pressed[pygame.K_w]:
        if player_one_container.y >= 5:
            player_one_container.y -= velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
    # move down
    if key_pressed[pygame.K_s]:
        if player_one_container.y <= height - 50:
            player_one_container.y += velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)


def player_two_movement(key_pressed, player_two_container, stepCounter, width, height):
    """

    :param height: window height
    :param width: window width
    :param stepCounter: counter for steps
    :param key_pressed: when user enter a key
    :param player_two_container: player 2 position
    :return:

    """
    stepCounter += 1
    print(stepCounter)
    # move left
    if key_pressed[pygame.K_LEFT]:
        if player_two_container.x >= 5:
            player_two_container.x -= velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
    # move right
    if key_pressed[pygame.K_RIGHT]:
        if player_two_container.x <= width - 50:
            player_two_container.x += velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
        # move up
    if key_pressed[pygame.K_UP]:
        if player_two_container.y >= 5:
            player_two_container.y -= velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
    # move down
    if key_pressed[pygame.K_DOWN]:
        if player_two_container.y <= height - 50:
            player_two_container.y += velocity
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)


def k_2_autoStimulation():
    """

    stimulate the k_2 student lost in forrest game
    :return: NONE

    """
    pygame.init()
    pygame.mixer.init()
    player_one_container = pygame.Rect(0, 0, person_width, person_height)

    # map data
    width, height = 500, 500
    gameWindow = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lost in the Wood")

    # forrest image
    forrestImage = pygame.image.load(os.path.join('images', "500map.jpg"))

    # gameover image
    gameOverImage = pygame.image.load(os.path.join('images', "500gameover.jpg"))

    # person one image
    person_One_Image = pygame.image.load(os.path.join('images', "pat.png"))
    person_One_Image.convert_alpha()
    person_One_Image.set_colorkey(alpha)

    # person two image
    person_Two_Image = pygame.image.load(os.path.join('images', "spongebob.png"))
    person_Two_Image.convert_alpha()
    person_Two_Image.set_colorkey(alpha)

    player_two_container = pygame.Rect(width - person_width, height - person_height, person_width, person_height)
    clock = pygame.time.Clock()
    is_GameOver = False
    stepCounter = 0
    while not is_GameOver:
        game_sound.play(-1)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_GameOver = True
                displayGameOverWindow(gameWindow, gameOverImage=gameOverImage)
            # if they meet game over
            if abs(player_one_container.x - player_two_container.x) <= 50 and abs(
                    player_one_container.y - player_two_container.y) <= 50:
                is_GameOver = False
                displayGameOverWindow(gameWindow,gameOverImage)

        key_pressed = pygame.key.get_pressed()
        if key_pressed:
            stepCounter += 1
        player_one_random_movement(player_one_container,width, height)
        player_two_random_movement(player_two_container,width, height)
        displayGameWindow(gameWindow,
                          player_one_container=player_one_container,
                          forrestImage=forrestImage,
                          player_two_container=player_two_container,
                          person_One_Image=person_One_Image,
                          person_Two_Image=person_Two_Image)
    print(stepCounter)
    sys.exit()


def map300_manuelStimulation():
    """

    stimulate the k_2 student lost in forrest game
    :return: NONE

    """
    pygame.init()
    pygame.mixer.init()
    player_one_container = pygame.Rect(0, 0, person_width, person_height)

    # map data
    width, height = 300, 300
    gameWindow = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lost in the Wood")

    # forrest image
    forrestImage = pygame.image.load(os.path.join('images', "300map.jpg"))

    # person one image
    person_One_Image = pygame.image.load(os.path.join('images', "pat.png"))
    person_One_Image.convert_alpha()
    person_One_Image.set_colorkey(alpha)

    # person two image
    person_Two_Image = pygame.image.load(os.path.join('images', "spongebob.png"))
    person_Two_Image.convert_alpha()
    person_Two_Image.set_colorkey(alpha)

    # game over image
    gameOverImage = pygame.image.load(os.path.join('images', "300gameover.jpg"))

    player_two_container = pygame.Rect(width - person_width, height - person_height, person_width, person_height)
    clock = pygame.time.Clock()
    is_GameOver = False
    stepCounter = 0
    while not is_GameOver:
        game_sound.play(-1)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_GameOver = True
                displayGameOverWindow(gameWindow, gameOverImage=gameOverImage, stepCounter=stepCounter)
            # if they meet game over
            if abs(player_one_container.x - player_two_container.x) <= 50 and abs(
                    player_one_container.y - player_two_container.y) <= 50:
                is_GameOver = False
                displayGameOverWindow(gameWindow, gameOverImage=gameOverImage, stepCounter=stepCounter)

        key_pressed = pygame.key.get_pressed()
        if key_pressed:
            stepCounter += 1
        player_one_movement(key_pressed, player_one_container, stepCounter, width, height)
        player_two_movement(key_pressed, player_two_container, stepCounter, width, height)
        displayGameWindow(gameWindow,
                          player_one_container=player_one_container,
                          forrestImage=forrestImage,
                          player_two_container=player_two_container,
                          person_One_Image=person_One_Image,
                          person_Two_Image=person_Two_Image)
    print(stepCounter)
    sys.exit()


def map500_manuelStimulation():
    """

    stimulate the k_2 student lost in forrest game
    :return: NONE

    """
    pygame.init()
    pygame.mixer.init()
    player_one_container = pygame.Rect(0, 0, person_width, person_height)

    # map data
    width, height = 500, 500
    gameWindow = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lost in the Wood")

    # forrest image
    forrestImage = pygame.image.load(os.path.join('images', "500map.jpg"))

    # person one image
    person_One_Image = pygame.image.load(os.path.join('images', "pat.png"))
    person_One_Image.convert_alpha()
    person_One_Image.set_colorkey(alpha)

    # person two image
    person_Two_Image = pygame.image.load(os.path.join('images', "spongebob.png"))
    person_Two_Image.convert_alpha()
    person_Two_Image.set_colorkey(alpha)

    # game over image
    gameOverImage = pygame.image.load(os.path.join('images', "500gameover.jpg"))

    player_two_container = pygame.Rect(width - person_width, height - person_height, person_width, person_height)
    clock = pygame.time.Clock()
    is_GameOver = False
    stepCounter = 0
    while not is_GameOver:
        game_sound.play(-1)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_GameOver = True
                displayGameOverWindow(gameWindow, gameOverImage=gameOverImage, stepCounter=stepCounter)
            # if they meet game over
            if abs(player_one_container.x - player_two_container.x) <= 50 and abs(
                    player_one_container.y - player_two_container.y) <= 50:
                is_GameOver = False
                displayGameOverWindow(gameWindow,gameOverImage=gameOverImage, stepCounter=stepCounter)

        key_pressed = pygame.key.get_pressed()
        if key_pressed:
            stepCounter += 1
        player_one_movement(key_pressed, player_one_container, stepCounter, width, height)
        player_two_movement(key_pressed, player_two_container, stepCounter, width, height)
        displayGameWindow(gameWindow,
                          player_one_container=player_one_container,
                          forrestImage=forrestImage,
                          player_two_container=player_two_container,
                          person_One_Image=person_One_Image,
                          person_Two_Image=person_Two_Image)
    print(stepCounter)
    sys.exit()


def forrest_manuelStimulation():
    """

    stimulate the k_2 student lost in forrest game
    :return: NONE

    """
    pygame.init()
    pygame.mixer.init()
    player_one_container = pygame.Rect(0, 0, person_width, person_height)

    # map data
    width, height = 1280, 600
    gameWindow = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lost in the Wood")

    # forrest image
    forrestImage = pygame.image.load(os.path.join('images', "forrest.jpg"))

    # person one image
    person_One_Image = pygame.image.load(os.path.join('images', "pat.png"))
    person_One_Image.convert_alpha()
    person_One_Image.set_colorkey(alpha)

    # person two image
    person_Two_Image = pygame.image.load(os.path.join('images', "spongebob.png"))
    person_Two_Image.convert_alpha()
    person_Two_Image.set_colorkey(alpha)

    # game over image
    gameOverImage = pygame.image.load(os.path.join('images', "forrestgameover.jpg"))

    player_two_container = pygame.Rect(width - person_width, height - person_height, person_width, person_height)
    clock = pygame.time.Clock()
    is_GameOver = False
    stepCounter = 0
    while not is_GameOver:
        game_sound.play(-1)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_GameOver = True
                displayGameOverWindow(gameWindow, gameOverImage=gameOverImage, stepCounter=stepCounter)
            # if they meet game over
            if abs(player_one_container.x - player_two_container.x) <= 50 and abs(
                    player_one_container.y - player_two_container.y) <= 50:
                is_GameOver = False
                displayGameOverWindow(gameWindow,gameOverImage=gameOverImage, stepCounter=stepCounter)

        key_pressed = pygame.key.get_pressed()
        if key_pressed:
            stepCounter += 1
        player_one_movement(key_pressed, player_one_container, stepCounter, width, height)
        player_two_movement(key_pressed, player_two_container, stepCounter, width, height)
        displayGameWindow(gameWindow,
                          player_one_container=player_one_container,
                          forrestImage=forrestImage,
                          player_two_container=player_two_container,
                          person_One_Image=person_One_Image,
                          person_Two_Image=person_Two_Image)
    print(stepCounter)
    sys.exit()


def vanGogh_Map_manuelStimulation():
    """

    stimulate the k_2 student lost in forrest game
    :return: NONE

    """
    player_one_container = pygame.Rect(0, 0, person_width, person_height)

    # map data
    width, height = 1200, 800
    gameWindow = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lost in the Wood")

    # forrest image
    forrestImage = pygame.image.load(os.path.join('images', "vanmap.jpg"))

    # person one image
    person_One_Image = pygame.image.load(os.path.join('images', "pat.png"))
    person_One_Image.convert_alpha()
    person_One_Image.set_colorkey(alpha)

    # person two image
    person_Two_Image = pygame.image.load(os.path.join('images', "spongebob.png"))
    person_Two_Image.convert_alpha()
    person_Two_Image.set_colorkey(alpha)

    # game over image
    gameOverImage = pygame.image.load(os.path.join('images', "forrestgameover.jpg"))

    player_two_container = pygame.Rect(width - person_width, height - person_height, person_width, person_height)
    clock = pygame.time.Clock()
    is_GameOver = False
    stepCounter = 0
    while not is_GameOver:
        game_sound.play(-1)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_GameOver = True
                displayGameOverWindow(gameWindow, gameOverImage=gameOverImage, stepCounter=stepCounter)
            # if they meet game over
            if abs(player_one_container.x - player_two_container.x) <= 50 and abs(
                    player_one_container.y - player_two_container.y) <= 50:
                is_GameOver = False
                displayGameOverWindow(gameWindow,gameOverImage=gameOverImage, stepCounter=stepCounter)

        key_pressed = pygame.key.get_pressed()
        if key_pressed:
            stepCounter += 1
        player_one_movement(key_pressed, player_one_container, stepCounter, width, height)
        player_two_movement(key_pressed, player_two_container, stepCounter, width, height)
        displayGameWindow(gameWindow,
                          player_one_container=player_one_container,
                          forrestImage=forrestImage,
                          player_two_container=player_two_container,
                          person_One_Image=person_One_Image,
                          person_Two_Image=person_Two_Image)
    print(stepCounter)
    sys.exit()


def Map2560_manuelStimulation():
    """

    stimulate the k_2 student lost in forrest game
    :return: NONE

    """
    player_one_container = pygame.Rect(0, 0, person_width, person_height)

    # map data
    width, height = 2560, 1600
    gameWindow = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lost in the Wood")

    # forrest image
    forrestImage = pygame.image.load(os.path.join('images', "2560map.jpg"))

    # person one image
    person_One_Image = pygame.image.load(os.path.join('images', "pat.png"))
    person_One_Image.convert_alpha()
    person_One_Image.set_colorkey(alpha)

    # person two image
    person_Two_Image = pygame.image.load(os.path.join('images', "spongebob.png"))
    person_Two_Image.convert_alpha()
    person_Two_Image.set_colorkey(alpha)

    # game over image
    gameOverImage = pygame.image.load(os.path.join('images', "2560gameover.jpg"))

    player_two_container = pygame.Rect(width - person_width, height - person_height, person_width, person_height)
    clock = pygame.time.Clock()
    is_GameOver = False
    stepCounter = 0
    while not is_GameOver:
        game_sound.play(-1)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_GameOver = True
                displayGameOverWindow(gameWindow, gameOverImage=gameOverImage, stepCounter=stepCounter)
            # if they meet game over
            if abs(player_one_container.x - player_two_container.x) <= 50 and abs(
                    player_one_container.y - player_two_container.y) <= 50:
                is_GameOver = False
                displayGameOverWindow(gameWindow,gameOverImage=gameOverImage, stepCounter=stepCounter)

        key_pressed = pygame.key.get_pressed()
        if key_pressed:
            stepCounter += 1
        player_one_movement(key_pressed, player_one_container, stepCounter, width, height)
        player_two_movement(key_pressed, player_two_container, stepCounter, width, height)
        displayGameWindow(gameWindow,
                          player_one_container=player_one_container,
                          forrestImage=forrestImage,
                          player_two_container=player_two_container,
                          person_One_Image=person_One_Image,
                          person_Two_Image=person_Two_Image)
    print(stepCounter)
    sys.exit()


def menu():
    print("Choose your level of difficulty")
    print("1 for rocket map(300*300) *easy")
    print("2 for forrest map(500*500) *medium")
    print("3 for Van Gogh map (1280*800) *Hard")
    print("4 for MYSTERY map (2560*1600) *Very Hard")
    selection = int(input("Select Your game mode"))
    while selection not in [1,2,3,4]:
        print("Instuction not found")
        selection = int(input("Select Your game mode"))
    if selection == 1:
        map300_manuelStimulation()
    if selection == 2:
        map500_manuelStimulation()
    if selection == 3:
        vanGogh_Map_manuelStimulation()
    if selection == 4:
        Map2560_manuelStimulation()





