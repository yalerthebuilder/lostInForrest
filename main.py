import pygame
import os

width, height = 1280, 720
gameWindow = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lost in the Wood")

white = (255, 255, 255)

# run the game at 60 frames per second
FPS = 60
velocity = 5
person_width = 50
person_height = 50

# image
alpha = (255, 255, 255)
forrestImage = pygame.image.load(os.path.join('images', "forrest.jpg"))
person_One_Image = pygame.image.load(os.path.join('images', "person.png"))
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


# def person_handler(key_press, person)

def player_one_movement(key_pressed, player_one_container):
    # move left
    if key_pressed[pygame.K_a]:
        player_one_container.x -= 1
    # move right
    if key_pressed[pygame.K_d]:
        player_one_container.x += 1
        # move up
    if key_pressed[pygame.K_w]:
        player_one_container.y -= 1
    # move down
    if key_pressed[pygame.K_s]:
        player_one_container.y += 1


def player_two_movement(key_pressed, player_two_container):
    # move left
    if key_pressed[pygame.K_LEFT]:
        player_two_container.x -= 1
    # move right
    if key_pressed[pygame.K_RIGHT]:
        player_two_container.x += 1
        # move up
    if key_pressed[pygame.K_UP]:
        player_two_container.y -= 1
    # move down
    if key_pressed[pygame.K_DOWN]:
        player_two_container.y += 1


def main():
    player_one_container = pygame.Rect(0, 0, person_width, person_height)
    player_two_container = pygame.Rect(width - person_width, height - person_height, person_width, person_height)
    clock = pygame.time.Clock()
    is_GameOver = True

    while is_GameOver:
        pygame.mixer.Sound.play(game_sound)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_GameOver = False
            if abs(player_one_container.x - player_two_container.x) <= 100 and abs(player_one_container.y - player_two_container.y) <= 100:
                is_GameOver = False

        key_pressed = pygame.key.get_pressed()

        player_one_movement(key_pressed, player_one_container)
        player_two_movement(key_pressed, player_two_container)

        displayGameWindow(player_one_container, player_two_container)

    pygame.quit()


if __name__ == "__main__":
    main()
