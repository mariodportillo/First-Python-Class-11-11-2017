import pygame
import time
pygame.init()
pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 30)

width = 400
height = 300
screen = pygame.display.set_mode((width,height))
done = False
is_blue = True
is_blue2 = True
Paddle1x = 350
Paddle1y = 50
Paddle2x = 60
Paddle2y = 50
Circlex = 200
Circley = 150
Circlexv = 3
Circleyv = 0
score1 = 0
score2 = 0
while not done: 
    Circlex += Circlexv
    Circley += Circleyv
    textsurface = myfont.render(str(score1), False, (255, 255,255 ))
    screen.blit(textsurface,(150,10))
    textsurface = myfont.render(str(score2), False, (255, 255,255 ))
    screen.blit(textsurface,(250,10))

    if Circley <= 0:
        Circleyv = -Circleyv
    if Circley >= height:
        Circleyv = -abs(Circleyv)
    if Circlex >= Paddle1x and Circley >= Paddle1y and Circley <= Paddle1y + 100:
        Circlexv = -abs(Circlexv) 
        d = Circley - Paddle1y
        if d <= 50:
            Circleyv = -3
        else:
             Circleyv = 3 
    if Circlex <= Paddle2x + 10  and Circley >= Paddle2y and Circley <= Paddle2y + 100:
        Circlexv = -Circlexv
        d = Circley - Paddle2y
        print("circlex: " + str(Circlex))
        if d <= 50:
            Circleyv = -3
        else:
             Circleyv = 3
        
    if Circlex >= 400: 
        Circlex = 200
        Circley = 150
        Circleyv = 0
        Circlexv = -3
        score1 = score1 + 1
    if Circlex <= 0: 
        Circlex = 200
        Circley = 150
        Circleyv = 0
        Circlexv = 3
        score2 = score2 + 1 
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: Paddle1y -= 5
    if pressed[pygame.K_DOWN]: Paddle1y += 5
    if pressed[pygame.K_w]: Paddle2y -= 5
    if pressed[pygame.K_s]: Paddle2y += 5
    for event in pygame.event.get():
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        if is_blue2: color = (0, 128, 255)
        else: color = (255, 100, 0)

    if event.type == pygame.QUIT:
            done = True  
    pygame.display.flip()
    if is_blue: color = (0, 128, 255)
    else: color = (255, 100, 0)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, pygame.Rect(Paddle1x, Paddle1y, 10, 100))
    pygame.draw.rect(screen, color, pygame.Rect(Paddle2x, Paddle2y, 10, 100))
    pygame.draw.circle(screen, (230,25,250) , (Circlex, Circley), 15)
    if score1 == 10:
        textsurface = myfont.render("Player 1 Wins!", False, (255, 255,255 ))
        text_rect = textsurface.get_rect(center=(width/2, height/2))
        screen.blit(textsurface, text_rect)
        pygame.display.flip()
        time.sleep(2)
        done = True
    elif score2 == 10:
        textsurface = myfont.render("Player 2 Wins!", False, (255, 255,255 ))
        text_rect = textsurface.get_rect(center=(width/2, height/2))
        screen.blit(textsurface,text_rect)
        pygame.display.flip()
        time.sleep(2)
        done = True