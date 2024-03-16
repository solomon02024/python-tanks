class Tank:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self):
        # Add movement logic here
        
    def shoot(self):
        # Add shooting logic here

class AI:
    def __init__(self):
        self.tanks = []
    
    def spawn_tanks(self, level):
        for _ in range(2 + level):  # Spawn 2-3 tanks based on level
            new_tank = Tank(random.randint(0, 10), random.randint(0, 10))
            self.tanks.append(new_tank)
    
    def control_tanks(self):
        for tank in self.tanks:
            tank.move()
            tank.shoot()

# Main script
import random

ai_controller = AI()
level = 1  # Change the level as the player progresses

ai_controller.spawn_tanks(level)
ai_controller.control_tanks()
