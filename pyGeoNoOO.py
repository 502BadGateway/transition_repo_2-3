from pygeocoder import Geocoder
import pyscreenshot as ImageGrab
import time
import webbrowser
import sys 
import pygame
import urllib
import image

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


mapsUrl2 = "http://maps.googleapis.com/maps/api/staticmap?center=" + strUrlExt + "&zoom=12&format=png&sensor=false&size=640x480&maptype=roadmap&style=element:labels|visibility:off"
print mapsUrl2

resource = urllib.urlopen(mapsUrl2)
output = open("screenshot1.jpg","wb")
output.write(resource.read())

pygame.init()
background = pygame.image.load("screenshot1.jpg")
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

