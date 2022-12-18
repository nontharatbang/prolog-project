:- module(minimax, [minimax/2]).

% All win positions for tic-tac-toe
win(P, [P, P, P, _, _, _, _, _, _]).
win(P, [_, _, _, P, P, P, _, _, _]).
win(P, [_, _, _, _, _, _, P, P, P]).
win(P, [P, _, _, P, _, _, P, _, _]).
win(P, [_, P, _, _, P, _, _, P, _]).
win(P, [_, _, P, _, _, P, _, _, P]).
win(P, [P, _, _, _, P, _, _, _, P]).
win(P, [_, _, P, _, P, _, P, _, _]).

% swap min max
swap(max, min).
swap(min, max).

% player -> we trying to max value for bot(o)
player(max, o).
player(min, x).

% full board if there is no n in the board
board_full(Board) :-
    \+ member(n, Board).

% find possible move
moves(P, [n | Rest], [P | Rest]).
moves(P, [X | Rest], [X | Rest2]) :-
    moves(P, Rest, Rest2).

% find all possible move
all_moves(P, Board, AllMoves) :-
    findall(Move, moves(P, Board, Move), AllMoves).

% evaluate boards
eval_board([], Value) :-
    Value is 0.
eval_board(Board, Value) :-
    win(o, Board),
    Value is 10, !.
eval_board(Board, Value) :-
    win(x, Board),
    Value is -10, !.
eval_board(Board, Value) :-
    board_full(Board),
    Value is 0.

% compare each value and return better move and its value
better_moves(max, MoveA, ValueA, _, ValueB, MoveA, ValueA) :-
	ValueA >= ValueB.
better_moves(max, _, ValueA, MoveB, ValueB, MoveB, ValueB) :-
	ValueA < ValueB.
better_moves(min, MoveA, ValueA, _, ValueB, MoveA, ValueA) :-
	ValueA =< ValueB.
better_moves(min, _, ValueA, MoveB, ValueB, MoveB, ValueB) :-
	ValueA > ValueB.

% find the best move
best_move(max, [], [], -1).
best_move(min, [], [], 1).
best_move(MinMax, [Move | Rest], BestMove, BestValue) :-
    eval_board(Move, Value),
    best_move(MinMax, Rest, BestMove1, BestValue1),
	better_moves(MinMax, Move, Value, BestMove1, BestValue1, BestMove, BestValue).
best_move(MinMax, [Move | Rest], BestMove, BestValue) :-
	best_move(MinMax, Rest, BestMove1, BestValue1),
	swap(MinMax, Other),
	find_solution(Other, Move, _, BestValue2),
	better_moves(MinMax, Move, BestValue2, BestMove1, BestValue1, BestMove, BestValue).

% find best possible move according to available board
find_solution(MinMax, Board, BestMove, BestValue) :-
	player(MinMax, Color),
	all_moves(Color, Board, AllMoves),
    best_move(MinMax, AllMoves, BestMove, BestValue).

% return best move according to input board
minimax(Board, BestMove) :-
	find_solution(max, Board, BestMove, _), !.