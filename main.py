from pyswip import Prolog

prolog = Prolog()
prolog.consult('tictactoe-game.pl')
print(list(prolog.query("play")))