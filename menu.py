import pygame
import sys
import os
from pygame.locals import *
import engine

# sound
pygame.mixer.init(44100, -16, 2, 2048)
game_sound = pygame.mixer.Sound("sound/spooky.mp3")
game_sound.set_volume(0.01)
game_sound.play()

mainClock = pygame.time.Clock()

pygame.init()
pygame.display.set_caption('LOST IN FORREST')
screen = pygame.display.set_mode((500, 500), 0, 32)
menuPicture = pygame.image.load(os.path.join('images', "menuImage.jpg"))
font = pygame.font.Font('freesansbold.ttf', 20)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    click = False
    while True:
        screen.fill((0, 0, 0))
        screen.blit(menuPicture, (0, 0))
        draw_text('ESC "exit"', font, (255, 255, 255), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        # rect( x, y, len, width)
        button_1 = pygame.Rect(150, 100, 200, 50)
        button_2 = pygame.Rect(150, 200, 200, 50)
        button_3 = pygame.Rect(150, 300, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                print("Game")
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                print("Options")
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                print("Credits")
                credit()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        draw_text('Start', font, (255, 255, 255), screen, 220, 100)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        draw_text('Option', font, (255, 255, 255), screen, 220, 200)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Credit', font, (255, 255, 255), screen, 220, 300)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def game():
    gameClick = False
    running = True
    print("Selected Game")
    while running:
        # allow user to pick game mode
        screen.fill((0, 0, 0))
        screen.blit(menuPicture, (0, 0))
        draw_text('ESC "Menu"', font, (255, 255, 255), screen, 20, 20)
        draw_text('Select Level Of Difficulty', font, (255, 255, 255), screen, 20, 50)

        mx, my = pygame.mouse.get_pos()

        # button attribute
        button_1 = pygame.Rect(150, 100, 200, 50)
        button_2 = pygame.Rect(150, 200, 200, 50)
        button_3 = pygame.Rect(150, 300, 200, 50)
        button_4 = pygame.Rect(150, 400, 200, 50)

        if button_1.collidepoint((mx, my)):
            if gameClick:
                easyMode()
        if button_2.collidepoint((mx, my)):
            if gameClick:
                mediumMode()
        if button_3.collidepoint((mx, my)):
            if gameClick:
                hardMode()
        if button_4.collidepoint((mx, my)):
            if gameClick:
                hellMode()

        # draw button
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        draw_text('Easy', font, (255, 255, 255), screen, 220, 100)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        draw_text('Medium', font, (255, 255, 255), screen, 220, 200)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Hard', font, (255, 255, 255), screen, 220, 300)
        pygame.draw.rect(screen, (255, 0, 0), button_4)
        draw_text('Hell', font, (255, 255, 255), screen, 220, 400)

        gameClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    gameClick = True

        pygame.display.update()
        mainClock.tick(60)


def easyMode():
    '''

    :return: easy mode active
    '''
    print("Easy Mode Selected")
    engine.map300_manuelStimulation()


def mediumMode():
    '''

    :return: easy mode active
    '''
    print("Medium Mode Selected")
    engine.map500_manuelStimulation()


def hardMode():
    '''

    :return: hard mode active
    '''
    print("Hard Mode Selected")
    engine.vanGogh_Map_manuelStimulation()


def hellMode():
    '''

    :return: hell mode active
    '''
    print("Hell Mode Selected")
    engine.Map2560_manuelStimulation()


def options():
    """

    :return: option page
    """
    optionClick = False
    running = True
    while running:
        # allow user to pick game mode
        screen.fill((0, 0, 0))
        screen.blit(menuPicture, (0, 0))
        draw_text('ESC "Menu"', font, (255, 255, 255), screen, 20, 20)
        draw_text('Select Sound Volume', font, (255, 255, 255), screen, 20, 50)

        mx, my = pygame.mouse.get_pos()

        # button attribute
        button_1 = pygame.Rect(150, 100, 200, 50)
        button_2 = pygame.Rect(150, 200, 200, 50)
        button_3 = pygame.Rect(150, 300, 200, 50)

        if button_1.collidepoint((mx, my)):
            if optionClick:
                set_Volume_Low()
        if button_2.collidepoint((mx, my)):
            if optionClick:
                set_Volume_Medium()
        if button_3.collidepoint((mx, my)):
            if optionClick:
                set_Volume_High()


        pygame.draw.rect(screen, (255, 0, 0), button_1)
        draw_text('Volume Low', font, (255, 255, 255), screen, 180, 100)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        draw_text('Volume Medium', font, (255, 255, 255), screen, 180, 200)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
        draw_text('Volume High', font, (255, 255, 255), screen, 180, 300)

        optionClick = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    optionClick = True

        pygame.display.update()
        mainClock.tick(60)


def set_Volume_Low():
    game_sound.set_volume(0.01)


def set_Volume_Medium():
    game_sound.set_volume(0.1)


def set_Volume_High():
    game_sound.set_volume(0.5)


def credit():
    """

    :return: credit page
    """
    while True:
        draw_text('ESC "Menu"', font, (255, 255, 255), screen, 20, 20)
        screen.fill((0, 0, 0))
        screen.blit(menuPicture, (0, 0))
        draw_text('Credit:', font, (255, 255, 255), screen, 20, 20)
        draw_text('COSC 445W', font, (255, 255, 255), screen, 20, 50)
        draw_text('Dr. Fadi Wedyan', font, (255, 255, 255), screen, 20, 80)
        draw_text('Lost In Forrest Team', font, (255, 255, 255), screen, 20, 110)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

        pygame.display.update()
        mainClock.tick(60)

main_menu()
