import pygame, sys
HEIGHT= WIDTH = 900
from pyswip import Prolog

vec2 = pygame.math.Vector2

class tictactoe:
    def __init__(self, game):
        self.game = game
        self.board = []
        self.player = "player"
        self.player_turn = True
        self.player_value = "o"
        self.position = int
        self.row= int
        self.col = int
        self.field = pygame.image.load('field.png')
        self.x = pygame.image.load('X.png')
        self.o = pygame.image.load('O.png')
        self.prolog = Prolog()
        self.prolog.consult('minimax.pl')
        self.create_board()
        self.draw_board()

    def create_board(self):
        for i in range(9):
            self.board.append('n')

    def draw_board(self):
        self.game.screen.blit(self.field, (0,0))

    def redraw(self):
        for i in range(len(self.board)):
            if self.board[i] != 'n':
                self.game.screen.blit(self.x if self.board[i] == 'x' else self.o, vec2(i % 3, i // 3) * 300)
        

    def input(self):

        print("board before", self.board)
        current_cell = vec2(pygame.mouse.get_pos()) // 300
        my_pos = int(current_cell[0] + (current_cell[1] * 3))
        print(current_cell)
        print("my_pos = ",my_pos)

        left_click = pygame.mouse.get_pressed()[0]

        # if left_click and self.game_array[row][col] and not self.is_filled(pos):
        #     x, y = pygame.mouse.get_pos()
        #     if (x < 900 / 3 and y < 900 / 3):
        #         self.position = 0
        #     elif (x < 900 / 3 * 2 and y < 900 / 3):
        #         self.position = 1
        #     elif (x < 900 and y < 900 / 3):
        #         self.position = 2
        #     elif (x < 900 / 3 and y < 900 / 3 * 2):
        #         self.position = 3
        #     elif (x < 900 / 3 * 2 and y < 900 / 3 * 2):
        #         self.position = 4
        #     elif (x < 900 and y < 900 / 3 * 2):
        #         self.position = 5
        #     elif (x < 900 / 3 and y < 900):
        #         self.position = 6
        #     elif (x < 900 / 3 * 2 and y < 900):
        #         self.position = 7
        #     elif (x < 900 and y < 900):
        #         self.position = 8

        if left_click and self.board[my_pos] == 'n':
            self.board[my_pos] = self.player_value
            print("board after", self.board)
            print("board len", len(self.board))
            self.player = self.swap_turn(self.player)
            # self.position = int(my_pos)

            
    def draw_image(self):
        if self.position == 0:
            self.row = 80
            self.col = 80
        
        self.game.screen.blit(self.x, (self.row, self.col))

        pygame.display.update()

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
                    # print("check ", self.board[board_pos[i][j]], "with ", value)
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
        self.player = self.swap_turn(self.player)

    def play(self):
        if(self.player == "player"):
            print("Player's Turn")
            
            self.redraw()
            
            #player input here
            self.input()

            #check win condition
            if self.check_win("player"):
                print("Player's win!")
                return

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
                return
        
        if self.board_full():
            print("Draw!")
            return
            
        #swap turn
        # self.player = self.swap_turn(self.player)
            
        print()
        self.redraw()
    
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.tictactoe = tictactoe(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.tictactoe.play()
            self.check_events()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()