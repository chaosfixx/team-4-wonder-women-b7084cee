from unittest import TestCase
from levelup.position import Position

# THIS IS AN EXAMPLE UNIT TEST. 
# All the unit tests for the Position should go here
# Unit tests for other classes should be in their own .py files (like test_character.py)
class TestPosition(TestCase):
    def test_init(self):
        testObj = Position()
        x_position = 4
        y_position = 4
        #assert testObj.status != None