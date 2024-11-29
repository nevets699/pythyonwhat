
import pygame
print("Versión de pygame:", pygame.__version__)

import sys

# Inicializar `pygame`
pygame.init()

# Establecer el tamaño de la ventana
size = (800, 600)
screen = pygame.display.set_mode(size)

# Establecer el título de la ventana
pygame.display.set_caption("Mi primer juego con pygame")

# Colores
WHITE = (255, 255, 255)

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Llenar la pantalla con color blanco
    screen.fill(WHITE)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de `pygame`
pygame.quit()
sys.exit()