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

    def test_init(self):
        testObj = Position()
        expected_minimum_positionx = 0
        expected_maximum_positionx = 9
        expected_minimum_positiony = 0
        expected_maximum_positiony = 9
        #assert testObj.status != None
        self.assertEqual(
            expected_minimum_positionx,
            testObj.minimum_positionx
        )
        self.assertEqual(
            expected_minimum_positiony,
            testObj.minimum_positiony
        )
        self.assertEqual(
            expected_maximum_positionx,
            testObj.maximum_positionx
        )
        self.assertEqual(
            expected_maximum_positiony,
            testObj.maximum_positiony
        )
        #self.assertEqual(
        #    x_position = 4,
        #    y_position = 4
        #)

       