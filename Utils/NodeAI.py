
import numpy as np
from easyAI import Negamax, TwoPlayerGame,AI_Player

#custom boards 
center_pos = [(3,3),(3,4),(4,3),(4,4)]
buffer_pos = [[(0,1),(1,0),(1,1)],[(0,6),(1,6),(1,7)],[(6,0),(6,1),(7,1)],[(6,6),(6,7),(7,6)]]
corner_pos = [(0,0),(0,7),(7,0),(7,7)]
edge_pos   = [[(0,x)for x in range(1,7)],[(7,x)for x in range(1,7)],[(x,0)for x in range(1,7)],[(x,7)for x in range(1,7)]]
diag_pos   = [[(i,i)for i in range(2,6)],[(i,7-i)for i in range(2,6)]]

#premade boards
chicken_diner=[
            [20, 2, 4, 4, 4, 4, 2, 20],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [9, 2, 4, 4, 4, 4, 4, 9]
        ]
chicken_lunch=[
            [20, 4, 4, 4, 4, 4, 2, 20],
            [2, 0, 1, 1, 1, 1, 0, 2],
            [4, 1, 2, 2, 2, 2, 1, 4],
            [4, 1, 2, 3, 3, 2, 1, 4],
            [4, 1, 2, 3, 3, 2, 1, 4],
            [4, 1, 2, 2, 2, 2, 1, 4],
            [2, 0, 1, 1, 1, 1, 0, 2],
            [20, 2, 4, 4, 4, 4, 4, 20]
        ]
chicken_starter=[
            [9, 4, 4, 4, 4, 4, 2, 9],
            [2, -1, 2, 1, 1, 1, -1, 2],
            [4, 2, 2, 1, 1, 1, 1, 4],
            [4, 1, 1, 5, 5, 1, 1, 4],
            [4, 1, 1, 5, 5, 1, 1, 4],
            [4, 2, 2, 1, 1, 2, 2, 4],
            [2, -1, 2, 1, 1, 2, -1, 2],
            [9, 2, 4, 4, 4, 4, 4, 9]
        ]


###----------custom boards
def extract_disks(board):
    """
    tansforms the board into two different lists of player positions
    board->[[player 1][player 2]]
    """
    result = ([],[])
    for l,line in enumerate( board ) :
        for c,disk in enumerate ( line ):
            if disk :result[disk-1].append((l,c)) 
    return result

def get_futures_dif(game):
    """
    calculates the move potential of for current board
    possible_moves for the current player - possible_moves for the opponent
    """
    return len(game.possible_moves())-len(game.possible_moves(True))
    
def give_point(board:list,pos:list,points:int):
    """
    attributes the chosen value to the chosen positions on the board
    """
    for p in pos:board[p[0]][p[1]]+=points

def give_points(board:list,points:list):
    """
    attributes the chosen values to all the diferent sections of the board
    """

    give_point(board,center_pos,points[0])
    
    give_point(board,buffer_pos[0]+buffer_pos[1]+buffer_pos[2]+buffer_pos[3],points[1])
    
    give_point(board,edge_pos[0] + edge_pos[1] + edge_pos[2] + edge_pos[3]  ,points[2])
    
    give_point(board,diag_pos[0] + diag_pos[1]  ,points[3])
    
    give_point(board,corner_pos,points[4])
    
###----------custom boards    

def make_scoreboard(game:TwoPlayerGame):
    """
    creates a scoreboard to reference the positions agaist, used to calculate the score
    """
    score_board = np.ones((8,8),dtype=int)
    
    game_stage = 64-np.sum(game.board ==0)
    
    if game_stage <10:           #3,-5,3,2,9
        #give_points(score_board,[1,-5,3,2,9])
        score_board = chicken_starter
        
        bonus = 1
    elif game_stage <20:
        #give_points(score_board,[1,-5,3,2,20])
        score_board = chicken_lunch
        bonus = 1.2
    else:
        give_points(score_board,[1,1,1,1,20])
        #score_board = chicken_diner
        bonus = 222
    
    return score_board

