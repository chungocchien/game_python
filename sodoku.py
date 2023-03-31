import pygame

pygame.init()

# Set the dimensions of the game window
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the game window
pygame.display.set_caption("Sudoku")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
LIGHT_BLUE = (102, 255, 255)

def draw_board(board):
    # Draw the background of the board
    screen.fill(WHITE)
    # Draw the grid lines
    for i in range(10):
        thickness = 1
        if i % 3 == 0:
            thickness = 3
        pygame.draw.line(screen, GRAY, (50 + 50 * i, 50), (50 + 50 * i, 500), thickness)
        pygame.draw.line(screen, GRAY, (50, 50 + 50 * i), (500, 50 + 50 * i), thickness)

    # Draw the numbers on the board
    font = pygame.font.SysFont('Calibri', 40, True, False)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                num = font.render(str(board[i][j]), True, BLACK)
                x = j * 50 + 70
                y = i * 50 + 55
                screen.blit(num, (x, y))

def is_valid_move(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check square
    square_row = (row // 3) * 3
    square_col = (col // 3) * 3
    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if board[i][j] == num:
                return False

    # If none of the above conditions are met, the move is valid
    return True

def handle_input(board, highlighted_cell):
    # Get the position of the mouse cursor
    mouse_pos = pygame.mouse.get_pos()

    # Check if the user clicked on a cell
    if 50 <= mouse_pos[0] <= 500 and 50 <= mouse_pos[1] <= 500:
        row = (mouse_pos[1] - 50) // 50
        col = (mouse_pos[0] - 50) // 50
        highlighted_cell = (row, col)

    # Check if the user pressed a number key
    keys = pygame.key.get_pressed()
    for i in range(1, 10):
        if keys[pygame.K_KP1 + i - 1] or keys[pygame.K_1 + i - 1]:
            if highlighted_cell is not None:
                row, col = highlighted_cell
                if is_valid_move(board, row, col, i):
                    board[row][col] = i

    return highlighted_cell

def run_game():
    # Initialize the game board
    board = [
        [0, 0, 0, 0, 0, 0, 0, 8, 3],
        [0, 3, 5, 4, 8, 2, 1, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 3, 2, 7, 6, 0, 0, 4],
        [8, 7, 2, 0, 0, 5, 0, 0, 0],
        [6, 0, 4, 0, 3, 0, 2, 5, 0],
        [9, 0, 0, 0, 1, 4, 0, 7, 0],
        [0, 0, 8, 0, 0, 7, 0, 2, 9],
        [3, 0, 0, 0, 2, 9, 5, 6, 1],
    ]

    # Initialize the highlighted cell
    highlighted_cell = None

    # Set the clock for the game loop
    clock = pygame.time.Clock()

    # Start the game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the game if the user closes the window
                pygame.quit()
                quit()

        # Handle user input
        highlighted_cell = handle_input(board, highlighted_cell)

        # Draw the board
        draw_board(board)

        # Highlight the selected cell
        if highlighted_cell is not None:
            row, col = highlighted_cell
            pygame.draw.rect(screen, LIGHT_BLUE, (50 + col * 50, 50 + row * 50, 50, 50), 3)

        # Update the screen
        pygame.display.update()

        # Set the frame rate
        clock.tick(60)

run_game()