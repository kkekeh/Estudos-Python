# Faça um programa que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init()
pygame.init()

#pygame.mixer.music.load('música aqui')
pygame.mixer.music.play()
pygame.event.wait()
