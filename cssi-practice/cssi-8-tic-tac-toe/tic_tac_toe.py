class Board:

    WIN = 1
    CONTINUE = 0
    DRAW = -1
    PLAYERS = 2
    SIZE = 3

    def __init__(self):
        self.reset_board()

    # prepares board for new game
    def reset_board(self):
        self.rows = [[0 for i in range(Board.PLAYERS)] for i in range(Board.SIZE)]
        self.columns = [[0 for i in range(Board.PLAYERS)] for i in range(Board.SIZE)]
        self.diag = [[0 for i in range(Board.PLAYERS)] for i in range(1)]
        self.anti_diag = [[0 for i in range(Board.PLAYERS)] for i in range(1)]
        self.moves_done = []
        self.moves = 0
        # print (self.board_list)

    def update_and_checks(self, structure, loc, player):
        structure[loc][player-1]+=1
        return structure[loc][player-1] == Board.SIZE

    def valid_move(self, loc_coord):
        if loc_coord in self.moves_done:
            return False
        self.moves_done.append(loc_coord)
        return True

    # accepts a new move from the player
    # returns 0 --> no winner, game continues; 1 --> winning move, game over; -1 --> no winner, no moves, game is a draw
    def player_move(self, x, y, player):
        if not self.valid_move( (x,y) ):
            print ("Invalid Move")
            return Board.CONTINUE

        if self.update_and_checks(self.rows, x, player): return Board.WIN
        if self.update_and_checks(self.columns, y, player): return Board.WIN
        if x == y and self.update_and_checks(self.diag, 0, player): return Board.WIN
        if x+y == Board.SIZE-1 and self.update_and_checks(self.anti_diag, 0, player): return Board.WIN

        self.moves+=1
        if self.moves == Board.SIZE**2: return Board.DRAW

        return Board.CONTINUE
