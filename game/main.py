import pygame
import os
from button import Button

pygame.font.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
PAUSE_FONT = pygame.font.SysFont('comicsans',20)
INSTRUCTIONS_FONT = pygame.font.SysFont('comicsans',10)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
MENU_TITLE = pygame.font.SysFont("comicsans", 30)
MENU_BUTTON = pygame.font.SysFont("comicsans", 20)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

BACKGROUND_MENU = pygame.transform.scale(
    pygame.image.load("assets/buttons/Background.png"), (400, 400))
BACKGROUND_OPTION = pygame.transform.scale(
    pygame.image.load("assets/buttons/background_option.png"), (200, 50))



def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    text_menu = PAUSE_FONT.render("PRESS ESC TO MENU",1,WHITE)
    INSTRUCTIONS = INSTRUCTIONS_FONT.render("INSTRUCTIONS",1,RED)
    UP_INSTRUCCION = INSTRUCTIONS_FONT.render("UP = W",1,WHITE)
    DOWN_INSTRUCCION = INSTRUCTIONS_FONT.render("DOWN = S",1,WHITE)
    LEFT_INSTRUCCION = INSTRUCTIONS_FONT.render("LEFT = D.",1,WHITE)
    RIGTH_INSTRUCCION = INSTRUCTIONS_FONT.render("RIGTH = A",1,WHITE)
    SHOOT_INSTRUCCION = INSTRUCTIONS_FONT.render("SHOOT = SPACE",1,WHITE)

    
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    WIN.blit(text_menu, (((WIDTH - red_health_text.get_width()) /2 ),(HEIGHT - text_menu.get_height())))

    '''WIN.blit(UP_INSTRUCCION, (10, 10))
    WIN.blit(DOWN_INSTRUCCION, (10, 10))
    WIN.blit(LEFT_INSTRUCCION, (10, 10))
    WIN.blit(RIGTH_INSTRUCCION, (10, 10))'''
    WIN.blit(INSTRUCTIONS, (10, WIN.get_height() - (INSTRUCTIONS.get_height()*6)))
    WIN.blit(UP_INSTRUCCION, (10, WIN.get_height() - (UP_INSTRUCCION.get_height()*5)))
    WIN.blit(DOWN_INSTRUCCION, (10, WIN.get_height() - (DOWN_INSTRUCCION.get_height()*4)))
    WIN.blit(LEFT_INSTRUCCION, (10, WIN.get_height() - (LEFT_INSTRUCCION.get_height()*3)))
    WIN.blit(RIGTH_INSTRUCCION, (10, WIN.get_height() - (RIGTH_INSTRUCCION.get_height()*2)))
    WIN.blit(SHOOT_INSTRUCCION, (10, WIN.get_height() - SHOOT_INSTRUCCION.get_height()))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL


def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    menu_active = False
    action = ""
    while run:
        clock.tick(FPS)
        if menu_active == True:
            action = menu()
            if(action == "CONTINUE"):
                menu_active = False
            if(action == "RESET"):
                break
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    #BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)

                if event.key == pygame.K_ESCAPE:
                    menu_active = True
                    

            if event.type == RED_HIT:
                red_health -= 1
                #BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                #BULLET_HIT_SOUND.play()

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow, red_bullets, yellow_bullets,
                    red_health, yellow_health)

    main()
    
def menu():
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    MENU_BOX_X = WIDTH/2 - (BACKGROUND_MENU.get_width()/2)
    MENU_BOX_Y = HEIGHT/2 - (BACKGROUND_MENU.get_height()/2)
    WIN.blit(BACKGROUND_MENU, (MENU_BOX_X, MENU_BOX_Y))

    MENU_TEXT = MENU_TITLE.render("MAIN MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(MENU_BOX_X + (BACKGROUND_MENU.get_width()/2) , MENU_BOX_Y + 40))
    WIN.blit(MENU_TEXT, MENU_RECT)
    PLAY_BUTTON = Button(BACKGROUND_OPTION, pos=(MENU_BOX_X +(BACKGROUND_MENU.get_width()/2) , MENU_BOX_Y + 150), 
                        text_input="Continue", font = MENU_BUTTON, base_color="#d7fcd4", hovering_color="White")
    RESET_BUTTON = Button(BACKGROUND_OPTION, pos=(MENU_BOX_X +(BACKGROUND_MENU.get_width()/2), MENU_BOX_Y +210), 
                        text_input="Reset", font=MENU_BUTTON, base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(BACKGROUND_OPTION, pos=(MENU_BOX_X +(BACKGROUND_MENU.get_width()/2), MENU_BOX_Y +270), 
                        text_input="Quit", font=MENU_BUTTON, base_color="#d7fcd4", hovering_color="White")
    
    for button in [PLAY_BUTTON, RESET_BUTTON, QUIT_BUTTON]:
        button.update(WIN)
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return "CONTINUE"
                if RESET_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return "RESET"
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()

    pygame.display.update()

if __name__ == "__main__":
    main()