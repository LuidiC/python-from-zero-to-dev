# Desafio 21
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame

print('=' * 5  + ' DESAFIO 21 ' + '=' * 5)

pygame.mixer.init()

pygame.mixer.music.load("desafio-aula08.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)