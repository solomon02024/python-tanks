import random

# Создание случайной карты размером width x height
def generate_random_level(width, height):
    level = []
    for _ in range(height):
        row = [random.choice(["препятствие", "пусто"]) for _ in range(width)]
        level.append(row)
    return level

# Пример использования
random_width = 10
random_height = 10
random_level = generate_random_level(random_width, random_height)
print(random_level)
