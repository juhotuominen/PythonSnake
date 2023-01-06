import pygame
import random


pygame.init()

black=(0,0,0,)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)

dis_width = 800
dis_height = 600

display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake")

head_img = pygame.image.load("images/snake_head.png").convert()
body_img = pygame.image.load("images/snake_body.png").convert()
apple_img = pygame.image.load("images/apple.png").convert()

clock = pygame.time.Clock()
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Score: " + str(score), True, white)
    display.blit(value, [0, 0])

def our_snake(snake_list):
    for x in snake_list:
        display.blit(body_img, [x[0], x[1]])
    display.blit(head_img, [x[0], x [1]])

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [150, 250])


def game_loop():
    running = True
    game_over = False

    x1 = 370
    y1 = 270
    dx1 = 0
    dy1 = 0

    snake_list = []
    lenght_of_snake = 1

    foodx = round(random.randrange(0, dis_width - 40) / 10.0) * 10
    foody = round(random.randrange(0, dis_height - 40) / 10.0) * 10

    while running:

        while game_over == True:
            display.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx1 = -10
                    dy1 = 0
                elif event.key == pygame.K_RIGHT:
                    dx1 = 10
                    dy1 = 0
                elif event.key == pygame.K_UP:
                    dx1 = 0
                    dy1 = -10
                elif event.key == pygame.K_DOWN:
                    dx1 = 0
                    dy1 = 10
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += dx1
        y1 += dy1
        display.fill(black)
        display.blit(apple_img, [foodx, foody])

        rect_snake = pygame.Rect(x1, y1, 40, 40)
        rect_apple = pygame.Rect(foodx+10, foody+10, 22, 22)

        collide = rect_snake.colliderect(rect_apple)

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > lenght_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_over = True
        
        our_snake(snake_list)
        your_score(lenght_of_snake - 1)

        pygame.display.update()

        if collide:
            foodx = round(random.randrange(0, dis_width - 40) / 10.0) * 10
            foody = round(random.randrange(0, dis_height - 40) / 10.0) * 10
            lenght_of_snake += 1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()