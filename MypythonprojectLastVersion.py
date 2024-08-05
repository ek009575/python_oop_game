import sys
import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.max_health = 200
        self.health = 100
        self.attack = 10
        self.coin=0
        self.location = 'Center Room'
        self.level = 1

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.max_health = health
        self.attack = random.randint(5, 9)
        self.monstercoin=5
        self.levelgain = 1

class Room:
    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.monsters=[]
        self.directions=[]






class Direction:
    def __init__(self,name):
        self.name=name

class Game:
    def __init__(self):

        self.monsters = []
        self.room = {}  # Initialize as a dictionary
        self.fillroom={}
        self.ourdirections = []
        self.health_adder=[]
        self.market_items_sword = {"Black Sword": 5, "Cursed Sword": 10, "Giant Sword": 15, "Giant Axe": 20}
        self.market_items_armor={"Black Armor":5,"Cursed Armor":10,"Giant Armor I":15,"Giant Armor II":20}
        self.market_items_armor_health={"Black Armor":10,"Cursed Armor":20,"Giant Armor I":30,"Giant Armor II":40}
        self.initialize_game() #IT should always be in bottom







    def initialize_game(self):

        player_name = input("Enter player name: ")

        #-----------------------------------------------------------------------

        # Define room names and descriptions
        room_names = ["South Room", "East Room", "West Room","North Room", "North East Room", "North West Room","South East Room", "South West Room"]
        room_descriptions = ["It is a South Room", "It is a East Room","It is a West Room", "It is a North Room", "It is a North East Room","It is a North West Room", "It is a South East Room", "It is a South West Room"]

        for index in range(len(room_names)):
            room = Room(room_names[index], room_descriptions[index])
            self.room[room_names[index]] = room


        #---------------------------------------------------------------------------------------------------------------
        possibledirections=["South","East","West","North","North East","North West","South East","South West"]
        for mydirection in possibledirections:

            distance_instance = Direction(mydirection)
            self.ourdirections.append(distance_instance)
        #----------------------------------------------------------------------------------------------------------------
        self.player = Player(player_name)
        #----------------------------------------------------------------------------------------------------------------
        monster_names = ["Witcher", "Dragon", "Zombie", "Headhunter", "Evil", "Orc","Goblin","BigBoss"]
        for name in monster_names:
            monster_health = random.randint(50, 80)
            monster_instance = Monster(name,monster_health)
            self.monsters.append(monster_instance)
        #----------------------------------------------------------------------------------------------------------------
        for index, room_name in enumerate(self.room):
            monsterfillingroom = [monster.name for monster in self.monsters]
            directionfillingroom = [direction.name for direction in self.ourdirections]
            self.fillroom[room_name] = (self.room[room_name].description, directionfillingroom[index], monsterfillingroom[index])
        #------------------------------------------------------------------------------------------------------------------
    def start(self):
        print("Welcome, {}. Are you ready for adventure?".format(self.player.name))
        time.sleep(2)
        self.play()

    def play(self):
        print("Player Name: " + self.player.name)
        print("Attack {}".format(self.player.attack))
        print("Max health {}".format(self.player.max_health))
        print("Health {}".format(self.player.health))
        print("Level {}".format(self.player.level))
        print("Coin {}".format(self.player.coin))
        time.sleep(2)
        print("u are in the safezone so you can move from there wherever u want")
        time.sleep(2)
        print("Enter 1 in order to move or Enter 2 for exit Enter 3 for going market")
        option = input("->")

        if option == "1":
            time.sleep(2)
            print("pickable directions are in here South,East,West,North,North East,North West,South East,South West")
            time.sleep(1)
            print("Enter value to pick ur direction")
            #option=input("-> ")


            valid_input = False
            while not valid_input:
                option = input("-> ")
                for i in range(len(self.ourdirections)):
                    if option == self.ourdirections[i].name:
                        x=option+" Room"
                        if x == "South West Room" and self.player.level < 8:
                             print("You cannot enter this room yet. Your level is not high enough.")
                             returnbutton=input("Enter R return safe safe zone: ")
                             if returnbutton=="R" or returnbutton=="r":
                                 self.play()

                             valid_input = True  # Exit the loop
                             break


                        mymonsters=self.fillroom[x][2]
                        for i in range(len(self.monsters)):

                            if mymonsters == self.monsters[i].name:
                                self.fight(self.monsters[i])

                        valid_input = True
                        break
                if not valid_input:
                    print("Invalid value. Please enter a valid direction value.")

        elif option == "2":
            time.sleep(2)
            print("Thank you for playing")
            sys.exit()
        elif option=="3":
            self.visit_market()
        else:
            print("Invalid choice. Please enter available option")
            self.play()

    def fight(self, monster):


          if monster.max_health>0:
            print("Fight Started!") #buraya if at dusman canı 0 dan buyukse savassın
            while self.player.health > 0 and monster.max_health > 0:
                print("Enter X for attack or Pass attack button is P")
                attack_button = input("-> ")
                if attack_button == "X" or attack_button == "x":
                    monster.max_health -= self.player.attack
                    if monster.max_health <= 0:

                        print("Congrats! you beat {} ! ".format(monster.name))
                        self.player.level=self.player.level+monster.levelgain




                        if monster.name == "BigBoss":
                            print("Congrats, you won the game!")
                            print("Press 'E' to exit the game or 'R' to return to the safe zone.")
                            exit_or_return = input("-> ").lower()
                            valid_input=False

                            while not valid_input:
                                if exit_or_return == "e":
                                    print("Thank you for playing")
                                    sys.exit()
                                elif exit_or_return == "r":
                                    self.play()
                                    valid_input=True
                                    break
                                else:
                                    print("Invalid option. Please enter 'E' to exit or 'R' to return to the safe zone.")

                        print("You are leveled up and your new level is {}".format(self.player.level))

                        print("If you wanna get potion please press F or you can pass it by pressing any button")
                        potbutton=input("->")
                        if potbutton=="f" or potbutton=="F":
                            x=100-self.player.health
                            self.player.health=self.player.health+x
                            for i in range(len(self.health_adder)):
                                self.player.health=self.player.health+self.health_adder[i]
                            print("your health is updated {}".format(self.player.health))
                        else:
                            pass
                        print("if you wanna collect coin please press C or you can pass it by pressing any button")
                        collectcoin=input("->")
                        if collectcoin=="c" or collectcoin=="C":
                            self.player.coin=self.player.coin+monster.monstercoin
                            print("your coin is updated {}".format(self.player.coin))
                        else:
                            pass


                        print("If u wanna return ur room pls press R")

                        returnbutton=input("->")
                        if returnbutton=="R" or returnbutton=="r":
                            self.play()
                            break
                    print("You attacked! Monster health is {} and your health is {}".format(monster.max_health, self.player.health))
                    self.player.health -= monster.attack
                    if self.player.health <= 0:
                        print("Sorry, You Lost the game. You have no health.")
                        print("Thank you for playing")
                        sys.exit()
                elif attack_button == "P" or attack_button == "p":
                    self.player.health -= monster.attack

                    if self.player.health <= 0:
                        print("Sorry, You Lost the game. You have no health.")
                        print("Thank you for playing")
                        sys.exit()
                    print("You didn't attack! Monster health is {} and your health is {}".format(monster.max_health, self.player.health))
                else:
                    pass
          else:
              print("There is no monster in the room. You can go back by pressing R")
              returnbutton=input("->")
              if returnbutton=="R" or returnbutton=="r":
                  self.play()
    def visit_market(self):  # Renamed from market to visit_market
        # self.market_items = {"Black Sword": 5, "Cursed Sword": 10, "Giant Sword": 15, "Giant Axe": 20}
        print("Swords available: " + ', '.join(self.market_items_sword.keys()))
        print("Armors available:"+", ".join(self.market_items_armor.keys()))
        print("Black Sword and Armor is 5 coin and other sword and armor prices increases by 5 coin")
        print("If you want to buy please enter S or if you want to buy armor please enter A ")

        pick_button=input("->")
        if pick_button=="S" or pick_button=="s":
            print("Swords available: " + ', '.join(self.market_items_sword.keys()))
            print("Please enter a sword you want to buy")
            buy_button = input("-> ")

            if buy_button in self.market_items_sword.keys():
                if self.player.coin >= self.market_items_sword[buy_button]:

                    self.player.coin -= self.market_items_sword[buy_button]
                    self.player.attack += 2
                    self.market_items_sword.pop(buy_button)
                    print("Your new damage value is {}".format(self.player.attack))
                    return_button = input("You can return to the area by pressing R: ")
                    if return_button.lower() == "r":
                        self.play()
                else:
                    print("Your money is not enough to buy. Please pick another sword or return to the center area.")
                    pick_option = input("If you want to stay in the market, press M. Press any other key to return: ")
                    if pick_option == "m" or pick_option=="M":
                        print("You are staying in the market")
                        self.visit_market()
                    else:
                        print("You are returning to your base")
                        self.play()
            else:
                print("it is invalid button")
                self.visit_market()

        elif pick_button=="A" or pick_button=="a":
            print("Armors available: " + ', '.join(self.market_items_armor.keys()))
            print("Please enter an armor you want to buy")
            buy_button = input("-> ")
            if buy_button in self.market_items_armor.keys():
                if self.player.coin >= self.market_items_armor[buy_button]:

                            self.player.coin -= self.market_items_armor[buy_button]
                            self.player.health += self.market_items_armor_health[buy_button]
                            self.health_adder.append(self.market_items_armor_health[buy_button])
                            self.market_items_armor.pop(buy_button)
                            print("Your new health value is {}".format(self.player.health))
                            return_button = input("You can return to the area by pressing R: ")
                            if return_button.lower() == "r":
                                self.play()

                else:
                    print("Your money is not enough to buy. Please pick another armor or return to the center area.")
                    pick_option = input("If you want to stay in the market, press M. Press any other key to return: ")
                    if pick_option == "m" or pick_option=="M":
                        print("You are staying in the market")
                        self.visit_market()
                    else:
                        print("You are returning to your base")
                        self.play()
            else:
                print("it is invalid button")
                self.visit_market()
        else:
            print("It is invalid try again please")
            self.visit_market()



    def help_menu():
        print("Welcome help menu")
        print("you can go back by pressing R")
        returnbutton=input("-> ")
        if (returnbutton=="R" and returnbutton=="r"):
            title_screen_selection()



    def Screen_selection():

        while True:
            print("Welcome! you can start the game by pressing 1, press 2 for help, Enter 3 in order to exit the game")

            option = input("->")
            if option == "1":
                game_instance = Game()  # To initialize first settings
                game_instance.start()   #call start function in game class
            elif option == "2":
                Game.help_menu()
            elif option == "3":
                print("Thank you for playing")
                sys.exit()

            else:
                print("Invalid choice, please enter valid value.")
if __name__ == "__main__":
    Game.Screen_selection()  #When u start the code game class call screen selection function and rest of it comes

    pass
