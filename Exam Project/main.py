import random
from game import Game, Move, Player
from agent import *


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
    g=Game()
    pl = MyPlayer()
    moves = pl.possible_moves(g.get_board(), 1)

    for m in moves:
        print(m)

    #win=0
    #for m in range(25):
    #    print(f"Game {m+1} start")
    #    g = Game()
    #    #g.print()
    #    player1 = MyPlayer()
    #    player2 = RandomPlayer()
    #    winner = g.play(player1, player2)
    #    if not winner:
    #        win+=1
    #    #g.print()
    #    print(f"Winner: Player {winner}")
    #
    #print(str(win*4)+"% win rate !!")

