from robot import Robot
class Dinosaur:
    def __init__(self, dino_name, attack_power):
        self.dino_name = dino_name
        self.attack_power = attack_power
        self.health = 100


    def attack(self, robot):
        robot.d_health = robot.d_health - self.attack_power
        print(f'{self.dino_name} attacked {robot.robot_name} for {self.attack_power}, his health is now {robot.d_health}')

    

