import pygame
import random

# Инициализация Pygame
pygame.init()

# Определение цветов (можно настроить под свои предпочтения)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Установка размеров окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра про танки")

# Генерация случайного уровня
def generate_level():
    level = []
    for _ in range(10):  # Для примера, 10 строк
        row = [random.choice([0, 1]) for _ in range(15)]  # Для примера, 15 клеток в строке
        level.append(row)
    return level

# Отрисовка уровня
def draw_level(level):
    for y, row in enumerate(level):
        for x, tile in enumerate(row):
            if tile == 1:
                pygame.draw.rect(screen, WHITE, (x*40, y*40, 40, 40))  # Пример размера тайла - 40x40

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  # Очистка экрана
    level = generate_level()  # Генерация нового уровня
    draw_level(level)  # Отрисовка уровня
    pygame.display.flip()  # Обновление экрана

# Завершение работы Pygame
pygame.quit()
