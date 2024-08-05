import sys #It is used in order to exit the game
import random
import time
import logging
class Player:  #Define player features
    def __init__(self, name): #player health
        self.name = name
        self.max_health = 200
        self.health = 100
        self.attack = 10
        self.coin=0
        self.location = 'Center Room'
        self.level = 1

class Monster: #Define monster feature
    def __init__(self, name, health):     #Monster name and monster health
        self.name = name
        self.max_health = health
        self.attack = random.randint(5, 9)
        self.monstercoin=5
        self.levelgain = 1

class Room:  #Define Room features
    def __init__(self,name,description):     #It defines room name and its description
        self.name=name
        self.description=description
        self.monsters=[]
        self.directions=[]






class Direction: #Define Direction features
    def __init__(self,name): #it defines direction name
        self.name=name

class Game:  #Define Game features  and provide a platform user can play by using related functions. It is the most signifant class in terms of sustainability of the game
    def __init__(self):
        logging.basicConfig(filename='game.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
        logging.basicConfig(level=logging.DEBUG)

        self.monsters = []
        self.room = {}  # Initialize as a dictionary
        self.fillroom={}
        self.ourdirections = []
        self.health_adder=[]
        self.market_items_sword = {"Black Sword": 5, "Cursed Sword": 10, "Giant Sword": 15, "Giant Axe": 20}
        self.market_items_armor={"Black Armor":5,"Cursed Armor":10,"Giant Armor I":15,"Giant Armor II":20}
        self.market_items_armor_health={"Black Armor":10,"Cursed Armor":20,"Giant Armor I":30,"Giant Armor II":40}
        self.initialize_game() #IT should always be in bottom







    def initialize_game(self):   #This class is used in order to install rooms, directions, monster names. It is a basically installation package class

        player_name = input("Enter player name: ")

        #-----------------------------------------------------------------------

        # Define room names and descriptions
        room_names = ["South Room", "East Room", "West Room","North Room", "North East Room", "North West Room","South East Room", "South West Room"]
        room_descriptions = ["It is a South Room", "It is a East Room","It is a West Room", "It is a North Room", "It is a North East Room","It is a North West Room", "It is a South East Room", "It is a South West Room"]
        #It matches room name and description on self.room constructor
        for index in range(len(room_names)):
            room = Room(room_names[index], room_descriptions[index])
            self.room[room_names[index]] = room



        #---------------------------------------------------------------------------------------------------------------
        #we create object and collect them in direction list in order to process this data
        possibledirections=["South","East","West","North","North East","North West","South East","South West"]
        for mydirection in possibledirections:

            distance_instance = Direction(mydirection)
            self.ourdirections.append(distance_instance)
        #----------------------------------------------------------------------------------------------------------------
        self.player = Player(player_name)   #IT is used to create player
        #----------------------------------------------------------------------------------------------------------------
        #we used this monster names in order to create monster objects then collected them on the list
        monster_names = ["Witcher", "Dragon", "Zombie", "Headhunter", "Evil", "Orc","Goblin","BigBoss"]
        for name in monster_names:
            monster_health = random.randint(50, 80)
            monster_instance = Monster(name,monster_health)
            self.monsters.append(monster_instance)
        #----------------------------------------------------------------------------------------------------------------
        #It is so vital part of the game since this part is basically used so as to fill rooms with monsters
        for index, room_name in enumerate(self.room):
            monsterfillingroom = [monster.name for monster in self.monsters]
            directionfillingroom = [direction.name for direction in self.ourdirections]
            self.fillroom[room_name] = (self.room[room_name].description, directionfillingroom[index], monsterfillingroom[index])
        #------------------------------------------------------------------------------------------------------------------
    def start(self):  #It release prompt containing player name
        print("Welcome, {}. Are you ready for adventure?".format(self.player.name))
        time.sleep(2)
        print("As a brave warrior, you embarked on a legendary quest to stop a coming darkness from devastating the kingdom of Valoria. ")
        print("countless legends of a powerful artifact that exists within the darkest dungeons and can bring peace and calm back to the land. But hazardous obstacles and evil creatures defend the dungeons.")
        print("Your journey as this land's hero begins here, in the heart of Valoria's citadel. You headed into unexplored territory with only your courage and a reliable sword")
        time.sleep(1.5)
        self.play()

    def play(self):  #It is a basically provie basement to user after boss fight after going market etc. every action might end up with this function.
         #When program asks if you wanna return, this function runs when user accept the condition

        # this part shows player informations and what he can do so on like exit game, move or going market
        print("Player Name: " + self.player.name)
        print("Attack {}".format(self.player.attack))
        print("Max health {}".format(self.player.max_health))
        print("Health {}".format(self.player.health))
        print("Level {}".format(self.player.level))
        print("Coin {}".format(self.player.coin))
        time.sleep(2)
        print("You take the role of a brave hero, choosing to use your name as an ambassador of hope for the Valorian people.")
        time.sleep(2)
        print("Enter 1 in order to move or Enter 2 for exit Enter 3 for going market")
        option = input("->")
        logging.info('Player {} started playing.'.format(self.player.name))

        if option == "1":
            print("The kingdom is split up into various zones, each of which faces unique difficulties and monsters. Along the route, you'll come across a variety of enemies and monsters as you go through the South, East, West, North, North East, North West, South East, and South West regions.")
            time.sleep(2)
            print("directions are in here South,East,West,North,North East,North West,South East,South West")
            time.sleep(1)
            print("Enter value to pick your direction. the direction you enter should be exactly the same shown above")
            #option=input("-> ")


            valid_input = False
            while not valid_input:
                option = input("-> ")

                for i in range(len(self.ourdirections)):
                    if option == self.ourdirections[i].name:
                        x=option+" Room"
                        #There is exception here if user choose South West Room he cannot go inside because there is a boss fight in here
                        #code force you to return to basement so that you can pick your direction again
                        if x == "South West Room" and self.player.level < 8:
                             print("You cannot enter this room yet. Your level is not high enough.")
                             returnbutton=input("Enter R return safe safe zone: ")
                             if returnbutton=="R" or returnbutton=="r":
                                 self.play()

                             valid_input = True  # Exit the loop
                             break

                        #It brings specific monster prepare fight environment so before every room is installed with specific room fillroom is used for that
                        mymonsters=self.fillroom[x][2]
                        for i in range(len(self.monsters)):

                            if mymonsters == self.monsters[i].name:
                                self.fight(self.monsters[i])

                        valid_input = True
                        break
                #When user enter invalid direction brings this part the main reason
                if not valid_input:
                    print("Invalid value. Please enter a valid direction value.")

        elif option == "2":  #When user pick you will be able to exit the game
            time.sleep(2)
            print("Thank you for playing Protector of Valoria")
            logging.info('Player {} exited the game.'.format(self.player.name))
            sys.exit()
        elif option=="3":     #It is used in order to go market
            logging.info('Player {} visited the market.'.format(self.player.name))
            self.visit_market()
        else:   #Algorithm will ask again you need to enter valid option
            print("Invalid choice. Please enter available option")
            self.play()

    def fight(self, monster):   #This function is used to adjust monster fights by using some conditions
          logging.debug('Player {} initiated a fight with {}.'.format(self.player.name, monster.name))


          if monster.max_health>0: #Code gonna check monster health first it is important in order to decide room's state
            print("Fight Started!")
            while self.player.health > 0 and monster.max_health > 0:  #If both healths are higher than 0, fight gonna start
                print("Enter X for attack or Pass attack button is P to {}".format(monster.name))
                attack_button = input("-> ")
                if attack_button == "X" or attack_button == "x": #It is attack mechanism or button in order to attack monster
                    monster.max_health -= self.player.attack
                    if monster.max_health <= 0:      #When monster health is less than 0
                        logging.info('Player {} defeated {}!'.format(self.player.name, monster.name))

                        print("Congrats! you beat {} and one step close to bring the peace to Valoria! ".format(monster.name))
                        self.player.level=self.player.level+monster.levelgain  #User gets level its important to be prepared for boss fight




                        if monster.name == "BigBoss":   #It is a special prompt for final boss

                            print("Congrats, you killed the boss and brought peace to the Valoria again!")
                            print("Press 'E' to exit the game or 'R' to return to the safe zone.")
                            exit_or_return = input("-> ").lower()  #It makes ur input automatically lower so it offer option to user to stay in the game or return
                            valid_input=False

                            while not valid_input:
                                if exit_or_return == "e":
                                    print("Thank you for playing Protector of Valoria")
                                    logging.info('Player {} exited the market.'.format(self.player.name))
                                    sys.exit()
                                elif exit_or_return == "r":
                                    self.play()
                                    valid_input=True
                                    break
                                else:
                                    print("Invalid option. Please enter 'E' to exit or 'R' to return to the safe zone.")

                        print("You are leveled up and your new level is {}".format(self.player.level))
                        #---------------------------LOOT SYSTEM-----------------------------------------------------------#
                        #This code is provide pot mechanism after monster fight so that hero can refull its health
                        print("If you wanna get potion please press F or you can pass it by pressing any button")
                        potbutton=input("->")
                        if potbutton=="f" or potbutton=="F":
                            logging.info('Player {} got potion!'.format(self.player.name))
                            x=100-self.player.health
                            self.player.health=self.player.health+x
                            for i in range(len(self.health_adder)):
                                self.player.health=self.player.health+self.health_adder[i]
                            print("your health is updated {}".format(self.player.health))
                        else:
                            pass
                        #It is used in order to collect money
                        print("if you wanna collect coin please press C or you can pass it by pressing any button")
                        collectcoin=input("->")
                        if collectcoin=="c" or collectcoin=="C":
                            logging.info('Player {} collected money.'.format(self.player.name))
                            self.player.coin=self.player.coin+monster.monstercoin
                            print("your coin is updated {}".format(self.player.coin))
                        else:
                            pass
                        #---------------------------LOOT SYSTEM-----------------------------------------------------------#

                        print("If you wanna return ur room pls press R")

                        returnbutton=input("->")
                        if returnbutton=="R" or returnbutton=="r":
                            logging.info('Player {}  returned base.'.format(self.player.name))
                            self.play()
                            break

                    print("You attacked! Monster health is {} and your health is {}".format(monster.max_health, self.player.health))
                    self.player.health -= monster.attack
                    #When user is killed user can gonna exit game automatically after several prompts
                    if self.player.health <= 0:
                        logging.info('Player {} is killed!'.format(self.player.name))
                        print("Sorry, You Lost the game. You have no health.")
                        print("Thank you for playing Protector of Valoria")
                        logging.info('Player {} exited the game.'.format(self.player.name))
                        sys.exit()
                 #Once user push "p" button, our hero gonna refuse the attack and gonna get damage without attacking monster. If user constantly push the button, he can suicide
                elif attack_button == "P" or attack_button == "p":
                    self.player.health -= monster.attack
                #User exit the game cuz it is dead due to the same reason before.
                    if self.player.health <= 0:
                        print("Sorry, You Lost the game. You have no health.")
                        print("Thank you for playing Protector of Valoria")
                        logging.info('Player {} lost the game.'.format(self.player.name))
                        sys.exit()
                    print("You didn't attack! Monster health is {} and your health is {}".format(monster.max_health, self.player.health))
                else:
                    pass
          else:
              #If this monster is killed before, when user try to enter the same room, this part will indicate there is no monster in that room anymore
              #It also gonna offer, you can return hero base again.
              print("There is no monster in the room. You can go back by pressing R")
              returnbutton=input("->")
              if returnbutton=="R" or returnbutton=="r":
                  self.play()

    def visit_market(self):  #To use the function enables to user buy items like sword and armor in order to obtain permanent power and health
        logging.info('Player {} entered the market.'.format(self.player.name))
        print("You have the option to visit the market where legendary swords and armors await. ")
        print("Spend your hard-earned coins wisely to increase your chances of survival.")
        time.sleep(1)
        # self.market_items = {"Black Sword": 5, "Cursed Sword": 10, "Giant Sword": 15, "Giant Axe": 20}
        print("")
        print("Swords available: " + ', '.join(self.market_items_sword.keys()))
        print("Armors available:"+", ".join(self.market_items_armor.keys()))
        print("Sword and Armor is 5 coin and other sword and armor prices increases by 5 coin")
        print("If you want to buy please enter S or if you want to buy armor please enter A ")

        pick_button=input("->")
        #It is used to pick sword if user has enough money
        if pick_button=="S" or pick_button=="s":
            print("Swords available: " + ', '.join(self.market_items_sword.keys()))
            print("Please enter a sword you want to buy")
            buy_button = input("-> ")

            if buy_button in self.market_items_sword.keys():
                #checks player money
                if self.player.coin >= self.market_items_sword[buy_button]:
                    #When user buy the item in market, the item gonna be removed from the market permanently
                    self.player.coin -= self.market_items_sword[buy_button]
                    self.player.attack += 2
                    self.market_items_sword.pop(buy_button)
                    print("Your new damage value is {}".format(self.player.attack))
                    return_button = input("You can return to the area by pressing R: ")
                    if return_button.lower() == "r":
                        self.play()
                else:
                    #If player does not, program ask you gonna stay in market or return base
                    print("Your money is not enough to buy. Please pick another sword or return to the center area.")
                    pick_option = input("If you want to stay in the market, press M. Press any other key to return: ")
                    if pick_option == "m" or pick_option=="M":
                        print("You are staying in the market")
                        self.visit_market()
                    else:
                        print("You are returning to your base")
                        self.play()
            else:
                #It ensures you need to push right button and return you to begininng prompot of the market
                logging.error('Invalid sword purchase attempt by Player {}.'.format(self.player.name))
                print("it is invalid button")
                self.visit_market()
         #It is used to pick armor if user has enough money
        elif pick_button=="A" or pick_button=="a":
            print("Armors available: " + ', '.join(self.market_items_armor.keys()))
            print("Please enter an armor you want to buy")
            buy_button = input("-> ")
            if buy_button in self.market_items_armor.keys():
                #checks player money
                if self.player.coin >= self.market_items_armor[buy_button]:
                            #When user buy the item in market, the item gonna be removed from the market permanently
                            self.player.coin -= self.market_items_armor[buy_button]
                            self.player.health += self.market_items_armor_health[buy_button]
                            self.health_adder.append(self.market_items_armor_health[buy_button])
                            self.market_items_armor.pop(buy_button)
                            print("Your new health value is {}".format(self.player.health))
                            return_button = input("You can return to the area by pressing R: ")
                            if return_button.lower() == "r":
                                self.play()

                else:
                    #If player does not, program ask you gonna stay in market or return base
                    print("Your money is not enough to buy. Please pick another armor or return to the center area.")
                    pick_option = input("If you want to stay in the market, press M. Press any other key to return: ")
                    if pick_option == "m" or pick_option=="M":
                        print("You are staying in the market")
                        self.visit_market()
                    else:
                        print("You are returning to your base")
                        self.play()
            else:
                logging.error('Invalid armor purchase attempt by Player {}.'.format(self.player.name))
                print("it is invalid button")
                self.visit_market()
        else:
            logging.error('Invalid pick attempt for armor and sword by Player {}.'.format(self.player.name))
            print("It is invalid try again please")
            self.visit_market()



    def help_menu():
        #this function is used to provide instruction to user basically about the game like guidance. In here, it is just an indicator
        print("Welcome help menu")
        print("You face off against formidable adversaries such as the Witcher, Dragon, Zombie, and more. Each battle tests your skills and strength.")
        time.sleep(2)
        print(" Defeating monsters earns you coins and experience points, allowing you to level up and acquire powerful items from the market. ")
        print("Choose wisely between different swords and armors to enhance your attack and health.")
        time.sleep(2)
        print("The only way you won the game is to kill all monsters in the room after you reach sufficient level you will be able to face with the final boss.")
        time.sleep(2)
        print("When you killed the boss, you are going to win the game")
        time.sleep(2)
        print("Directions, Armor and Sword Names should be entered exactly it is shown")
        time.sleep(2)
        print("you can go back by pressing R")
        returnbutton=input("-> ")
        if (returnbutton=="R" and returnbutton=="r"):
            title_screen_selection()



    def Screen_selection():  #It is a basically screen selection in every game like #Start #Save #Load #Help and #Exit.

        while True:  #It holds the screen until it is concluded with valid option
            print("Welcome! you can start the game by pressing 1, press 2 for help, Enter 3 in order to exit the game")

            option = input("->")
            if option == "1":  #It is start button of the game basically. When user push the button, the player gonna be spawned in hero base
                game_instance = Game()  # To initialize first settings
                game_instance.start()   #call start function in game class
            elif option == "2": #It is help menu
                Game.help_menu()
            elif option == "3":   #it exits from the game without starting the game.
                logging.info('Player {} exited the game.'.format(self.player.name))
                print("Thank you for playing Protector of Valoria")
                sys.exit()

            else:
                print("Invalid choice, please enter valid value.")
if __name__ == "__main__":
    Game.Screen_selection()  #When u start the code game class call screen selection function and rest of it comes

    pass
