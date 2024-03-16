import time

tank_x = 0
tank_y = 0

def move_tank(direction):
    global tank_x, tank_y
    if direction == 'w':
        tank_y -= 1
    elif direction == 'a':
        tank_x -= 1
    elif direction == 's':
        tank_y += 1
    elif direction == 'd':
        tank_x += 1

def print_tank_position():
    print(f"Tank position: ({tank_x}, {tank_y})")

# Главный игровой цикл
while True:
