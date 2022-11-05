import pygame
 
#init
pygame.mixer.init()
 
#load file
pygame.mixer.music.load("/home/pi/Documents/Hermes/2.mp3")
 
#play
pygame.mixer.music.play()
 
#끝까지 재생할때까지 기다린다.
while pygame.mixer.music.get_busy() == True:
    continue
    
# #다음 파일 재생    
# pygame.mixer.music.load("/home/poppy/poppy_audio/welcome.wav")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy() == True:
#     continue
    
# pygame.mixer.music.load("/home/poppy/poppy_audio/not_welcome.wav")
# pygame.mixer.music.play()