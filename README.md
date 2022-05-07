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




