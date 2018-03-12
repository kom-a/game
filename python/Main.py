from Const import *

done = True

window = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.Surface((screen_width, screen_height))
# screen.fill((80, 80, 80))
screen.fill((244, 255, 193))
# player1 = pygame.Surface((rect_width, rect_height))
# player1 = posFaceStep1
# player1.fill((90, 140, 200))
# player2 = pygame.Surface((rect_width, rect_height))
# player2.fill((90, 160, 90))
player2 = posFaceStep1


def draw_bomb(screen, color, X, Y, width, height, arr, count):
    soundTick.play()
    if count >= 5:
        count = 0
        # screen.fill((80,80,80))
    arr[count] = X, Y
    # pygame.draw.rect(screen, color, (X, Y, width, height), 5)
    screen.blit(bombPNG, (X, Y))
    print(arr)
    return count


def boom(x, y):
    for pos in boomAnim:
        window.blit(pos, (x, y))
        pygame.time.delay(75)
        screen.fill((244,255,193))
        pygame.display.flip()




while done:
    timeNow = time.time() * 10**9
    delta += timeNow - lastTime
    lastTime = timeNow
    animationTime = int(time.clock() * 10 ** 3)

    if animationTime - animationSkipTime > 150:
        animationSkipTime += 150
        animCount += 1

        if animCount == len(animArray):
            animCount = 0
        if animCount == len(animArray_p2):
            animCount = 0

        playerPos = animArray[animCount]
        player2Pos = animArray_p2[animCount]
    if delta >= PartTime:
        # events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
            if e.type == pygame.KEYDOWN:
                # wasd move (player 1)

                # @!!!!!!!!!@!!!!!!!!!@!!!!!!!!!@!!!!!!!!!@!!!!!!!!!@!!!!!!!!!@!!!!!!!!!@!!!!!!!!!@!!!!!!!!!@!!!!!!!!!@
                if e.key == pygame.K_ESCAPE:
                    done = False
                if e.key == pygame.K_d:
                    animArray = animArray3
                    y1_speed = 0
                    x1_speed = 4
                if e.key == pygame.K_a:
                    animArray = animArray4
                    y1_speed = 0
                    x1_speed = -4
                if e.key == pygame.K_w:
                    animArray = animArray2
                    x1_speed = 0
                    y1_speed = -4
                if e.key == pygame.K_s:
                    animArray = animArray1
                    x1_speed = 0
                    y1_speed = 4
                if e.key == pygame.K_SPACE:

                    bomb_count1 = draw_bomb(screen,(90, 140, 200),player1_x + rect_width / 2 - bomb_width / 2, player1_y + rect_height / 2 - bomb_height / 2, bomb_width, bomb_height, bomb_p1, bomb_count1)
                    bomb_count1 += 1

                # arrows move (player 2)
                if e.key == pygame.K_RIGHT:
                    animArray_p2 = animArray3_p2
                    y2_speed = 0
                    x2_speed = 4
                if e.key == pygame.K_LEFT:
                    animArray_p2 = animArray4_p2
                    y2_speed = 0
                    x2_speed = -4
                if e.key == pygame.K_UP:
                    animArray_p2 = animArray2_p2
                    x2_speed = 0
                    y2_speed = -4
                if e.key == pygame.K_DOWN:
                    animArray_p2 = animArray1_p2
                    x2_speed = 0
                    y2_speed = 4
                if e.key == pygame.K_k:
                    bomb_count2 = draw_bomb(screen, (90, 160, 90), player2_x + rect_width / 2 - bomb_width / 2, player2_y + rect_height / 2 - bomb_height / 2, bomb_width,bomb_height, bomb_p2,bomb_count2)
                    bomb_count2 += 1


        for pos in bomb_p1:
            try:
                if (player2_x <= pos[0] <= player2_x + rect_width) and (player2_y <= pos[1] <= player2_y + rect_height):
                    soundBoom.play()
                    boom(pos[0], pos[1])
                    print("p1 win")
                    window.blit(goal_font.render('p1 WIN', 3, (0, 0, 0)),
                                (screen_width / 2 - 140, screen_height / 2 - 80))
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    screen.fill((244, 255, 193))
                    player1_x = 50
                    player1_y = 50
                    player2_x = screen_width - 50 - rect_width
                    player2_y = screen_height - 50 - rect_height

                    x1_speed = 0
                    y1_speed = 0

                    x2_speed = 0
                    y2_speed = 0

                    bomb_p1 = [[], [], [], [], []]
                    bomb_p2 = [[], [], [], [], []]

                    bomb_count1 = 0
                    bomb_count2 = 0

            except IndexError:
                pass

        for pos in bomb_p2:
            try:
                if (player1_x <= pos[0] <= player1_x + rect_width) and (player1_y <= pos[1] <= player1_y + rect_height):
                    soundBoom.play()
                    boom(pos[0], pos[1])
                    window.blit(goal_font.render('p2 WIN', 3, (0, 0, 0)),
                                (screen_width / 2 - 140, screen_height / 2 - 80))
                    pygame.display.flip()
                    print("p2 win")
                    pygame.time.delay(1000)
                    screen.fill((244, 255, 193))
                    player1_x = 50
                    player1_y = 50
                    player2_x = screen_width - 50 - rect_width
                    player2_y = screen_height - 50 - rect_height

                    x1_speed = 0
                    y1_speed = 0

                    x2_speed = 0
                    y2_speed = 0

                    bomb_p1 = [[], [], [], [], []]
                    bomb_p2 = [[], [], [], [], []]

                    bomb_count1 = 0
                    bomb_count2 = 0

            except IndexError:
                pass

        if player1_x <= 0:
            animArray = animArray3
            x1_speed = -x1_speed
        if player1_x >= screen_width - rect_width:
            animArray = animArray4
            x1_speed = -x1_speed
        if player1_y <= 0:
            animArray = animArray1
            y1_speed = -y1_speed
        if player1_y >= screen_height - rect_height:
            animArray = animArray2
            y1_speed = -y1_speed

        if player2_x <= 0:
            animArray_p2 = animArray3_p2
            x2_speed = -x2_speed
        if player2_x >= screen_width - rect_width:
            animArray_p2 = animArray4_p2
            x2_speed = -x2_speed
        if player2_y <= 0:
            animArray_p2 = animArray1_p2
            y2_speed = -y2_speed
        if player2_y >= screen_height - rect_height:
            animArray_p2 = animArray2_p2
            y2_speed = -y2_speed

        player1_x += x1_speed
        player1_y += y1_speed

        player2_x += x2_speed
        player2_y += y2_speed

        window.blit(screen, (0, 0))
        window.blit(playerPos, (player1_x, player1_y))
        window.blit(player2Pos,(player2_x, player2_y))
        
        # pygame.display.flip()
        updates += 1
        delta = 0
    pygame.display.flip()
    frames += 1
		
    if (time.time() * 10**3 - timer > 1000):
        timer += 1000
        pygame.display.set_caption("updates: " + str(frames) + "  |  " + "frames: " + str(updates))
       # print("updates: " + str(frames) + "  |  " + "frames: " + str(updates))
        updates = 0
        frames = 0
    if mytimer != int(time.clock()):
        mytimer = int(time.clock())
        screen.fill((244, 255, 193))
        print("updated")            