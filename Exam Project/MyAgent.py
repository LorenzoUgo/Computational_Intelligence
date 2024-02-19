import random
from game import Game, Move, Player
from copy import deepcopy
import collections
import numpy


class MyPlayer(Player):
    ''' Default Functions '''

    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        self.my_ID = game.get_current_player()
        _, move_to_do = self.minmax_pruning(game, 3, True, game.get_current_player())

        return move_to_do[0], move_to_do[1]
    
    def minmax_pruning(self, game: 'Game', depth: int, maximizing: bool, player: int, alpha=float('-inf'), beta=float('+inf')) -> tuple[tuple[int, int], Move]:

        ### TERMINAL STATE ###
        if depth == 0 or game.check_winner()!=-1:
            return self.__evaluate(game, self.my_ID), None
    
        ####    Player Turn in the exploration    ####
        if maximizing:
            value = float('-inf')
            all_possible_moves = self.possible_moves(game.get_board(), player) 
            random.shuffle(all_possible_moves)      #--> In case of equal state value, the move is not defined by any order

            for move in all_possible_moves:         ##      Player explore every possible move it can do      ##
                next_game_state = deepcopy(game)
                next_game_state._Game__move(move[0], move[1], player)
                tmp, _ = self.minmax_pruning(next_game_state, depth-1, False, 1-player, alpha, beta)

                if tmp > value:
                    value = tmp
                    best_move = move

                #   Alpha Beta Pruning  #
                if value >= beta:
                    break
                alpha = max(alpha, value)
        else:
            value = float('+inf')
            all_possible_moves = self.possible_moves(game.get_board(), player) 
            random.shuffle(all_possible_moves)      #--> In case of equal state value, the move is not defined by any order

            for move in all_possible_moves:         ##      Player explore every possible move it can do      ##
                next_game_state = deepcopy(game)
                next_game_state._Game__move(move[0], move[1], player)
                tmp, _ = self.minmax_pruning(next_game_state, depth-1, False, 1-player, alpha, beta)

                if tmp < value:
                    value = tmp
                    best_move = move
                
                #   Alpha Beta Pruning  #
                if value <= alpha:
                    break
                beta = min(beta, value)

        return value, best_move

    def possible_moves(self, status, ID_player: int) -> list[tuple[int, int], Move]:
        moves = []
        for x in range(5):
            if x in [0, 4]:
                for y in range(5):
                    if self.__check_tile((y, x), status, ID_player):
                        for m in [Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT]:
                            if self.__check_slide((y, x), m):
                                moves.append(((x, y), m))        #((coord_x, coord_y), slide)
            else:
                for y in [0, 4]:
                    if self.__check_tile((y, x), status, ID_player):
                        for m in [Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT]:
                            if self.__check_slide((y, x), m):
                                moves.append(((x, y), m))        #((coord_x, coord_y), slide)

        return moves

    def __check_tile(self, tile, status, ID_player: int) -> bool:
        acceptable: bool = (
                # check if it is in the first row
            (tile[0] == 0 and tile[1] < 5)
                # check if it is in the last row
            or (tile[0] == 4 and tile[1] < 5)
                # check if it is in the first column
            or (tile[1] == 0 and tile[0] < 5)
                # check if it is in the last column
            or (tile[1] == 4 and tile[0] < 5)
                # and check if the piece can be moved by the current player
        ) and (status[tile] < 0 or status[tile] == ID_player)
        
        return acceptable

    def __check_slide(self, tile, move) -> bool:
        if tile not in [(0, 0), (0, 4), (4, 0), (4, 4)]:
            acceptable_top: bool = tile[0] == 0 and ( move == Move.BOTTOM or move == Move.LEFT or move == Move.RIGHT )  # it can be replaced down, left or right

            acceptable_bottom: bool = tile[0] == 4 and ( move == Move.TOP or move == Move.LEFT or move == Move.RIGHT )  # it can be replaced up, left or right
            
            acceptable_left: bool = tile[1] == 0 and ( move == Move.BOTTOM or move == Move.TOP or move == Move.RIGHT )  # it can be replaced up, down or right
            
            acceptable_right: bool = tile[1] == 4 and ( move == Move.BOTTOM or move == Move.TOP or move == Move.LEFT )  # it can be replaced up, down or left
        # if the piece position is in a corner
        else:
            acceptable_top: bool = tile == (0, 0) and ( move == Move.BOTTOM or move == Move.RIGHT ) # it can be replaced to the right and down
            
            acceptable_left: bool = tile == (4, 0) and ( move == Move.TOP or move == Move.RIGHT )   # it can be replaced to the right and up

            acceptable_right: bool = tile == (0, 4) and ( move == Move.BOTTOM or move == Move.LEFT )# it can be replaced to the left and down
            
            acceptable_bottom: bool = tile == (4, 4) and ( move == Move.TOP or move == Move.LEFT )  # it can be replaced to the left and up
        
        # check if the move is acceptable
        acceptable: bool = acceptable_top or acceptable_bottom or acceptable_left or acceptable_right
        return acceptable
    
    def __evaluate(self, game: Game, ID_player: int) -> int:
        status = game.get_board()
        transpose = game.get_board().transpose()		# columns in board = rows in transpose
        playercount = []            # count current player symbol in rows/columns/diags
        opponentcount = []          # count opponent symbol in rows/columns/diags
        for row, column in zip(status, transpose):      # half computational time

            rowcounter = collections.Counter(row)
            columncounter = collections.Counter(column)
            playercount.append(rowcounter.get(ID_player, 0))  # 0 se non trova il simbolo del giocatore
            playercount.append(columncounter.get(ID_player, 0))   # se trova il simbolo del giocatore invece, inserisce le sue occorrenze
            opponentcount.append(rowcounter.get(1 - ID_player, 0))
            opponentcount.append(columncounter.get(1 - ID_player , 0))

        
        diagonals = [numpy.diag(status), numpy.diag(numpy.fliplr(status))]
        main_diagonal_count = collections.Counter(diagonals[0])
        second_diagonal_count = collections.Counter(diagonals[1])
        playercount.append(main_diagonal_count.get(ID_player, 0))
        playercount.append(second_diagonal_count.get(ID_player, 0))
        opponentcount.append(main_diagonal_count.get(1 - ID_player, 0))
        opponentcount.append(second_diagonal_count.get(1 - ID_player, 0))

		# max(count): maximum number of player's tiles in a row, column, or a diagonal (the highest value is 5)
		# max(opponentcount): maximum number of opponent's tiles in a row, column, or a diagonal (the highest value is 5)
        scoremax = 5 ** max(playercount)
        scoremin = 5 ** max(opponentcount)

        return scoremax - scoremin
    