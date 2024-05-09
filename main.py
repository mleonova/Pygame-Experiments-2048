import pygame
import constants as c

class GameGrid:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("2048")
        self.window = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))

        # Fonts
        self.large_font = pygame.font.SysFont("arial", 60, bold=True)
        self.medium_font = pygame.font.SysFont("arial", 18, bold=True)
        self.small_font = pygame.font.SysFont("arial", 14, bold=True)

    def draw_window(self):
        # Print game name
        game_name = self.large_font.render("~ 2048 ~", 1, c.MAIN_FONT_COLOR)
        name_container = game_name.get_rect(center=(c.WINDOW_WIDTH/2, c.OFFSET))
        self.window.blit(game_name, name_container)

        # Print score
        score_container = pygame.draw.rect(self.window, c.GRID_CONTAINER_COLOR, (c.OFFSET, name_container.bottom + c.PADDING, c.BUTTON_WIDTH, c.BUTTON_HEIGHT), 0, 3)
        score_label = self.small_font.render("SCORE", 1, c.FONT_COLOR)
        score = self.medium_font.render("0", 1, c.FONT_COLOR)
        self.window.blit(score_label, (score_container.centerx - score_label.get_width()/2, score_container.top + c.PADDING))
        self.window.blit(score, (score_container.centerx - score.get_width()/2, score_container.centery))

        # Print best score
        best_score_container = pygame.draw.rect(self.window, c.GRID_CONTAINER_COLOR, (score_container.right + c.PADDING*2, name_container.bottom + c.PADDING, c.BUTTON_WIDTH, c.BUTTON_HEIGHT), 0, 3)
        best_score_label = self.small_font.render("BEST", 1, c.FONT_COLOR)
        best_score = self.medium_font.render("0", 1, c.FONT_COLOR)
        self.window.blit(best_score_label, (best_score_container.centerx - best_score_label.get_width()/2, best_score_container.top + c.PADDING))
        self.window.blit(best_score, (best_score_container.centerx - best_score.get_width()/2, best_score_container.centery))

        # Print AI button
        ai_button = pygame.draw.rect(self.window, c.BUTTON_COLOR, (c.OFFSET, score_container.bottom + c.PADDING, c.BUTTON_WIDTH, c.BUTTON_HEIGHT), 0, 3)
        ai_button_label = self.medium_font.render("AI", 1, c.FONT_COLOR)
        self.window.blit(ai_button_label, (ai_button.centerx - ai_button_label.get_width()/2, ai_button.centery - ai_button_label.get_height()/2))

        # Print New Game button
        reset_button = pygame.draw.rect(self.window, c.BUTTON_COLOR, (ai_button.right + c.PADDING*2, best_score_container.bottom + c.PADDING, c.BUTTON_WIDTH, c.BUTTON_HEIGHT), 0, 3)
        reset_button_label = self.medium_font.render("New Game", 1, c.FONT_COLOR)
        self.window.blit(reset_button_label, (reset_button.centerx - reset_button_label.get_width()/2, reset_button.centery - reset_button_label.get_height()/2))

        # Draw grid
        grid = pygame.draw.rect(self.window, c.GRID_CONTAINER_COLOR, (c.OFFSET, ai_button.bottom + c.PADDING, c.GRID_SIZE, c.GRID_SIZE), 0, 10)    
        for row in range(0, c.ROWS):
            for col in range(0, c.COLS):
                pygame.draw.rect(self.window, c.EMPTY_TILE_COLOR, 
                                 (grid.topleft[0] + col * c.CELL_SIZE + c.PADDING + c.PADDING * col, grid.topleft[1] + row * c.CELL_SIZE + c.PADDING + c.PADDING * row, c.CELL_SIZE, c.CELL_SIZE), 0, 7)
        
    def draw(self):
        self.window.fill(c.BACKGROUND_COLOR)
        self.draw_window()
        pygame.display.update()    

def main():
    game_grid = GameGrid()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        game_grid.draw()

    pygame.quit()

if __name__ == "__main__":
    main()
