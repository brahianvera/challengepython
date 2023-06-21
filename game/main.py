import pygame
import os
from button import Button

pygame.font.init()

def increment_event():
    global event_number
    event_number += 1
    return event_number

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SHIP COMBAT!")

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
SPACE_BELLOW_INSTRUCTIONS = 10
SPACE_BORDER_INSTRUCTIONS = 10
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
max_bullets_red = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
event_number = 0
YELLOW_HIT = pygame.USEREVENT + increment_event()
RED_HIT = pygame.USEREVENT + increment_event()


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
two_players = False


# MACHINE VARS
machines_vertical_direction = "UP"
machines_horizontal_direction = "LEFT"
SHOOT_MACHINE = pygame.USEREVENT + increment_event()
VEL_MACHINE = 7
TIME_SHOOTING = 300

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health,show_menu):
    txt_pause = "PRESS SPACE TO MENU"
    if show_menu:
       txt_pause = "PRESS SPACE TO CONTINUE"
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, WHITE)
    draw_instructions()
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    text_menu = PAUSE_FONT.render(txt_pause,1,WHITE)
    WIN.blit(text_menu, (((WIDTH - text_menu.get_width()) /2 ),(HEIGHT - text_menu.get_height())))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()


def draw_instructions():
    draw_yellow_instruction()
    if two_players:
        draw_red_instruction()

def draw_yellow_instruction():
    INSTRUCTIONS = INSTRUCTIONS_FONT.render("INSTRUCTIONS",1,RED)
    UP = INSTRUCTIONS_FONT.render("UP = W",1,WHITE)
    DOWN = INSTRUCTIONS_FONT.render("DOWN = S",1,WHITE)
    LEFT = INSTRUCTIONS_FONT.render("LEFT = D",1,WHITE)
    RIGTH = INSTRUCTIONS_FONT.render("RIGTH = A",1,WHITE)
    SHOOT = INSTRUCTIONS_FONT.render("SHOOT = RCTRL",1,WHITE)
    WIN.blit(INSTRUCTIONS, (10, WIN.get_height() - (INSTRUCTIONS.get_height()*6) -SPACE_BELLOW_INSTRUCTIONS ))
    WIN.blit(UP, (SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - (UP.get_height()*5) -SPACE_BELLOW_INSTRUCTIONS ))
    WIN.blit(DOWN, (SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - (DOWN.get_height()*4)-SPACE_BELLOW_INSTRUCTIONS ))
    WIN.blit(LEFT, (SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - (LEFT.get_height()*3)-SPACE_BELLOW_INSTRUCTIONS ))
    WIN.blit(RIGTH, (SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - (RIGTH.get_height()*2)-SPACE_BELLOW_INSTRUCTIONS ))
    WIN.blit(SHOOT, (SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - SHOOT.get_height()-SPACE_BELLOW_INSTRUCTIONS ))

def draw_red_instruction():
    INSTRUCTIONS = INSTRUCTIONS_FONT.render("INSTRUCTIONS",1,RED)
    UP = INSTRUCTIONS_FONT.render("UP = UP ARROW",1,WHITE)
    DOWN = INSTRUCTIONS_FONT.render("DOWN = DOW ARROW",1,WHITE)
    LEFT = INSTRUCTIONS_FONT.render("LEFT = LEFT ARROW",1,WHITE)
    RIGTH = INSTRUCTIONS_FONT.render("RIGTH = RIGTH ARROW",1,WHITE)
    SHOOT = INSTRUCTIONS_FONT.render("SHOOT = LCTRL",1,WHITE)
    WIN.blit(INSTRUCTIONS, (WIN.get_width() - INSTRUCTIONS.get_width() - SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - (INSTRUCTIONS.get_height()*6)-SPACE_BELLOW_INSTRUCTIONS))
    WIN.blit(UP, (WIN.get_width() - INSTRUCTIONS.get_width() - SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - (UP.get_height()*5)-SPACE_BELLOW_INSTRUCTIONS))
    WIN.blit(DOWN, (WIN.get_width() - DOWN.get_width() -SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - (DOWN.get_height()*4)-SPACE_BELLOW_INSTRUCTIONS))
    WIN.blit(LEFT, (WIN.get_width() - LEFT.get_width() - SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - (LEFT.get_height()*3)-SPACE_BELLOW_INSTRUCTIONS))
    WIN.blit(RIGTH, (WIN.get_width() - RIGTH.get_width() - SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - (RIGTH.get_height()*2)-SPACE_BELLOW_INSTRUCTIONS))
    WIN.blit(SHOOT, (WIN.get_width() - SHOOT.get_width() - SPACE_BORDER_INSTRUCTIONS, WIN.get_height() - SHOOT.get_height()-SPACE_BELLOW_INSTRUCTIONS))

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += VEL


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
    pygame.time.delay(3000)


