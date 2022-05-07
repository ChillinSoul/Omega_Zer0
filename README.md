# Omega_Zer0

 Othello-AI

 Omega_Zer0 is an ai designed to play the board game Othello.
 It's using the min-max algorithm to predict the best move taking into account current and future board states.

Othello rules: 
    source: https://service.mattel.com/instruction_sheets/T8130-Eng.pdf
__init__

    1-Each player takes 32 disks and chooses one color to use throughout the game.
    2-The to four discks (2 white 2 black) are arranged in the middle in a cross patern. 

__game__

    1-Black moves first
    2-If a player cannot outflank and flip at least one opposing disk, they forfeit their turn and their opponent moves again. However, if a move is available a player may not forfeit their turn
    3-A disk may outflank any number of disks in one or more rows in any number of directions at the same time--horizontally, vertically or diagonally. A "row" is defined as one or more disks in a continuous straight line.
    4-Players may not skip over their own color disk(s) to outflank an opposing disk.
    5-Disk(s) may only be outflanked as a direct result of a move and must fall in the direct line of the disk placed down.
    6-All disks outflanked in any one move must be flipped, even if it is to the player’s advantage not to flip them at all.
    7-A player who flips a disk that should not have been turned may correct the mistake as long as the opponent has not made a subsequent move. If the opponent has already moved, it is too late for a change and the disk(s) remain as is.
    8-Once a disk is placed on a square, it can never be moved to another square later in the game.
    9-If a player runs out of disks, but still has the opportunity to outflank an opposing disk on their turn, the opponent must give the player a disk to use. This can happen as many times as the player needs and can use a disk.
    10-When it is no longer possible for either player to move, the game is over. Disks are counted and the player with the majority of their color showing is the winner.
    Note: It is possible for a game to end before all 64 squares are filled.

__SCORING__

    Players desiring to score their games may do so by determining the margin by which a player won a game. The smaller number of disks is simply subtracted from the larger number of disks.

__strat__

    The corners are special. Corner disks can never be outflanked and, often, can protect whole collections of disks from enemy capture. In Diagram 1, the black disk at H8 protects the entire black group--no matter what happens during the rest of the game, there is no way White will ever be able to capture any of the black disks already on the board.

    At times, it might be a bad idea to place a disk next to an empty corner - you may be giving your opponent a chance to take that corner.

    Sometimes it can be difficult or impossible to find a way to capture a corner even
    though your opponent has moved into one of the ‘dangerous’ squares right next to it.


Omega-Zer0 strat: 

__Board_structure__
    [
    c ,d ,e ,e ,e ,e ,d ,c ,
    d ,d ,0 ,0 ,0 ,0 ,d ,d ,
    e ,0 ,0 ,0 ,0 ,0 ,0 ,e ,
    e ,0 ,0 ,sb,sw,0 ,0 ,e ,
    e ,0 ,0 ,sw,sb,0 ,0 ,e ,
    e ,0 ,0 ,0 ,0 ,0 ,0 ,e ,
    d ,d ,0 ,0 ,0 ,0 ,d ,d ,
    c ,d ,e ,e ,e ,e ,d ,c
    ]
    c(corners)  :[0,7,56,63] great position, unflipable 
    d(danger)   :[1,6,8,9,14,15,48,49,54,55,57,62] bad position if the corner is not atributed (gateawy to the corner for the opponent)
    e(edge)     :[2,3,4,5,16,23,24,31,32,39,40,47,58,59,60,61] good position
    sw(strt_wht):[28,35] defautl start position 
    sb(strt_blk):[27,36] default start position 


__MinMax__
    Given a board state, a node is created. This node represent the current gamestate, recurcively a node tree is then created. The minimax algorithm will then go down the tree all the way to the first leave. it will then evaluate all the leaves connected to the same node and set this node's value to the best leave's value (maximum for the maximizing player and minimum for the minimizing player). it will to the same for all the subsequent nodes going up and down the tree. 
    once all the nodes have been evaluated, the algorithm will return the best move to play at depth 0 (the actual turn).
__AB_Pruning__
    The algorithm will keep a copy of the current best move for either players(alpha and beta). If the algorithm detects that a node's result can't affect the outcome, this node won't be evaluated saving computational recources. 



