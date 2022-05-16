import numpy as np
from easyAI import Negamax, TwoPlayerGame,AI_Player
from time import time
from random import randint 
from copy import deepcopy


class omegaZer0AI(TwoPlayerGame):
    """
    
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


        #weird experimental strategy 
        self.chicken_diner=[
            [9, 4, 4, 4, 4, 4, 2, 9],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [4, 1, 1, 1, 1, 1, 1, 4],
            [2, 1, 1, 1, 1, 1, 1, 2],
            [9, 2, 4, 4, 4, 4, 4, 9]
        ]
        self.chicken_lunch=[
            [9, 4, 4, 4, 4, 4, 2, 9],
            [2, 0, 1, 1, 1, 1, 0, 2],
            [4, 1, 2, 2, 2, 2, 1, 4],
            [4, 1, 2, 3, 3, 2, 1, 4],
            [4, 1, 2, 3, 3, 2, 1, 4],
            [4, 1, 2, 2, 2, 2, 1, 4],
            [2, 0, 1, 1, 1, 1, 0, 2],
            [9, 2, 4, 4, 4, 4, 4, 9]
        ]
        self.chicken_starter=[
            [9, 4, 4, 4, 4, 4, 2, 9],
            [2, -1, 2, 1, 1, 1, -1, 2],
            [4, 2, 2, 1, 1, 1, 1, 4],
            [4, 1, 1, 5, 5, 1, 1, 4],
            [4, 1, 1, 5, 5, 1, 1, 4],
            [4, 2, 2, 1, 1, 2, 2, 4],
            [2, -1, 2, 1, 1, 2, -1, 2],
            [9, 2, 4, 4, 4, 4, 4, 9]
        ]
        
    

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
                    elif self.board[l][c] == self.current_player and i>0:
                        
                        return True
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
                    else : cnt -=1
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
        if self.win():
            return 10000
        S = 0
        game_stage = np.sum(self.board ==0)
        if game_stage > 48:
            for l,ligne in enumerate(self.board):
                for c,disk in enumerate(ligne):
                    
                    if disk == self.current_player: S+= self.chicken_starter[l][c]
                    elif disk == self.opponent_index: S-= self.chicken_starter[l][c]
            S+=(len(self.possible_moves())-len(self.possible_moves(True)))*2
        elif game_stage > 32:
            for l,ligne in enumerate(self.board):
                for c,disk in enumerate(ligne):
                    
                    if disk == self.current_player: S+= self.chicken_lunch[l][c]
                    elif disk == self.opponent_index: S-= self.chicken_lunch[l][c]
            S+=(len(self.possible_moves())-len(self.possible_moves(True)))
        elif game_stage > 160:
            for l,ligne in enumerate(self.board):
                for c,disk in enumerate(ligne):
                    
                    if disk == self.current_player: S+= self.chicken_lunch[l][c]
                    elif disk == self.opponent_index: S-= self.chicken_lunch[l][c]
             
        else:
            for l,ligne in enumerate(self.board):
                for c,disk in enumerate(ligne):
                    
                    if disk == self.current_player: S+= self.chicken_diner[l][c]
                    elif disk == self.opponent_index: S-= self.chicken_diner[l][c]
        #print("potential score: {}".format(S))
        return S

if __name__ =="__main__":
    #don't have much time for fancy unit test when you decide to start over the night before
    state = {'players': ['OmegaZero', 'OmegaZero1'], 'current': 0, 'board': [[28, 35], [27, 36]]}
    AI = omegaZer0AI([AI_Player(Negamax(4)),AI_Player(Negamax(4))],state)
    bestmove=AI.get_move()