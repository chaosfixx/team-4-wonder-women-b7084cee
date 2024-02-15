
import unittest
from levelup.character import Character

# THIS IS AN EXAMPLE UNIT TEST. 
# All the unit tests for the Character should go here
# Unit tests for other classes should be in their own .py files (like test_character.py)

class TestCharacter(unittest.TestCase):
    def test_initialization(self):
        testObj = Character()
        assert testObj.name != None
        