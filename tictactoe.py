from pyswip import Prolog
from Constant import *

TILE_SIZE = WIDTH // 3

class TicTacToe:
    def __init__(self, game):
        self.game = game
        self.board = []
        self.game_end = False
        self.player = 'player'
        self.player_value = 'o'
        self.board_bg = pygame.image.load('./Resources/field.png')
        self.x_image = pygame.image.load('./Resources/X.png')
        self.o_image = pygame.image.load('./Resources/O.png')
        self.font = pygame.font.SysFont('Verdana', 150 // 4, True)
        self.prolog = Prolog()
        self.prolog.consult('minimax.pl')
        
        self.create_board()
        self.draw_board()

    def create_board(self):
        for i in range(9):
            self.board.append('n')

    def draw_board(self):
        self.game.screen.blit(self.field, (0, 0))
        pygame.display.set_caption('Minimax TicTacToe')

    def redraw(self):
        for i in range(len(self.board)):
            if self.board[i] != 'n':
                self.game.screen.blit(self.x if self.board[i] == 'x' else self.o, vec2(i % 3, i // 3) * 300)

    def player_input(self):
        current_tile = vec2(pygame.mouse.get_pos()) // TILE_SIZE
        tile_pos = int(current_tile[0] + (current_tile[1] * 3))
        print("tile position: ", tile_pos)

        left_click = pygame.mouse.get_pressed()[0]

        if left_click and self.board[tile_pos] == 'n' and not self.game_end:
            self.board[tile_pos] = self.player_value
            self.player = self.swap_turn(self.player)

    def draw_winner(self):
        if self.check_win('player'):
            label = self.font.render(f'Player wins! Press Spacbar to Restart', True, 'white', 'black')
            self.game.screen.blit(label, (WIDTH // 2 - label.get_width() // 2, WIDTH // 4))
        elif self.check_win('bot'):
            label = self.font.render(f'Bot wins! Press Spacbar to Restart', True, 'white', 'black')
            self.game.screen.blit(label, (WIDTH // 2 - label.get_width() // 2, WIDTH // 4))

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
                #if the value is not the current player's value
                if self.board[board_pos[i][j]] != value:
                    win = False
                    break
            if win:
                self.game_end = True
                return win
        
        #check winning columns
        for i in range(board_len):
            win = True
            for j in range(board_len):
                if self.board[board_pos[j][i]] != value:
                    win = False
                    break
            if win:
                self.game_end = True
                return win
        
        #check winning diagonals
        win = True
        for i in range(board_len):
            if self.board[board_pos[i][i]] != value:
                win = False
                break
        if win:
            self.game_end = True
            return win
        
        win = True
        for i in range(board_len):
            if self.board[board_pos[i][board_len - 1 - i]] != value:
                win = False
                break
        if win:
            self.game_end = True
            return win

        return False
        
        # for val in self.board:
        #     if val == 'n':
        #         return False


    def board_full(self):
        for val in self.board:
            if val == 'n':
                return False
        return True

    def swap_turn(self, player):
        return 'bot' if player == 'player' else 'player'

    def bot_move(self, new_board):
        for i in range(len(new_board)):
            self.board[i] = str(new_board[i])
        self.player = self.swap_turn(self.player)

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