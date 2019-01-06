class Board(object):

    def __init__(self):
        self.non_diagonals = [(0, 1), (1, 0), (1, 2), (2, 1)]

    # prepares board for new game
    def reset_board(self):
        self.board_list = [[0]*3 for i in range(3)]
        # print (self.board_list)

    # accepts a new move from the player
    # returns 0 --> no winner, game continues; 1 --> winning move, game over; -1 --> no winner, no moves, game is a draw
    def player_move(self, x, y, player):
        self.board_list[x][y] = player

        #find for matches horizontally
        if self.board_list[x].count(self.board_list[x][0]) == 3:
            return 1
        #find for matches vertically
        self.compare = self.board_list[0][y]
        self.match_flag = True
        for i in range(3):
            if self.board_list[i][y] != self.compare:
                self.match_flag = False
        if self.match_flag:
            return 1
        #find for matches diagonally
        if (x,y) not in self.non_diagonals:
            self.compare = self.board_list[1][1]
            if self.compare != 0 and (self.board_list[0][0] == self.board_list[2][2] == self.compare or \
                    self.board_list[2][0] == self.board_list[0][2] == self.compare):
                 return 1

        #check if board is full or not
        for row in self.board_list:
            if 0 in row:
                return 0

        return -1
