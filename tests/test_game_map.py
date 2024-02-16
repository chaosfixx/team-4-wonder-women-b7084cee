import unittest
from levelup.gamemap import GameMap

class TestMap(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        x_minimum_value = 0
        x_maximum_value = 9
        y_minimum_value = 0
        y_maximum_value = 9
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def test_x_initialization(self):
        testobj = GameMap()
        assert testobj.status != None

        x_minimum_value = 0
        x_maximum_value = 9
        
        self.assertEqual(
            x_minimum_value,
            testobj.minimum_value
        )
        self.assertEqual (
            x_maximum_value,
            testobj.maximum_value
        )

    def test_y_initialization(self):
        testobj = GameMap()

        y_minimum_value = 0
        y_maximum_value = 9

        self.assertEqual (
            y_minimum_value,
            testobj.minimum_value,
        )
        self.assertEqual(
            y_maximum_value,
            testobj.maximum_value
        )