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
