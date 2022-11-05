import pygame
 
#init
pygame.mixer.init()

music = "a"

if(music=="a"):
    pygame.mixer.music.load("/home/pi/Documents/Hermes/asset/music_a.mp3")
else:
   pygame.mixer.music.load("/home/pi/Documents/Hermes/asset/music_b.mp3") 
 
pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
    continue


def changeMusic(newMusic):
    global music
    music = newMusic

def endMusic():
    pygame.mixer.music.stop()