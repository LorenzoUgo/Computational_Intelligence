import random
from game import Game, Move, Player
from copy import deepcopy


class MyPlayer(Player):
    ''' Default Functions '''

    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        _, move_to_do = self.minmax_pruning(game, 2, True, game.get_current_player())
        return move_to_do[0], move_to_do[1]

    def minmax(self, game: 'Game', depth: int, maximizing: bool, player: int) -> tuple[tuple[int, int], Move]:
        ### TERMINAL STATE ###
        if depth == 0 or game.check_winner()!=-1:
            if game.check_winner()==0:
                return +(1 + 1/depth), None     #(1 + 1/depth)
            if game.check_winner()==1:
                return -(1 + 1/depth), None     #(depth*depth)
            if game.check_winner()==-1:
                return 0, None
    
        #print(depth)

        ####    Player Turn in the exploration    ####

        if maximizing:
            value = float('-inf')
            all_possible_moves = self.possible_moves(game.get_board(), player)

            random.shuffle(all_possible_moves)      #--> In case of equal state value, the move is not defined by any order

            for move in all_possible_moves:         ##      Player explore every possible move it can do      ##
                next_game_state = deepcopy(game)
                next_game_state._Game__move(move[0], move[1], player)

                tmp, _ = self.minmax(next_game_state, depth-1, False, 1-player)
                if tmp > value:
                    value = tmp
                    best_move = move
        else:
            value = float('+inf')
            all_possible_moves = self.possible_moves(game.get_board(), player)

            random.shuffle(all_possible_moves)      #--> In case of equal state value, the move is not defined by any order

            for move in all_possible_moves:         ##      Player explore every possible move it can do      ##
                next_game_state = deepcopy(game)
                next_game_state._Game__move(move[0], move[1], player)

                tmp, _ = self.minmax(next_game_state, depth-1, True, 1-player)
                if tmp < value:
                    value = tmp
                    best_move = move

        return value, best_move
    
    def minmax_pruning(self, game: 'Game', depth: int, maximizing: bool, player: int, alpha=float('-inf'), beta=float('+inf')) -> tuple[tuple[int, int], Move]:
        ### TERMINAL STATE ###
        if depth == 0 or game.check_winner()!=-1:
            if game.check_winner()==0:
                return +1, None
            else:
                return -1, None
    
        #print(depth)

        ####    Player Turn in the exploration    ####

        if maximizing:
            value = float('-inf')
            all_possible_moves = self.possible_moves(game.get_board(), player) 
            random.shuffle(all_possible_moves)          #--> In case of equal state value, the move is not defined by any order

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
                alpha = min(alpha, value)
        else:
            value = float('+inf')
            all_possible_moves = self.possible_moves(game.get_board(), player)
            random.shuffle(all_possible_moves)          #--> In case of equal state value, the move is not defined by any order

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
            for y in range(5):
                for m in [Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT]:
                    prev_status = deepcopy(status)
                    if self.__check_decision((y, x), m, status, ID_player):
                        moves.append(((x, y), m))
        return moves

    def __check_decision(self, tile, move, status, ID_player: int) -> bool:
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
        
        if acceptable:
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

    def train(self):
        pass
    
    def analyze(self):
        pass