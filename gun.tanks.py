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
