import pygame
from constants import (
    WIN, BLACK, BORDER, WHITE, RED, YELLOW,
    BULLET_VEL, BORDER, HEALTH_FONT, WINNER_FONT,
    YELLOW_SPACESHIP, RED_SPACESHIP, SPACE,
    RED_HIT, YELLOW_HIT, WIDTH, HEIGHT
)

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update()

def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - 5 > 0:  # LEFT
        yellow.x -= 5
    if keys_pressed[pygame.K_d] and yellow.x + 5 + yellow.width < BORDER.x:  # RIGHT
        yellow.x += 5
    if keys_pressed[pygame.K_w] and yellow.y - 5 > 0:  # UP
        yellow.y -= 5
    if keys_pressed[pygame.K_s] and yellow.y + 5 + yellow.height < HEIGHT - 15:  # DOWN
        yellow.y += 5

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - 5 > BORDER.x + BORDER.width:  # LEFT
        red.x -= 5
    if keys_pressed[pygame.K_RIGHT] and red.x + 5 + red.width < WIDTH:  # RIGHT
        red.x += 5
    if keys_pressed[pygame.K_UP] and red.y - 5 > 0:  # UP
        red.y -= 5
    if keys_pressed[pygame.K_DOWN] and red.y + 5 + red.height < HEIGHT - 15:  # DOWN
        red.y += 5

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
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)