import pygame
import time
import threading
pygame.init()
pygame.font.init()
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
posFaceStep1 = pygame.image.load("assets\PNG\Default size\Player\player_05.png")
posFaceStep2 = pygame.image.load("assets\PNG\Default size\Player\player_06.png")
posFaceStep3 = pygame.image.load("assets\PNG\Default size\Player\player_07.png")

posBackStep1 = pygame.image.load("assets\PNG\Default size\Player\player_08.png")
posBackStep2 = pygame.image.load("assets\PNG\Default size\Player\player_09.png")
posBackStep3 = pygame.image.load("assets\PNG\Default size\Player\player_10.png")

posRightStep1 = pygame.image.load("assets\PNG\Default size\Player\player_17.png")
posRightStep2 = pygame.image.load("assets\PNG\Default size\Player\player_18.png")
posRightStep3 = pygame.image.load("assets\PNG\Default size\Player\player_19.png")

posLeftStep1 = pygame.image.load("assets\PNG\Default size\Player\player_20.png")
posLeftStep2 = pygame.image.load("assets\PNG\Default size\Player\player_21.png")
posLeftStep3 = pygame.image.load("assets\PNG\Default size\Player\player_22.png")

playerPos = posFaceStep1

animArray1 = [posFaceStep1,posFaceStep2, posFaceStep1, posFaceStep3]
animArray2 = [posBackStep1,posBackStep2, posBackStep1, posBackStep3]
animArray3 = [posRightStep1, posRightStep2, posRightStep1, posRightStep3]
animArray4 = [posLeftStep1, posLeftStep2, posLeftStep1, posLeftStep3]

animArray = animArray1

animCount = 0

bombPNG = pygame.image.load("bomb2.png")

soundTick = pygame.mixer.Sound("tick.ogg")
soundBoom = pygame.mixer.Sound("boom.ogg")

mytimer = int(time.clock())

goal_font = pygame.font.Font('BAUHS93.TTF', 100)

animationTime = int(time.clock() * 10**3)
animationSkipTime = 150
