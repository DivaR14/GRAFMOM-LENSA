import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran kanvas
canvas_width = 800
canvas_height = 600

# Warna
white = (255, 255, 255)

# Membuat kanvas
canvas = pygame.display.set_mode((canvas_width, canvas_height))
pygame.display.set_caption("Menggambar Garis")

# Fungsi untuk menggambar garis horizontal dan vertikal
def draw_lines():
    # Menggambar garis horizontal di tengah
    pygame.draw.line(canvas, white, (0, canvas_height // 2), (canvas_width, canvas_height // 2), 3)
    # Menggambar garis vertikal di tengah
    pygame.draw.line(canvas, white, (canvas_width // 2, 0), (canvas_width // 2, canvas_height), 3)

# Main loop
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Menggambar garis di kanvas
        canvas.fill((0, 0, 0))  # Menghapus layar
        draw_lines()  # Menggambar garis
        pygame.display.flip()  # Memperbarui layar

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
