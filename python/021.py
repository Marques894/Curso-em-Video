# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('/home/augustti/Documents/VSCode/Studys/Curso_em_Video/python/021_anosluz.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)