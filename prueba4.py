# -*- coding: utf-8 -*
import sys, pygame,os
from pygame.locals import *
import random
import math, operator
import Image

# Constantes
WIDTH = 300
HEIGHT = 300


def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image


def comparate(padre,hijo):
    im1=Image.open(padre).histogram()
    im2=Image.open(hijo).histogram()
    rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, im1, im2))/len(im1))
    return rms

def main():
    generation=0
    TRANSPARENT = (255,0,255)
    fondo="imagenes/white.jpg"
    radio=10
    PADRE = "imagenes/padre.jpg"
    ORIGINAL = "imagenes/perrito.jpg"
    HIJO = "imagenes/hijo.jpg"
    pygame.init()
    #aptitud_padre=comparate(ORIGINAL,PADRE)
    color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    posicion=(random.randint(0,WIDTH),random.randint(0,HEIGHT))
    screen = pygame.display.set_mode((300,300))
    surf1 = pygame.Surface((500,500))
    surf1.fill(TRANSPARENT)
    surf1.set_colorkey(TRANSPARENT)
    pygame.draw.circle(surf1,color,posicion, radio)
    surf1.set_alpha(100)
    background_image = load_image(fondo)
    screen.blit(background_image, (0, 0))
    screen.blit(surf1, (0,0))
    pygame.display.flip()
    pygame.image.save(screen,PADRE)
    aptitud_padre=comparate(ORIGINAL,PADRE)
    fondo=PADRE
    while True:
        color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        posicion=(random.randint(0,WIDTH),random.randint(0,HEIGHT))
        screen = pygame.display.set_mode((300,300))
        surf1 = pygame.Surface((500,500))
        surf1.fill(TRANSPARENT)
        surf1.set_colorkey(TRANSPARENT)
        pygame.draw.circle(surf1,color,posicion, radio)
        surf1.set_alpha(100)
        background_image = load_image(fondo)
        screen.blit(background_image, (0, 0))
        screen.blit(surf1, (0,0))
        pygame.display.flip()
        pygame.image.save(screen,HIJO)
        aptitud_hijo=comparate(ORIGINAL,HIJO)
        if aptitud_hijo < aptitud_padre:
            #Realzamos reemplazo
            os.remove(PADRE)
            aptitud_padre=aptitud_hijo
            os.rename(HIJO,PADRE)
            fondo= PADRE
        else:
            os.remove(HIJO)
            fondo =PADRE
    return 0

if __name__ == '__main__':
    pygame.init()
    main()