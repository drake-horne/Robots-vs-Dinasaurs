from weapon import Weapon

class Robot:
    def __init__(self, robot_name,):
        self.robot_name = robot_name 
        self.active_weapon = Weapon('particle beam', 25)
        self.d_health = 100
    def attack_robo(self, dinosaur):
        dinosaur.health = dinosaur.health - self.active_weapon.attack_power 
        print(f'{self.robot_name} attacked {dinosaur.dino_name} with {self.active_weapon.weapon_name} for {self.active_weapon.attack_power} his health is now {dinosaur.health}')
