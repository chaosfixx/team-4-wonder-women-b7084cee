import logging
from dataclasses import dataclass
from enum import Enum
from levelup.character import Character

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    character_name: str = "Character"
    #character: Character
    move_count: int = 0
    running: bool = False
    current_position: tuple = (4, 4)

    def __str__(self) -> str:
        return f"{self.character_name} moved {self.move_count} times."
    
    def set_character_position(self, xycoordinates: tuple):
        print("Set character position state for testing")
        self.current_position=xycoordinates
        print("Current position: " + str( self.current_position[0] )+ "," +str( self.current_position[1]) )

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class GameController:
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()
        self.character= Character("default")

    def start_game(self):
        pass

    def create_character(self, character_name: str) -> None:
        pass

    def move(self, direction: Direction):
        self.status.set_character_position( GameStatus.current_position)
        print (direction)
        if (direction == Direction.NORTH):
            print ("NORTH" )
            newtuple = (GameStatus.current_position[0], GameStatus.current_position[1] + 1)
            #self.status.set_character_position( GameStatus.current_position )
            self.status.set_character_position( newtuple)
            self.status.move_count = self.status.move_count + 1
            print ("Current move count: " + str(self.status.move_count) )

        elif (direction == Direction.SOUTH):
            print ("SOUTH" )
            newtuple = (GameStatus.current_position[0], GameStatus.current_position[1] - 1)
            #self.status.set_character_position( GameStatus.current_position )
            self.status.set_character_position( newtuple)
            self.status.move_count = self.status.move_count + 1
            print ("Current move count: " + str(self.status.move_count) )

        elif (direction == Direction.EAST):
            print ("EAST" )
            newtuple = (GameStatus.current_position[0] + 1, GameStatus.current_position[1])
            #self.status.set_character_position( GameStatus.current_position )
            self.status.set_character_position( newtuple)
            self.status.move_count = self.status.move_count + 1
            print ("Current move count: " + str(self.status.move_count) )

        elif (direction == Direction.WEST):
            print ("WEST" )
            newtuple = (GameStatus.current_position[0] - 1, GameStatus.current_position[1])
            #self.status.set_character_position( GameStatus.current_position )
            self.status.set_character_position( newtuple)
            self.status.move_count = self.status.move_count + 1
            print ("Current move count: " + str(self.status.move_count) )
           
        
