class tictactoe:
    def __init__(self):
        self.board = []
        self.player_turn = True
        self.player_value = "X"

    def create_board(self):
        for i in range(9):
            self.board.append('-')

    def draw_board(self):
        board_len = len(self.board)
        for i in range(board_len):
            if(i % 3 == 0):
                print()
            print(self.board[i], end=" ")
        print()

    def fill_position(self, pos, value):
        self.board[pos - 1] = value

    def check_win(self, player):
        win = None
        value = 'X' if player == "player" else 'O'
        board_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        board_len = len(board_pos)

        #check winning rows
        for i in range(board_len):
            for j in range(board_len):
                if self.board[board_pos[i][j]] != value:
                    win = False
                    break
            if win:
                return win
        
        #check winning columns
        for i in range(board_len):
            for j in range(board_len):
                if self.board[board_pos[j][i]] != value:
                    win = False
                    break
            if win:
                return win
        
        #check winning diagonals
        win = True
        for i in range(board_len):
            if self.board[board_pos[i][i]] != value:
                win = False
                break
        if win:
            return win
        
        win = True
        for i in range(board_len):
            if self.board[board_pos[i][board_len - 1 - i]] != value:
                win = False
                break
        if win:
            return win

        # for row in self.board:
        #     for val in row:
        #         if val == '-':
        #             return False
        return True

    def board_full(self):
        for val in self.board:
            if val == '-':
                return False
        return True

    def play(self):
        self.create_board()

        while True:
            if(player == 'player'):
                print("Player's Turn")
                
                self.draw_board()
                
                #player input here
                pos = int(input("Input: "))

                #fill value according to position
                self.board[pos] = self.player_value

                #check win condition
                if self.check_win("player"):
                    print("Player's win!")
                    break

            else:
                print("Computer's Turn")
                
                #com function minimax
                
                #check win condition
                if self.check_win("com"):
                    print("Player's win!")
                    break
            
            if self.board_full():
                print("Draw!")
                break
                
            #swap turn
            player = self.swap_turn(player)
            
        print()
        draw_board()

