from Game import Game

if __name__ == "__main__":
    game = Game()
    while True:
        game.draw()
        game.run()
        if game.game_board.game_over:
            print("GAME OVER!!!")
            break
        else:
            print("\033c", end='')

        
