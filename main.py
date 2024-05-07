import pygame
import constants as c
import random
import math

pygame.init()

#CONSTANT VALUES
FPS = 60 #frames per second (how quickly the game is running)
WINDOW_WIDTH, WINDOW_HEIGHT = 550, 700
GRID_SIZE = 450
HEADING_HEIGHT = 150
ROWS, COLS = 4, 4
OFFSET = 50
PADDING = 10

RECT_WIDTH = GRID_SIZE // ROWS
RECT_HEIGHT = GRID_SIZE // COLS

#COLORS
OUTLINE_COLOR = (187, 173, 160)
OUTLINE_THICKNESS = 10
#BACKGROUND_COLOR = (205, 192, 180)
BACKGROUND_COLOR = (250, 248, 239)
GRID_CONTAINER_COLOR = (187, 173, 160)
FONT_COLOR = (119, 110, 101)

LARGE_FONT = pygame.font.SysFont("arial", 80, bold=True)
MEDIUM_FONT = pygame.font.SysFont("arial", 18, bold=True)
SMALL_FONT = pygame.font.SysFont("arial", 14, bold=True)

MOVE_VEL = 20 #tiles will move at 20 pixels per second

#SETUP pygame WINDOW
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("2048")


def draw_grid(window):
    pass

    
    #for row in range(1, ROWS):
    #    y = row * RECT_HEIGHT
    #    pygame.draw.line(window, OUTLINE_COLOR, (0, y), (WIDTH, y), OUTLINE_THICKNESS)
    
    #for col in range(1, COLS):
    #    x = col * RECT_WIDTH
    #    pygame.draw.line(window, OUTLINE_COLOR, (x, 50), (x, HEIGHT+OFFSET), OUTLINE_THICKNESS)

    #pygame.draw.rect(window, OUTLINE_COLOR, (0, 50, WIDTH, HEIGHT), OUTLINE_THICKNESS)

def draw_window_heading(window):
    heading = pygame.draw.rect(window, (BACKGROUND_COLOR), (0, 0, WINDOW_WIDTH, HEADING_HEIGHT))

    #game name
    game_name = LARGE_FONT.render("2048", 1, FONT_COLOR)
    window.blit(game_name, (OFFSET + PADDING, PADDING))

    #score window
    score_window = pygame.draw.rect(window, GRID_CONTAINER_COLOR, (heading.centerx, PADDING, 100, 70), 0, 3)
    score_label = SMALL_FONT.render("SCORE", 1, (238, 228, 218))
    score = MEDIUM_FONT.render("0", 1, (238, 228, 218))
    window.blit(score_label, ((score_window.centerx - score_label.get_width() // 2), (score_window.centery - (score_label.get_height() // 2) - 20)))
    window.blit(score, (score_window.centerx, score_window.centery))

    #best score window
    best_score_window = pygame.draw.rect(window, GRID_CONTAINER_COLOR, (score_window.right + PADDING, PADDING, 100, 70), 0, 3)
    best_score_label = SMALL_FONT.render("BEST", 1, (238, 228, 218))
    best_score = MEDIUM_FONT.render("0", 1, (238, 228, 218))
    window.blit(best_score_label, ((best_score_window.centerx - best_score_label.get_width() // 2), (best_score_window.centery - (best_score_label.get_height() // 2) - 20)))
    window.blit(best_score, (best_score_window.centerx, best_score_window.centery))
    #AI button
    ai_button = pygame.draw.rect(window, GRID_CONTAINER_COLOR, (heading.centerx, (score_window.bottom + PADDING), 100, 40), 0, 3)
    ai_button_label = MEDIUM_FONT.render("AI", 1, (238, 228, 218))
    window.blit(ai_button_label, (ai_button.centerx - ai_button_label.get_width() // 2, ai_button.centery - ai_button_label.get_height() // 2))

    #reset button
    reset_button = pygame.draw.rect(window, GRID_CONTAINER_COLOR, (ai_button.right + PADDING, (best_score_window.bottom + PADDING), 100, 40), 0, 3)
    reset_button_label = MEDIUM_FONT.render("Reset", 1, (238, 228, 218))
    window.blit(reset_button_label, (reset_button.centerx - reset_button_label.get_width() // 2, reset_button.centery - reset_button_label.get_height() // 2))

def draw_window_body(window):
    pygame.draw.rect(window, (143, 122, 102), (OFFSET, HEADING_HEIGHT + OFFSET, GRID_SIZE, GRID_SIZE), 0, 10)

def draw(window):
    window.fill(BACKGROUND_COLOR)
    draw_window_heading(window)
    draw_window_body(window)
    draw_grid(window)
    pygame.display.update()
    

#Event loop
def main(window):
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window)
    pygame.quit()        

#Only going to execute this function if we're running this file directly
if __name__ == "__main__":
    main(WINDOW)
