from pygeocoder import Geocoder
import pyscreenshot as ImageGrab
import time
import webbrowser
import sys 
import pygame


class Geo():
    place1 = raw_input("Please input a location: ")
    place2 = Geocoder.geocode(place1)


    print (place2[0])
    print (place2[0].coordinates)
    place3 = (place2[0])
    urlExtention = place2[0].coordinates
    print urlExtention


    strUrlExt = str(urlExtention)
    place4 = str(place3)


    strUrlExt = strUrlExt.replace('(','').replace(')','').replace(' ','')
    print strUrlExt


    mapsUrl2 = "https://www.google.co.uk/maps/@" + strUrlExt + ",12z"
    print mapsUrl2
    webbrowser.open_new(mapsUrl2)
time.sleep(1.5)


class imageGrab():
    box = (0,190,1200,1100)
    im = ImageGrab.grab().crop(box).save("screenshot.bmp","BMP")


class displayCreate():
    pygame.init()
    background = pygame.image.load("screenshot.bmp")
    backgroundRect = background.get_rect()

    size = (width, height) = background.get_size()
    screen = pygame.display.set_mode(size)

    screen.blit(background, backgroundRect)
    pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()



    