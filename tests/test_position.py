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

    def test_init(self):
        testObj = Position()
        expected_minimum_positionx = 0
        expected_maximum_positionx = 9
        expected_minimum_positiony = 0
        expected_maximum_positiony = 9

        def test_x_coordinates(self):
            myposition = Position()
            self.assertTrue(0 >= myposition.x_position <=9)

        def test_y_coordinates(self):
            myposition = Position()
            self.assertTrue(0 >= myposition.y_position <=9 )
