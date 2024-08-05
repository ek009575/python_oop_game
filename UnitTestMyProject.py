import unittest
from unittest.mock import patch
from myproject import Game,Player,Monster,Room,Direction

class TestPlayerInitialization(unittest.TestCase):
    def test_player_initialization(self):
        entered_player_name = "Test_Player"
        player = Player(entered_player_name)

        self.assertEqual(player.name, entered_player_name)
        self.assertEqual(player.max_health, 200)
        self.assertEqual(player.health, 100)
        self.assertEqual(player.attack, 10)
        self.assertEqual(player.level, 1)
class TestMonster(unittest.TestCase):

    def test_monster_initialization(self):
        # Test monster initialization
        entered_monster_name = "Test_Monster"
        entered_monster_health = 75
        monster = Monster(entered_monster_name, entered_monster_health)

        self.assertEqual(monster.name, entered_monster_name)
        self.assertEqual(monster.max_health, entered_monster_health)
        self.assertTrue(5 <= monster.attack and monster.attack<= 9)
        self.assertEqual(monster.levelgain, 1)
class TestRoom(unittest.TestCase):
    def test_room_initialization(self):
        # Test room initialization
        room_name = "Test_Room"
        room_description = "This is a test room."
        room = Room(room_name, room_description)

        self.assertEqual(room.name, room_name)
        self.assertEqual(room.description, room_description)
        self.assertEqual(room.monsters, [])
        self.assertEqual(room.directions, [])

class TestDirection(unittest.TestCase):
    def test_direction_initialization(self):
        expected_direction_name = "Test_Direction"
        direction = Direction(expected_direction_name)
        self.assertEqual(direction.name, expected_direction_name)
class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()



    def test_fillroom_attribute(self):
        # Check if fillroom attribute is initialized as an empty dictionary
        self.assertIsInstance(self.game.fillroom, dict)
        self.assertEqual(len(self.game.fillroom), 8)
    def test_room_attribute(self):
        # Check if room attribute is initialized as an empty dictionary
        self.assertIsInstance(self.game.room, dict)
        self.assertEqual(len(self.game.room), 8)
    def test_monsters_attribute(self):
        # Check if monsters attribute is initialized as an empty list
        self.assertIsInstance(self.game.monsters, list)
        self.assertEqual(len(self.game.monsters), 8)
    def test_ourdirections_attribute(self):
        self.assertEqual(len(self.game.ourdirections), 8)
    def test_health_adder_attribute(self):
        # Check if health_adder attribute is initialized as an empty list
        self.assertIsInstance(self.game.health_adder, list)
        self.assertEqual(len(self.game.health_adder), 0)
    def test_market_items_sword_attribute(self):
        # Check if market_items_sword attribute is initialized as expected
        expected_market_items_sword = {"Black Sword": 5, "Cursed Sword": 10, "Giant Sword": 15, "Giant Axe": 20}
        self.assertEqual(self.game.market_items_sword, expected_market_items_sword)

    def test_market_items_armor_attribute(self):
        # Check if market_items_armor attribute is initialized as expected
        expected_market_items_armor = {"Black Armor": 5, "Cursed Armor": 10, "Giant Armor I": 15, "Giant Armor II": 20}
        self.assertEqual(self.game.market_items_armor, expected_market_items_armor)

    def test_market_items_armor_health_attribute(self):
        # Check if market_items_armor_health attribute is initialized as expected
        expected_market_items_armor_health = {"Black Armor": 10, "Cursed Armor": 20, "Giant Armor I": 30, "Giant Armor II": 40}
        self.assertEqual(self.game.market_items_armor_health, expected_market_items_armor_health)



    def testgame_initialization(self):


        # Check if player is properly initialized
        self.assertEqual(self.game.player.name, 'Test_Player')

        # Check if rooms are properly initialized
        self.assertEqual(len(self.game.room), 8)  # Assuming 8 rooms are created

        # Check if directions are properly initialized
        self.assertEqual(len(self.game.ourdirections), 8)  # Assuming 8 directions are created

        # Check if monsters are properly initialized
        self.assertEqual(len(self.game.monsters), 8)  # Assuming 8 monsters are created



        for myitems in self.game.fillroom.values():
            self.assertIn(myitems[0], ["It is a South Room", "It is a East Room","It is a West Room", "It is a North Room", "It is a North East Room","It is a North West Room", "It is a South East Room", "It is a South West Room"])
            self.assertIn(myitems[1], ["South", "East", "West", "North", "North East", "North West", "South East", "South West"])  # Check if direction is valid
            self.assertIn(myitems[2], ["Witcher", "Dragon", "Zombie", "Headhunter", "Evil", "Orc", "Goblin", "BigBoss"])  # Check if monster name is valid

        for myroom in self.game.fillroom.keys():

            self.assertIn(myroom,["South Room", "East Room", "West Room","North Room", "North East Room", "North West Room","South East Room", "South West Room"])




if __name__ == '__main__':
    unittest.main()
