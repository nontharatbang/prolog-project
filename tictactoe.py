class tictactoe:
    def __init__(self):
        self.board = []
        self.player_turn = True
        self.player_value = "X"

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)

    def draw_board(self):
        for row in self.board:
            for val in row:
                print(val, end=" ")
            print()

    def fill_position(self, row, col, value):
        self.board[row][col] = value

    def check_win(self, player):
        win = None
        board_len = len(self.board)
        value = 'X' if player == "player" else 'O'
        #check winning rows
        for i in range(board_len):
            for j in range(board_len):
                if self.board[i][j] != value:
                    win = False
                    break
            if win:
                return win
        
        #check winning columns
        for i in range(board_len):
            for j in range(board_len):
                if self.board[j][i] != value:
                    win = False
                    break
            if win:
                return win
        
        #check winning diagonals
        win = True
        for i in range(board_len):
            if self.board[i][i] != value:
                win = False
                break
        if win:
            return win
        
        win = True
        for i in range(board_len):
            if self.board[i][board_len - 1 - i] != value:
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
        for row in self.board:
            for val in row:
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
                row, col = list(map(int, input("Input: ").split()))

                #fill value according to position
                self.board[row][col] = self.player_value

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

