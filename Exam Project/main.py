import random
import numpy as np
from game import Game, Move, Player
from MyAgent import *

def print_board(board):
        char_map = np.array(['o', 'x', ' '])

        print('  ' + ' '.join(map(str, np.arange(board.shape[0]))) +
              '\n' + '_' * (board.shape[0] * 2 + 2))
        
        for row_index, row in enumerate(board):
            print(str(row_index) + '|' + '|'.join(char_map[row]) + '|')

        print('_' * (board.shape[0] * 2 + 2))


class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move


#class MyPlayer(Player):
#    def __init__(self) -> None:
#        super().__init__()
#
#    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
#        from_pos = (random.randint(0, 4), random.randint(0, 4))
#        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
#        return from_pos, move


if __name__ == '__main__':
    win=[0,0]         # [my wins, opponent's win]
    player_0 = MyPlayer()
    player_1 = RandomPlayer()

    if False:                ##      1 Game w/random start     ##
        g = Game()
        print_board(g.get_board())
        if random.choice([0, 1]):
            print("Lorenzo is player 0. First to play")
            print("Gregorio is player 1. Second to play")
            
            player_1.set_my_player_idx(1)
            winner = g.play(player_0, player_1)
            print_board(g.get_board())


            print(f"{"Lorenzo" if not winner else "Gregorio"} wins !!")
        else:
            print("Gregorio is player 0. First to play")
            print("Lorenzo is player 1. Second to ply")
            
            player_1.set_my_player_idx(0)
            winner = g.play(player_1, player_0)
            print_board(g.get_board())

            print(f"{"Gregorio" if winner else "Lorenzo"} wins !!")

    elif False:             ##      100 Games - Agent starting first        ##
        for m in range(100):
            print(f"Game {m+1} start")
            g = Game()
            print_board(g.get_board())

            winner = g.play(my_player, opponent)
            win[winner] += 1
            print_board(g.get_board())

            print(f"Winner: Player {winner}")

        print(f"My player (o), starting first, wins {win[0]} times !!")
        print(f"Opponent (x), starting second, wins {win[1]} times !!")

    elif False:             ##      100 Games - Agent starting second       ##
        win=[0,0]
        for m in range(100):
            print(f"Game {m+1} start")
            g = Game()
            print_board(g.get_board())

            winner = g.play(opponent, my_player)
            win[1 - winner] += 1
            print_board(g.get_board())

            print(f"Winner: Player {winner}")

        print(f"My player (x), starting second, wins {win[0]} times !!")
        print(f"Opponent (o), starting first, wins {win[1]} times !!")
    
    elif True:             ##      100 Games w/ random start       ##
        win=[0, 0]
        for m in range(100):
            print(f"Game {m+1} start")
            g = Game()
            print_board(g.get_board())
            if random.choice([0, 1]):
                print("Agent is player 0. First to play")
                winner = g.play(player_0, player_1)
                print_board(g.get_board())
                print(f"{"Agent" if not winner else "Random"} wins !!")

                win[winner] += 1
            else:
                print("Agent is player 1. Second to play")
                winner = g.play(player_1, player_0)
                print_board(g.get_board())
                print(f"{"Agent" if winner else "Opponent"} wins !!")

                win[1 - winner] += 1
        print(f"Agent wins {win[0]} times !!")
        print(f"Opponent wins {win[1]} times !!")
