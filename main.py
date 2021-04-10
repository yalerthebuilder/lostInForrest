import pygame
import os
import random

# k_2 data
k2_width, k2_height = 250, 250
gameWindow = pygame.display.set_mode((k2_width, k2_height))
pygame.display.set_caption("Lost in the Wood")

white = (255, 255, 255)

# run the game at 60 frames per second
FPS = 200
velocity = 50
person_width = 50
person_height = 50

# direction
choices = ["up", "down", "left", "right"]
# image
alpha = (255, 255, 255)
forrestImage = pygame.image.load(os.path.join('images', "forrest.jpg"))
person_One_Image = pygame.image.load(os.path.join('images', "pat.png"))
person_One_Image.convert_alpha()
person_One_Image.set_colorkey(alpha)

person_Two_Image = pygame.image.load(os.path.join('images', "person2.png"))
person_Two_Image.convert_alpha()
person_Two_Image.set_colorkey(alpha)

# sound
pygame.mixer.init(44100, -16, 2, 2048)
game_sound = pygame.mixer.Sound("sound/soundTrack.mp3")


def displayGameWindow(player_one_container, player_two_container):
    gameWindow.fill(white)
    gameWindow.blit(forrestImage, (0, 0))
    gameWindow.blit(person_One_Image, (player_one_container.x, player_one_container.y))
    gameWindow.blit(person_Two_Image, (player_two_container.x, player_two_container.y))
    pygame.display.update()


def player_one_random_movement(player_one_container):
    choice = random.choice(choices)
    print(choice)
    if choice == "up" and player_one_container.y >= 50:
        player_one_container.y -= velocity
    if choice == "down" and player_one_container.y <= k2_height - 50:
        player_one_container.y += velocity
    if choice == "left" and player_one_container.x >= 50:
        player_one_container.x -= velocity
    if choice == "right" and player_one_container.x <= k2_width - 50:
        player_one_container.x += velocity


def player_two_random_movement(player_two_container):
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
    # move left
    if key_pressed[pygame.K_a]:
        player_one_container.x -= 50
    # move right
    if key_pressed[pygame.K_d]:
        player_one_container.x += 50
        # move up
    if key_pressed[pygame.K_w]:
        player_one_container.y -= 50
    # move down
    if key_pressed[pygame.K_s]:
        player_one_container.y += 50


def player_two_movement(key_pressed, player_two_container):
    # move left
    if key_pressed[pygame.K_LEFT]:
        player_two_container.x -= 50
    # move right
    if key_pressed[pygame.K_RIGHT]:
        player_two_container.x += 50
        # move up
    if key_pressed[pygame.K_UP]:
        player_two_container.y -= 50
    # move down
    if key_pressed[pygame.K_DOWN]:
        player_two_container.y += 50


def k_2_counterStimulation():
    player_one_container = pygame.Rect(0, 0, person_width, person_height)
    player_two_container = pygame.Rect(k2_width - person_width, k2_height - person_height, person_width, person_height)
    clock = pygame.time.Clock()
    is_GameOver = True
    stepCounter = 0
    while is_GameOver:
        pygame.mixer.Sound.play(game_sound)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_GameOver = False
            # if they meet game over
            if player_one_container.x == player_two_container.x and player_one_container.y == player_two_container.y:
                is_GameOver = False

        key_pressed = pygame.key.get_pressed()

        # player_one_movement(key_pressed, player_one_container)
        # player_two_movement(key_pressed, player_two_container)
        # if player_one_container.x >= 0 and player_one_container.x <= 1280 and player_one_container.x >= 0
        player_one_random_movement(player_one_container)
        stepCounter += 1
        player_two_random_movement(player_two_container)
        stepCounter += 1
        displayGameWindow(player_one_container, player_two_container)
    print(stepCounter)
    pygame.quit()


k_2_counterStimulation()
