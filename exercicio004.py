import pygame # Importa biblioteca pygame
pygame.mixer.init() # Inicia o mixer
pygame.mixer.music.load('exercicio4.mp3') # Carrega o meu arquivo mp3
pygame.mixer.music.play() # Toca o mp3

# Espera até o áudio terminar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)