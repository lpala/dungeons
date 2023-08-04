from enum import Enum


class Chest:
    id = int
    chestType = Enum
    itemsStashed = list()
    goldStashed = int


class ChestType(Enum):
    Wooden = 1
    Iron = 2
    Silver = 3
    Golden = 4
    Diamond = 5
