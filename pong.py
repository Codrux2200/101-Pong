#!/usr/bin/python3
##
## EPITECH PROJECT, 2020
## undefined
## File description:
## pong
##
import pygame
import random
from pygame.locals import *
pygame.init() 
surface = pygame.display.set_mode((800,600))
pygame.display.set_caption("PongEpitech")
continuer = True
barre = pygame.Rect(400, -300, 20, 1200)
barrelat = [Rect(0, -20, 1800, 20), Rect(0, 600, 1800, 20)]
paddle_1 = []
paddle_2 = []
x = 300
x1 = 300
go = bool((random.randint(0,1)))
bas = False
haut = False
compteur = 0
compteur2 = 0
start = False
xc = 400
yc = 300
calibri_font = pygame.font.SysFont("Arial", 70)
calibri_font2 = pygame.font.SysFont("Arial", 20)

def keyboard():
    global x,x1,start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                start = True
    if start == True:       
        keyboard = pygame.key.get_pressed()
        if keyboard[K_UP]: 
            x1 = x1 - 5 
        if keyboard[K_DOWN]:
            x1 = x1 + 5
        if keyboard[K_z]:
            x = x - 5 
        if keyboard[K_s]:
            x = x + 5

def screen():
    global compteur,calibri_font,compteur2
    surface.fill((0, 0, 0))
    argent_text_surface = calibri_font.render(str(compteur),True,(255,255,255))
    argent_text_surface2 = calibri_font.render(str(compteur2),True,(255,255,255))
    surface.blit(argent_text_surface2, (750,50))
    surface.blit(argent_text_surface, (50,50))   
    pygame.draw.rect(surface, (255, 255, 255), barre)
    
def rect():
    global x,x1,paddle_1,paddle_2
    d = 0
    s = 0
    paddle_1.insert(0, Rect(10, x, 20, 20))
    paddle_1.insert(1, Rect(10, x + 20, 20, 35))
    paddle_1.insert(2, Rect(10, x - 35, 20, 35))
    paddle_2.insert(0, Rect(770, x1, 20, 20))
    paddle_2.insert(1, Rect(770, x1 + 20, 20, 35))
    paddle_2.insert(2, Rect(770, x1 - 35, 20, 35))

while continuer:
    pygame.time.Clock().tick(60)
    paddle_1 = []
    paddle_2 = []
    paddle = [paddle_2, paddle_1]
    rect()
    keyboard()
    pygame.draw.circle(surface, (0,0,255), (xc,yc), 10)
    circle = pygame.Rect(xc - 6, yc - 6, 14, 14)

    for v in range(len(paddle_1)):
        pygame.draw.rect(surface,(255, 0, 0),paddle_1[v])
        pygame.draw.rect(surface,(0, 255, 0),paddle_2[v])
        
    if bas == False and haut == False:
        c = 6
    for v in range(len(paddle)):
        if (circle.collidelist(paddle[v]) != -1):
            go = bool(v)
            pygame.mixer.music.load("./sound/ballon.mp3")
            pygame.mixer.music.play(start = 0.09)
            if ( circle.collidelist(paddle[v]) == 1):
                haut = False
                bas = True
            if ( circle.collidelist(paddle[v]) == 2):
                bas = False
                haut = True
            if ( circle.collidelist(paddle[v]) == 0):
                bas = False
                haut = False

    if (paddle_2[2].colliderect(barrelat[0])):
        x1 = x1 + 5
    if (paddle_2[1].colliderect(barrelat[1])):
        x1 = x1 - 5
    if (paddle_1[2].colliderect(barrelat[0])):
        x = x + 5
    if (paddle_1[1].colliderect(barrelat[1])):
        x = x - 5
           
    if ( circle.collidelist(barrelat) != -1):
        pygame.mixer.music.load("./sound/ballon.mp3")
        pygame.mixer.music.play(start = 0.09)
        if bas == True:
            bas = False
            haut = True
        elif haut == True:
            bas = True
            haut = False
            
    if start == True:
        if go == False:
            xc = xc - c
        else:
            xc = xc + c
        if bas == True:
            yc = yc - 5
            c = 5
        if haut == True:
            yc = yc + 5
            c = 5
    else:
        x = 300
        x1 = 300
        haut = False
        bas = False
        argent_text_surface3 = calibri_font2.render("up = K_UP",True,(255,255,255))
        surface.blit(argent_text_surface3, (650,120))
        argent_text_surface3 = calibri_font2.render("Down = K_DOWN",True,(255,255,255))
        surface.blit(argent_text_surface3, (600,140))
        argent_text_surface4 = calibri_font2.render("up = Z",True,(255,255,255))
        surface.blit(argent_text_surface4, (10,120))
        argent_text_surface4 = calibri_font2.render("Down = S",True,(255,255,255))
        surface.blit(argent_text_surface4, (10,140))
        argent_text_surface5 = calibri_font2.render("PRESS SPACE TO BEGIN",True,(255,255,255))
        surface.blit(argent_text_surface5, (450,300))
        
    if (xc <= -10 or xc >= 820):
        pygame.mixer.music.load("./sound/defaite.mp3")
        pygame.mixer.music.play(start = 0.5)
        start = False
        if xc < 0:
            compteur2 += 1
            go = True
        else:
            compteur += 1
            go = False
        xc = 400
        yc = 300
    
    pygame.display.flip()
    screen()
    
pygame.quit()