import pygame, sys
from TicTacToe import *
from Constant import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.tictactoe = TicTacToe(self)
    
    def new_game(self):
        self.tictactoe = TicTacToe(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.new_game()

    def run(self):
        while True:
            self.tictactoe.play()
            self.check_events()
            pygame.display.update()
            self.clock.tick(60)