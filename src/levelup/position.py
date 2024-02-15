import logging
from dataclasses import dataclass
from enum import Enum

class Position(int):
    x_position: int = 4
    y_position: int = 4
    minimum_positionx: int = 0
    maximum_positionx: int = 9
    minimum_positiony: int = 0
    maximum_positiony: int = 9