class Tank:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health
        self.ammo = 0

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
            print(f"{self.name} выстрелил! Урон {self.damage}")
        else:
            print("Нет боеприпасов!")

    def reload(self, ammo_count):
        self.ammo += ammo_count
        print(f"{self.name} перезарядился! Боеприпасов: {self.ammo}")

class Shop:
    def __init__(self):
        self.ammo_stock = 100

    def buy_ammo(self, tank, ammo_count):
        if self.ammo_stock >= ammo_count:
            tank.reload(ammo_count)
            self.ammo_stock -= ammo_count
            print(f"Покупка совершена! Остаток боеприпасов в магазине: {self.ammo_stock}")
        else:
            print("Недостаточно боеприпасов в магазине!")

# Создаем танк и магазин
tank1 = Tank("Танк 1", 50, 100)
shop = Shop()

# Перезаряжаем танк
shop.buy_ammo(tank1, 50)

# Совершаем выстрел
tank1.shoot()
import turtle

# Настройка окна
turtle.setup(800, 600)
turtle.speed(0)
turtle.bgcolor('white')

# Тело танка
turtle.color('green')
turtle.begin_fill()
turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()

# Башня танка
turtle.penup()
turtle.goto(100, 50)
turtle.pendown()
turtle.color('brown')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# Опция для сохранения рисунка
ts = turtle.getscreen()
ts.getcanvas().postscript(file="tank.eps")

turtle.done()
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
class Tankpiry:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Недостаточно средств")

    def check_balance(self):
        print("Баланс танкпиров: ", self.balance)


# Пример использования

tankpiry_account = Tankpiry(100)  # Создание счета с начальным балансом 100 танкпиров
tankpiry_account.check_balance()  # Проверяем баланс
tankpiry_account.deposit(50)  # Вносим 50 танкпиров
tankpiry_account.check_balance()  # Проверяем обновленный баланс
tankpiry_account.withdraw(30)  # Снимаем 30 танкпиров
tankpiry_account.check_balance()  # Проверяем оставшийся баланс
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
class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shoot(self, target_x, target_y):
        bullet = Bullet(self.x, self.y, target_x, target_y)
        bullet.fire()

class Bullet:
    def __init__(self, x, y, target_x, target_y):
        self.x = x
        self.y = y
        self.target_x = target_x
        self.target_y = target_y

    def fire(self):
        # Логика анимации перемещения пули от текущей позиции (x, y) к цели (target_x, target_y)
        pass

# Создание объекта танка
tank = Tank(x=100, y=100)

# Вызов метода стрельбы танка
tank.shoot(target_x=200, target_y=200)
tankpirov = 1000000
print("У вас", tankpirov, "танкпиров")
import random

def april_fools_update():
    features = ["Новый игровой режим: Танцующие таонки!",
                "Добавлены эксклюзивные костюмы на первом ящике",
                "Таонки теперь могут говорить!"]
    
    print("Поздравляем с первоапрельским обновлением игры про таонки!")
    print("Что нового:")
    
    for feature in features:
        print("- " + feature)
    
    print("Приятной игры!")

april_fools_update()
