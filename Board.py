from random import randint
from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(4)] for _ in range(4)]
        self.DIRECTION_VECTOR = [
            ( 0,-1),
            ( 1, 0),
            ( 0, 1),
            (-1, 0),
            ]

        self.baned_overlay = []
        self.direction = None

    def generate(self, amount: int = 1):
        if amount <= 0:
            return

        positions = []
        while len(positions) != amount:
            x, y = randint(0, 3), randint(0, 3)
            if (x, y) in positions or self.board[y][x] != 0:
                continue
            positions.append((x, y))
            
        for x, y in positions:
            self.board[y][x] = 2

    def out_of_range(self, x: int, y: int):
        return x < 0 or x >= 4 or y < 0 or y >= 4

    def step(self, x: int, y: int):
        if self.board[y][x] == 0:
            return False

        _x = x + self.DIRECTION_VECTOR[self.direction.value][0]
        _y = y + self.DIRECTION_VECTOR[self.direction.value][1]

        if self.out_of_range(_x, _y):
            return False

        if self.board[_y][_x] == 0:
            self.board[_y][_x] = self.board[y][x]
            self.board[y][x] = 0
            return True

        if self.board[_y][_x] == self.board[y][x] and not (x, y) in self.baned_overlay:
            self.board[_y][_x] += self.board[y][x]
            self.board[y][x] = 0
            self.baned_overlay.append((_x, _y))
            return True

        return False

    def moving(self, direction: Direction):
        self.baned_overlay.clear()
        self.direction = direction

        while True:
            movingCounter = 0
            for y in range(4):
                for x in range(4):
                    movingCounter += 1 if self.step(x, y) else 0
            if movingCounter == 0:
                break

        self.generate(1)




                    