from Game import Game

if __name__ == "__main__":
    game = Game()
    while True:
        game.draw()
        game.controll()
        print("\033c", end='')

        
