import pygame,time
# ################################################################################### player 1
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

boomAnimStep1 = pygame.image.load("assets\explosion\step1.png")
boomAnimStep2 = pygame.image.load("assets\explosion\step2.png")
boomAnimStep3 = pygame.image.load("assets\explosion\step3.png")
boomAnimStep4 = pygame.image.load("assets\explosion\step4.png")
boomAnimStep5 = pygame.image.load("assets\explosion\step5.png")
boomAnimStep6 = pygame.image.load("assets\explosion\step6.png")
boomAnimStep7 = pygame.image.load("assets\explosion\step7.png")


# ################################################################################# player 2
posFaceStep1_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_05.png")
posFaceStep2_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_06.png")
posFaceStep3_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_07.png")

posBackStep1_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_08.png")
posBackStep2_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_09.png")
posBackStep3_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_10.png")

posLeftStep1_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_20.png")
posLeftStep2_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_21.png")
posLeftStep3_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_22.png")

posRightStep1_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_17.png")
posRightStep2_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_18.png")
posRightStep3_p2 = pygame.image.load("assets\PNG\Default size\Player\p2\player_19.png")

boomAnim = [boomAnimStep1,boomAnimStep2,boomAnimStep3,boomAnimStep4,boomAnimStep5,boomAnimStep6,boomAnimStep7]

boomAnimCount = 0

playerPos = posFaceStep1
player2Pos= posFaceStep1_p2

animArray1 = [posFaceStep1,posFaceStep2, posFaceStep1, posFaceStep3]
animArray2 = [posBackStep1,posBackStep2, posBackStep1, posBackStep3]
animArray3 = [posRightStep1, posRightStep2, posRightStep1, posRightStep3]
animArray4 = [posLeftStep1, posLeftStep2, posLeftStep1, posLeftStep3]


animArray1_p2 = [posFaceStep1_p2,posFaceStep2_p2, posFaceStep1_p2, posFaceStep3_p2]
animArray2_p2 = [posBackStep1_p2,posBackStep2_p2, posBackStep1_p2, posBackStep3_p2]
animArray3_p2 = [posRightStep1_p2,posRightStep2_p2, posRightStep1_p2, posRightStep3_p2]
animArray4_p2 = [posLeftStep1_p2,posLeftStep2_p2, posLeftStep1_p2, posLeftStep3_p2]

animArray = animArray1
animArray_p2 = animArray1_p2

animCount = 0

animationTime = int(time.clock() * 10**3)
animationSkipTime = 150