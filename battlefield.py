


from robot import Robot
from dinasaur import Dinosaur
class Battlefield:
    
    def __init__(self):
        self.robot = Robot('roboman')
        self.dinosaur = Dinosaur('Dino', 30)
    
    def display_welcome(self):
        print('Welcome to the game of robot vs dinosaur!')
        
    def battlephase(self):
        while ((self.robot.d_health) and (self.dinosaur.health)) > 0:
            if (self.robot.d_health) > 0: 
                self.robot.attack_robo(self.dinosaur)
            if self.dinosaur.health > 0:
                self.dinosaur.attack(self.robot)
        if self.dinosaur.health <= 0:
            print(self.robot.robot_name + ' is the winner')
                
        if self.robot.d_health <= 0:
            print(self.dinosaur.dino_name + ' is the winner.') 
            

    
    def run_battle(self):
        self.display_welcome()
        self.battlephase()  
        
                





            

