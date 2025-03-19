import pygame  # Impordib PyGame mooduli


def draw_grid(screen, square_size, rows, cols, line_color):
    """Funktsioon, mis joonistab ekraanile ruudustiku."""
    for row in range(rows):  # Läbib kõik read
        for col in range(cols):  # Läbib kõik veerud
            rect = pygame.Rect(col * square_size, row * square_size, square_size,
                               square_size)  # Loob ruudu koordinaadid
            pygame.draw.rect(screen, line_color, rect, 1)  # Joonistab ruudu, mille piir on määratud värviga


# Initsialiseerib PyGame
pygame.init()

# Määrab ekraani suuruse
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Harjutamine")  # Seab akna pealkirja

# Seadistused ruudustiku jaoks
SQUARE_SIZE = 20  # Ruudu suurus pikslites
ROWS = SCREEN_HEIGHT // SQUARE_SIZE  # Ridade arv
COLS = SCREEN_WIDTH // SQUARE_SIZE  # Veergude arv
LINE_COLOR = (255, 0, 0)  # Ruudu piiride värv (punane)
BG_COLOR = (144, 238, 144)  # Taustavärv (hele roheline)

# Peamine mängutsükkel
running = True
while running:
    screen.fill(BG_COLOR)  # Täidab ekraani taustavärviga
    draw_grid(screen, SQUARE_SIZE, ROWS, COLS, LINE_COLOR)  # Joonistab ruudustiku

    for event in pygame.event.get():  # Kontrollib kõiki sündmusi
        if event.type == pygame.QUIT:  # Kui vajutatakse sulgemisnuppu
            running = False  # Lõpetab tsükli

    pygame.display.flip()  # Uuendab ekraani

pygame.quit()  # Sulgeb PyGame'i

