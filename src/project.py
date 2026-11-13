import pygame
import sys

pygame.init()

#main menu window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visual Novel")
clock = pygame.time.Clock()

#Font features and colors
title_font = pygame.font.SysFont("arial", 54, bold=True)
btn_font = pygame.font.SysFont("arial", 32)
WHITE, RED, PINK = (255, 255, 255), (255, 0, 0), (255, 182, 193)

#Buttons size and shape