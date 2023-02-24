import pygame

# Inicia o mixer do pygame
pygame.mixer.init()

# Iniciando o pygame
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()
print('Obrigado')
