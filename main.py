import pygame
import os
import random

# k_2 data
k2_width, k2_height = 1280, 600
gameWindow = pygame.display.set_mode((k2_width, k2_height))
pygame.display.set_caption("Lost in the Wood")

white = (255, 255, 255)

# run the game at 60 frames per second
FPS = 60
velocity = 2
person_width = 5
person_height = 5

# direction
choices = ["up", "down", "left", "right"]
# image
alpha = (255, 255, 255)
forrestImage = pygame.image.load(os.path.join('images', "forrest.jpg"))

# person one image
person_One_Image = pygame.image.load(os.path.join('images', "pat.png"))
person_One_Image.convert_alpha()
person_One_Image.set_colorkey(alpha)

# person two image
person_Two_Image = pygame.image.load(os.path.join('images', "person2.png"))
person_Two_Image.convert_alpha()
person_Two_Image.set_colorkey(alpha)

# sound
pygame.mixer.init(44100, -16, 2, 2048)
game_sound = pygame.mixer.Sound("sound/spooky.mp3")
game_sound.set_volume(0.01)
celebration_sound = pygame.mixer.Sound("sound/auld.mp3")
collision_sound_loader = pygame.mixer.Sound("sound/hitWall.mp3")

#pygame.mixer.music.play()


def displayGameWindow(player_one_container, player_two_container):
    """

    :param player_one_container: player_one position
    :param player_two_container: player_two position
    :return: NONE

    """
    gameWindow.fill(white)
    gameWindow.blit(forrestImage, (0, 0))
    gameWindow.blit(person_One_Image, (player_one_container.x, player_one_container.y))
    gameWindow.blit(person_Two_Image, (player_two_container.x, player_two_container.y))
    pygame.display.update()


def displayGameOverWindow():
    game_sound.stop()
    pygame.mixer.Sound.play(celebration_sound)
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() < start_time+3000:
        gameWindow.fill(white)
        gameOverImage = pygame.image.load(os.path.join('images', "gameover.jpg"))
        gameWindow.blit(gameOverImage, (0, 0))
        pygame.display.update()
    pygame.quit()


def player_one_random_movement(player_one_Container):
    """

    :param player_one_Container: player 1 location update after move a step
    :return: NONE
    """
    choice = random.choice(choices)
    if choice == "up" and player_one_Container.y >= 50:
        player_one_Container.y -= velocity
    if choice == "down" and player_one_Container.y <= k2_height - 50:
        player_one_Container.y += velocity
    if choice == "left" and player_one_Container.x >= 50:
        player_one_Container.x -= velocity
    if choice == "right" and player_one_Container.x <= k2_width - 50:
        player_one_Container.x += velocity


def player_two_random_movement(player_two_container):
    """

    :param player_two_container: player 2 location update after move a step
    :return: NONE

    """
    choice = random.choice(choices)
    if choice == "up" and player_two_container.y >= 50:
        player_two_container.y -= velocity
    if choice == "down" and player_two_container.y <= k2_height - 50:
        player_two_container.y += velocity
    if choice == "left" and player_two_container.x >= 50:
        player_two_container.x -= velocity
    if choice == "right" and player_two_container.x <= k2_width - 50:
        player_two_container.x += velocity


def player_one_movement(key_pressed, player_one_container):
    """

    :param key_pressed: when user enter a key
    :param player_one_container: player 1 position
    :return: NONE

    """

    # move left
    if key_pressed[pygame.K_a]:
        if player_one_container.x >= 5:
            player_one_container.x -= 5
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
    # move right
    if key_pressed[pygame.K_d]:
        if player_one_container.x <= k2_width - 50:
            player_one_container.x += 5
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
    # move up
    if key_pressed[pygame.K_w]:
        if player_one_container.y >= 5:
            player_one_container.y -= 5
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
    # move down
    if key_pressed[pygame.K_s]:
        if player_one_container.y <= k2_height - 50:
            player_one_container.y += 5
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)


def player_two_movement(key_pressed, player_two_container):
    """

    :param key_pressed: when user enter a key
    :param player_two_container: player 2 position
    :return:

    """
    # move left
    if key_pressed[pygame.K_LEFT]:
        if player_two_container.x >= 5:
            player_two_container.x -= 5
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
    # move right
    if key_pressed[pygame.K_RIGHT]:
        if player_two_container.x <= k2_width - 50:
            player_two_container.x += 5
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
        # move up
    if key_pressed[pygame.K_UP]:
        if player_two_container.y >= 5:
            player_two_container.y -= 5
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)
    # move down
    if key_pressed[pygame.K_DOWN]:
        if player_two_container.y <= k2_height - 50:
            player_two_container.y += 5
        else:
            pygame.mixer.Channel(0).play(collision_sound_loader, maxtime=600)



def auto_stimulation():
    """

    stimulate the k_2 student lost in forrest game
    :return: NONE

    """
    player_one_container = pygame.Rect(0, 0, person_width, person_height)
    player_two_container = pygame.Rect(1230, 550, person_width, person_height)
    clock = pygame.time.Clock()
    is_GameOver = True
    stepCounter = 0
    while is_GameOver:
        # pygame.mixer.Sound.play(game_sound)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_GameOver = False
            # if they meet game over
            if player_one_container.x == player_two_container.x and player_one_container.y == player_two_container.y:
                is_GameOver = False

        if 0 <= player_one_container.x <= 1280 and player_one_container.x >= 0:
            player_one_random_movement(player_one_container)
            stepCounter += 1
            player_two_random_movement(player_two_container)
            stepCounter += 1
            displayGameWindow(player_one_container, player_two_container)
    print(stepCounter)
    pygame.quit()


def k_2_counterStimulation():
    """

    stimulate the k_2 student lost in forrest game
    :return: NONE

    """
    player_one_container = pygame.Rect(0, 0, person_width, person_height)
    player_two_container = pygame.Rect(k2_width - person_width, k2_height - person_height, person_width, person_height)
    clock = pygame.time.Clock()
    is_GameOver = False
    stepCounter = 0
    while not is_GameOver:
        game_sound.play(-1)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_GameOver = True
                displayGameOverWindow()
            # if they meet game over
            if abs(player_one_container.x - player_two_container.x) <= 50 and abs(
                    player_one_container.y - player_two_container.y) <= 50:
                is_GameOver = False
                displayGameOverWindow()


        key_pressed = pygame.key.get_pressed()

        player_one_movement(key_pressed, player_one_container)
        player_two_movement(key_pressed, player_two_container)
        displayGameWindow(player_one_container, player_two_container)
    print(stepCounter)
    pygame.quit()


k_2_counterStimulation()

'''
def menu():
    print("Enter 1 for k2-stimulation")
    print("Enter 2 for auto-stimulation")
    gameMode = int(input("ENTER YOUR GAME MODE"))
    #if gameMode == 1:
    #    k_2_counterStimulation()
    #if gameMode == 2:
    #    auto_stimulation()
'''
