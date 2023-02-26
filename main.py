import pygame
from time import sleep

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("TIC TAC TOE")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

score = 0

board = [['', '', ''], ['', '', ''], ['', '', '']]

my_font = pygame.font.SysFont('Comic Sans MS', 30)

current_player = 'O'

font = pygame.font.Font(None, max(WINDOW_WIDTH, WINDOW_HEIGHT) // 5)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            row = mouse_position[1] // (WINDOW_HEIGHT // 3)
            col = mouse_position[0] // (WINDOW_HEIGHT // 3)
            if board[row][col] == '':
                board[row][col] = current_player
                score += 1
                if current_player == 'O':
                    current_player = 'X'
                else:
                    current_player = 'O'

    window.fill(WHITE)

    pygame.draw.line(window, (0, 0, 0), [WINDOW_WIDTH // 3, 0], [WINDOW_WIDTH // 3, WINDOW_HEIGHT], 5)
    pygame.draw.line(window, (0, 0, 0), [(WINDOW_WIDTH // 3) * 2, 0], [(WINDOW_WIDTH // 3) * 2, WINDOW_HEIGHT], 5)
    pygame.draw.line(window, (0, 0, 0), [0, WINDOW_HEIGHT // 3], [WINDOW_WIDTH, WINDOW_HEIGHT // 3], 5)
    pygame.draw.line(window, (0, 0, 0), [0, 2 * (WINDOW_HEIGHT // 3)], [WINDOW_WIDTH, 2 * (WINDOW_HEIGHT // 3)], 5)


    text_surface = my_font.render(f'Кто ходит:  {current_player}', False, (0, 0, 0))
    window.blit(text_surface, (0, 0))

    for i in range(3):
        for j in range(3):
            text = font.render(board[i][j], True, BLACK)
            text_width = WINDOW_WIDTH // 3
            text_height = WINDOW_HEIGHT // 3
            text_x = j * text_width
            text_y = i * text_height
            window.blit(text, (text_x + WINDOW_HEIGHT // 8, text_y + WINDOW_WIDTH // 8))

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '':
            text_surface = font.render(f'WINS  {board[i][0]}!', False, (255, 111, 255))
            window.blit(text_surface, (WINDOW_WIDTH // 2 - WINDOW_WIDTH // 5, WINDOW_HEIGHT // 2 - WINDOW_WIDTH // 20))
            game_over = True
        if board[0][i] == board[1][i] == board[2][i] != '':
            text_surface = font.render(f'WINS  {board[0][i]}!', False, (255, 111, 255))
            window.blit(text_surface, (WINDOW_WIDTH // 2 - WINDOW_WIDTH // 5, WINDOW_HEIGHT // 2 - WINDOW_WIDTH // 20))
            game_over = True

    if board[0][0] == board[1][1] == board[2][2] != '':
        text_surface = font.render(f'WINS  {board[0][0]}!', False, (255, 111, 255))
        window.blit(text_surface, (WINDOW_WIDTH // 2 - WINDOW_WIDTH // 5, WINDOW_HEIGHT // 2 - WINDOW_WIDTH // 20))
        game_over = True
    if board[0][2] == board[1][1] == board[2][0] != '':
        text_surface = font.render(f'WINS  {board[0][2]}!', False, (255, 111, 255))
        window.blit(text_surface, (WINDOW_WIDTH // 2 - WINDOW_WIDTH // 5, WINDOW_HEIGHT // 2 - WINDOW_WIDTH // 20))
        game_over = True
    if score == 9 and game_over != True:
        text_surface = font.render(f'DRAW!', False, (255, 111, 255))
        window.blit(text_surface, (WINDOW_WIDTH // 2 - WINDOW_WIDTH // 5, WINDOW_HEIGHT // 2 - WINDOW_WIDTH // 20))
        game_over = True
    pygame.display.update()
    if game_over == True:
        sleep(2)