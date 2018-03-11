import pygame
import time
import threading
pygame.init()
screen_width = 1280
screen_height = 720
# screen_width = 1920
# screen_height = 1080

rect_width = 50
rect_height = 50

player1_x = 50
player1_y = 50
player2_x = screen_width - 50 - rect_width
player2_y = screen_height - 50 - rect_height

x1_speed = 0
y1_speed = 0

x2_speed = 0
y2_speed = 0

bomb_width = 20
bomb_height = 20

bomb_p1 = [[], [], [], [], []]
bomb_p2 = [[], [], [], [], []]


bomb_count1 = 0
bomb_count2 = 0

timer = 0

PartTime = 1000000000.0 / 60.0
delta = 0
lastTime = time.time() * 10**9
timer = time.time() * 10**3

updates = 0
frames = 0
posStay = pygame.image.load("assets\PNG\Default size\Player\player_05.png")
bombPNG = pygame.image.load("bomb2.png")

soundTick = pygame.mixer.Sound("tick.ogg")
soundBoom = pygame.mixer.Sound("boom.ogg")