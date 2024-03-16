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
