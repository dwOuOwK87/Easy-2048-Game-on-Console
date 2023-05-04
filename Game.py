from Board import Board, Direction

class Game:
    def __init__(self):
        self.USER_INPUT_DIC = {
            0 : Direction.UP,
            1 : Direction.RIGHT,
            2 : Direction.DOWN,
            3 : Direction.LEFT
            }

        self.game_board = Board()
        self.game_board.generate(2)
        
    def run(self):
        try:
            user_input = int(input("(0: UP, 1: RIGHT, 2: DOWN, 3: LEFT) Input: "))
            if not self.USER_INPUT_DIC.get(user_input):
                return self.run()
        except:
            return self.run()

        self.game_board.moving(self.USER_INPUT_DIC.get(user_input))

    def draw(self):
        for col in self.game_board.board:
            for item in col:
                print(f"{item:<5d}", end = "")
            print()



    



        
