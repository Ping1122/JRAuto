from enum import IntEnum

class Status(IntEnum):
    normal = 100,
    repeat = 101,
    damagedRepeat = 102,
    terminate = 103,
    damaged = 104,