def get_score(game):
    """
    calculate the current board score
    """
    if game.win():
            return 10000
    S = 0
    score_board = make_scoreboard(game)
    for l,ligne in enumerate(game.board):
        for c,disk in enumerate(ligne):
            
            if disk == game.current_player: S+= score_board[l][c]
            elif disk == game.opponent_index: S-= score_board[l][c]
        
    
            
    return S+(get_futures_dif(game))

class omegaZer0AI(TwoPlayerGame):
    """
    implementation of TwoPlayerGame of Othello
    """
    def __init__(self,Players:list,state:dict)-> None: 
        """
        initialization of the game
        """

        #unpack
        self.state = state
        self.players = Players
        self.board = self.make_board(state["board"])
        self.current_player = state["current"]+1
        
        
        


        self.dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        self.done_flag = False
        self.pass_flag = False


        
        
    

    def possible_moves(self,b=False):
        """
        returns a list of all possible moves
        """
        result =[[i,j]
                for i in range(8)
                for j in range(8)
                if (self.board[i][j]==0)
                and(self.legal([i,j],b))]
        
        
        return result

    def legal(self,move:tuple,b:bool):
        """
        checks if a move is allowed
        """
        for dr in self.dirs:
            i = 0
            l=move[0]+(i+1)*dr[0]
            c=move[1]+(i+1)*dr[1]
            
            if not b:
                
                while 0<=l<8 and 0<=c<8:

                    if self.board[l][c] == self.opponent_index:
                    
                        i+=1
                        l=move[0]+(i+1)*dr[0]
                        c=move[1]+(i+1)*dr[1]
                    elif self.board[l][c] == self.current_player and i>0: return True
                    else: 
                        break
                
                    
            else:
                
                while 0<=l<8 and 0<=c<8:
                
                    if self.board[l][c] == self.current_player: 
                        i+=1
                        l=move[0]+(i+1)*dr[0]
                        c=move[1]+(i+1)*dr[1]
                    elif self.board[l][c] == self.opponent_index and i>0: return True
                    else: break
               
            

        return False

    def make_move(self, move:list):
        """
        finds where to put the discs on the board to play the desired move
        """
        to_flip =[move]
        
        for dr in self.dirs:
            i = 0
            l=move[0]+(i+1)*dr[0]
            c=move[1]+(i+1)*dr[1]
            
            while 0<=l<8 and 0<=c<8:
                
                
                if self.board[l][c] == self.opponent_index:
                    to_flip.append((l,c))
                    i+=1
                    l=move[0]+(i+1)*dr[0]
                    c=move[1]+(i+1)*dr[1]
                elif self.board[l][c] ==0:break
                else :to_flip.append((l,c));self.set_disk(to_flip);break

    def set_disk(self,moves:list):
        """
        creates a new board from a board and a move
        """
        for (l,c) in moves:
            
            self.board[l][c] = self.current_player
        
    def is_over(self):
        """
        just a getter to signial the algotritm to stop looking
        """
        return self.done_flag

    def make_board(self,board:list):
        """
        takes two arrays of indexes and convert them into a Matrix 8x8
        """
        
        player,opp = board
        game_board = np.zeros((8,8),dtype=int)
        for c in player + opp:
            if c in player: game_board[c//8,c%8] = 1
            else: game_board[c//8,c%8] = 2
        return game_board
                   
    def count(self):
        """
        conts the difference of disk in each player's possession 
        """
        cnt = 0
        for line in self.board:
                for  piece in line:
                    if piece == self.current_player: cnt +=1
                    elif piece == self.opponent_index : cnt -=1
        return cnt

    def win(self):
        """
        simple win check, if no one can move and i have more points than the other one, I win 
        """
        
        if len(self.possible_moves(self.current_player))==0:
            self.pass_flag = not self.pass_flag
            if len(self.possible_moves(self.opponent_index))==0:
                self.done_flag = not self.done_flag
                return self.count()>0
        return False

    def scoring(self):
        """
        changes the scoring based on the nuber of turns, the position on the board and futur moves avialable 
        """
        return get_score(self)
        


