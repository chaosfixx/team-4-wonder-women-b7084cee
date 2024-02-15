from levelup.position import Position
class Character:
    name: str
    move_count: int = 0
    current_position: None

    def getStatus(self):
        print  ("Inside Character getStatus")

    def __init__(self, c_name):
        self.name = c_name
        print("Character name: "+ self.name)