import pygame as p
from MiniChess import ChessEngine

p.init()

HEIGHT = 384
WIDTH = 320
DIMENSION_VERTICAL = 6
DIMENSION_HORIZONTAL = 5
SQ_SIZE = 64
MAX_FPS = 15
IMAGES = {}

def load_images():
    pieces = ["bR", "bN", "bB", "bQ", "bK", "bp", "wR", "wN", "wB", "wQ", "wK", "wp"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"../images/{piece}.png"), (SQ_SIZE, SQ_SIZE))

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    load_images()
    print(gs.board)
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        print("working")
        draw_game_state(screen, gs)
        print("working2")
        clock.tick(MAX_FPS)
        p.display.flip()

def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)

def draw_board(screen):
    colors = [p.Color('white'), p.Color('grey')]
    for r in range(DIMENSION_VERTICAL):
        for c in range(DIMENSION_HORIZONTAL):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, board):
    for r in range(DIMENSION_VERTICAL):
        for c in range(DIMENSION_HORIZONTAL):
            piece = board[r][c]
            if piece != "--":  # Ignore empty squares
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

if __name__ == "__main__":
    main()
