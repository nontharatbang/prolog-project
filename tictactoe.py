from pyswip import Prolog

class TicTacToe:
    def __init__(self):
        self.board = []
        self.player_turn = True
        self.player_value = "o"
        self.prolog = Prolog()
        self.prolog.consult('minimax.pl')

    def create_board(self):
        for i in range(9):
            self.board.append('n')

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
        value = 'o' if player == "player" else 'x'
        board_pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        board_len = len(board_pos)

        if self.board_full():
            return False

        #check winning rows
        for i in range(board_len):
            win = True
            for j in range(board_len):
                if self.board[board_pos[i][j]] != value:
                    print("check ", self.board[board_pos[i][j]], "with ", value)
                    win = False
                    break
            if win:
                print("win row")
                return win

        
        #check winning columns
        for i in range(board_len):
            win = True
            for j in range(board_len):
                if self.board[board_pos[j][i]] != value:
                    win = False
                    break
            if win:
                print("win col")
                return win
        
        #check winning diagonals
        win = True
        for i in range(board_len):
            if self.board[board_pos[i][i]] != value:
                win = False
                break
        if win:
            print("win diagonal left")
            return win
        
        win = True
        for i in range(board_len):
            if self.board[board_pos[i][board_len - 1 - i]] != value:
                win = False
                break
        if win:
            print("win diagonal right")
            return win

        for val in self.board:
            if val == 'n':
                return False

        print("win default")
        return True

    def board_full(self):
        for val in self.board:
            if val == 'n':
                return False
        return True

    def swap_turn(self, player):
        return "com" if player == "player" else "player"
    
    def is_filled(self, pos):
        return True if self.board[pos] != 'n' else False

    def bot_move(self, new_board):
        for i in range(len(new_board)):
            self.board[i] = str(new_board[i])

    def play(self):
        self.create_board()

        player = "player"
        while True:
            if(player == "player"):
                print("Player's Turn")
                
                self.draw_board()
                
                #player input here
                pos = int(input("Input: "))
                if self.is_filled(pos):
                    print("The position is already filled. Choose a new one.")
                    continue

                #fill value according to position
                self.board[pos] = self.player_value

                #check win condition
                if self.check_win("player"):
                    print("Player's win!")
                    break

            else:
                print("Computer's Turn")
                
                self.draw_board()
                #com function minimax
                # pos = sorted(self.prolog.query("minimax({}, Pos".format(self.board)))
                new_val = sorted(self.prolog.query("minimax({}, Pos)".format(self.board)))[0]["Pos"]
                self.bot_move(new_val)
                
                #check win condition
                if self.check_win("com"):
                    print("Bot's win!")
                    break
            
            if self.board_full():
                print("Draw!")
                break
                
            #swap turn
            player = self.swap_turn(player)
            
        print()
        self.draw_board()

game = TicTacToe()
game.play()