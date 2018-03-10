from Const import *

done = True

window = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.Surface((screen_width, screen_height))
screen.fill((80, 80, 80))
player1 = pygame.Surface((rect_width, rect_height))
player1.fill((90, 140, 200))
player2 = pygame.Surface((rect_width, rect_height))
player2.fill((90, 160, 90))


def draw_bomb(screen, color, X, Y, width, height, arr, count):
    if count >= 5:
        count = 0
        # screen.fill((80,80,80))
    arr[count] = X, Y
    pygame.draw.rect(screen, color, (X, Y, width, height), 5)

    print(arr)
    print(count)
    return count

def refresh():
    pass
while done:
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
                y1_speed = 0
                x1_speed = 2
            if e.key == pygame.K_a:
                y1_speed = 0
                x1_speed = -2
            if e.key == pygame.K_w:
                x1_speed = 0
                y1_speed = -2
            if e.key == pygame.K_s:
                x1_speed = 0
                y1_speed = 2
            if e.key == pygame.K_SPACE:
                bomb_count1 = draw_bomb(screen,(90, 140, 200),player1_x + rect_width / 2 - bomb_width / 2, player1_y + rect_height / 2 - bomb_height / 2, bomb_width, bomb_height, bomb_p1, bomb_count1)
                bomb_count1 += 1

            # arrows move (player 2)
            if e.key == pygame.K_RIGHT:
                y2_speed = 0
                x2_speed = 2
            if e.key == pygame.K_LEFT:
                y2_speed = 0
                x2_speed = -2
            if e.key == pygame.K_UP:
                x2_speed = 0
                y2_speed = -2
            if e.key == pygame.K_DOWN:
                x2_speed = 0
                y2_speed = 2
            if e.key == pygame.K_k:
                bomb_count2 = draw_bomb(screen, (90, 160, 90), player2_x + rect_width / 2 - bomb_width / 2, player2_y + rect_height / 2 - bomb_height / 2, bomb_width,bomb_height, bomb_p2,bomb_count2)
                bomb_count2 += 1

    for pos in bomb_p1:
        try:
            if (player2_x <= pos[0] <= player2_x + rect_width) and (player2_y <= pos[1] <= player2_y + rect_height):
                print("p1 win")
                pygame.time.delay(1000)
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
                print("p2 win")
                pygame.time.delay(1000)
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

    if player1_x <=0:
        x1_speed = -x1_speed
    if player1_x >= screen_width - rect_width:
        x1_speed = -x1_speed
    if player1_y <= 0:
        y1_speed = -y1_speed
    if player1_y >= screen_height - rect_height:
        y1_speed = -y1_speed

    if player2_x <= 0:
        x2_speed = -x2_speed
    if player2_x >= screen_width - rect_width:
        x2_speed = -x2_speed
    if player2_y <= 0:
        y2_speed = -y2_speed
    if player2_y >= screen_height - rect_height:
        y2_speed = -y2_speed

    player1_x += x1_speed
    player1_y += y1_speed

    player2_x += x2_speed
    player2_y += y2_speed

    window.blit(screen, (0, 0))
    window.blit(player1, (player1_x,player1_y))
    window.blit(player2,(player2_x, player2_y))
    # if timer != int(time.clock()):
    #     timer = int(time.clock())
    #     screen.fill((80, 80, 80))
    #     print("updated")
    pygame.display.flip()
