import unittest
from levelup.gamemap import GameMap

class TestMap(unittest.TestCase):
    def test_initialization(self):
        testObj = GameMap()
        assert testObj.status != None