def main():

    global max_bullets_red
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
    if two_players == False:
        max_bullets_red = 6
    else:
        max_bullets_red = MAX_BULLETS
    show_menu = False
    pygame.time.set_timer(SHOOT_MACHINE, TIME_SHOOTING)
    while run:
        clock.tick(FPS)
        if show_menu == True:
            action = menu()
            if(action == "CONTINUE"):
                show_menu = False
            elif(action == "RESET"):
                break
            elif(action == "QUIT"):
                pygame.quit()
            pygame.time.delay(50)
            continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL:
                    red_bullets = red_shoot(red_bullets,red)
                if event.key == pygame.K_SPACE:
                    show_menu = True
            
            if event.type == SHOOT_MACHINE and not two_players:
                red_shoot(red_bullets,red)
            
            if event.type == RED_HIT:
                red_health -= 1

            if event.type == YELLOW_HIT:
                yellow_health -= 1

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
                    red_health, yellow_health,show_menu)

    main()
    
def menu():
    global two_players
    MENU_MOUSE_POS = pygame.mouse.get_pos()
    MENU_BOX_X = WIDTH/2 - (BACKGROUND_MENU.get_width()/2)
    MENU_BOX_Y = HEIGHT/2 - (BACKGROUND_MENU.get_height()/2)
    WIN.blit(BACKGROUND_MENU, (MENU_BOX_X, MENU_BOX_Y))
    MENU_TEXT = MENU_TITLE.render("MAIN MENU", True, "#b68f40")
    MENU_RECT = MENU_TEXT.get_rect(center=(MENU_BOX_X + (BACKGROUND_MENU.get_width()/2) , MENU_BOX_Y + 40))
    WIN.blit(MENU_TEXT, MENU_RECT)
    txt_play_mode =  "Machine"
    if not two_players:
        txt_play_mode = "Two player"
    PLAY_BUTTON = Button(BACKGROUND_OPTION, pos=(MENU_BOX_X +(BACKGROUND_MENU.get_width()/2) , MENU_BOX_Y + 150), 
                        text_input="Continue", font = MENU_BUTTON, base_color="#d7fcd4", hovering_color="White")
    RESET_BUTTON = Button(BACKGROUND_OPTION, pos=(MENU_BOX_X +(BACKGROUND_MENU.get_width()/2), MENU_BOX_Y +210), 
                        text_input="Reset", font=MENU_BUTTON, base_color="#d7fcd4", hovering_color="White")
    TWO_PLAYERS = Button(BACKGROUND_OPTION, pos=(MENU_BOX_X +(BACKGROUND_MENU.get_width()/2), MENU_BOX_Y +270), 
                        text_input=txt_play_mode, font=MENU_BUTTON, base_color="#d7fcd4", hovering_color="White")
    QUIT_BUTTON = Button(BACKGROUND_OPTION, pos=(MENU_BOX_X +(BACKGROUND_MENU.get_width()/2), MENU_BOX_Y +330), 
                        text_input="Quit", font=MENU_BUTTON, base_color="#d7fcd4", hovering_color="White")
    
    for button in [PLAY_BUTTON, RESET_BUTTON,TWO_PLAYERS, QUIT_BUTTON]:
        button.update(WIN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                return "QUIT"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                return "CONTINUE"
            if RESET_BUTTON.checkForInput(MENU_MOUSE_POS):
                return "RESET"
            if TWO_PLAYERS.checkForInput(MENU_MOUSE_POS):
                two_players = not two_players
                return "RESET"
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    return "CONTINUE"
            

    pygame.display.update()


#For two players.
def red_handle_movement(keys_pressed, red):
    if two_players:
        player_movement(keys_pressed,red)
        return
    machine_vertical_movement(red)
    

def machine_vertical_movement(red):
    global machines_vertical_direction
    if machines_vertical_direction == "UP":
        red.y -= VEL_MACHINE
        if red.y - VEL_MACHINE <= 0:
            machines_vertical_direction = "DOWM"
            machine_horizontal_movement(red)
    else: 
        red.y += VEL_MACHINE
        if red.y + VEL_MACHINE + red.height > HEIGHT - 15:
            machines_vertical_direction = "UP"
            machine_horizontal_movement(red)

        
def  machine_horizontal_movement(red):
    global machines_horizontal_direction
    if machines_horizontal_direction == "LEFT":
        red.x -= VEL_MACHINE
        if red.x - VEL_MACHINE < BORDER.x + BORDER.width:
            machines_horizontal_direction = "RIGTH"
    else:
        red.x += VEL_MACHINE
        if red.x + VEL + red.width > WIDTH:
            machines_horizontal_direction = "LEFT"

def red_shoot(red_bullets, red):
    global max_bullets_red
    if len(red_bullets) < max_bullets_red:
        bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
        red_bullets.append(bullet)
    return red_bullets

#for two players
def player_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL

if __name__ == "__main__":
    main()