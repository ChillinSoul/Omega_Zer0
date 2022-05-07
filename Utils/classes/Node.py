
from pydoc import Helper
from sys import maxsize
from functions.helpers import *


brd = []
class node(object):
    """
    Node class:
    the node represents a gamestate,
    it contains a current copy of the game, the current recursion depth (c_depth) and the maximum recurtion depth (m_depth).
    the children attribute contains the possible futur gamestates at the (c_depth +1) depth.
    
    """
    def __init__(self,c_depth:int,m_depth:int,board:list,player:str,val = 0,move = None):

        ######################### Unpack
        self.c_depth = c_depth
        self.m_depth = m_depth
        self.board = board 
        self.player = player

        self.val  = val
        self.move = move
        ######################### Unpack


        ######################### variable init
        self.chlidren = []
        ######################### variable init


        ######################### function(s)
        self.MakeChild()# this line is what creates the entire tree.
        ######################### function(s)
    


    def PGS_eval(self):
        """
        given a specific gamestate, this fuction uses the rules of the game to find all the possible gamestates
        """
        if self.player   == "b" and not self.c_depth%2:
            color = "b"
            opp   = "w"
        elif self.player == "b" and self.cdeph%2:
            color = "w"
            opp   = "b"
        elif self.player == "w" and not self.c_depth%2:
            color = "w"
            opp   = "b"
        else:
            color = "b"
            opp   = "w"

        pgs = []
        for i in range (64):
            if Legal(self.board,i,color,opp):
                pgs.append((Board_update(self.board,i,color,opp),i))
        return pgs
    
    def Score_eval(self):
        """
        given a specific gamestate, this function will return the board score.
        """
        c=[0,7,56,63]
        d=[1,6,8,9,14,15,48,49,54,55,57,62]
        e=[2,3,4,5,16,23,24,31,32,39,40,47,58,59,60,61]
        nb_w   =0
        nb_b   =0
        nb_w_c =0
        nb_b_c =0
        nb_w_e =0
        nb_b_e =0
        nb_w_d =0
        nb_b_d =0

        for i,pos in enumerate(self.board):
            if   i in e and pos == "b": nb_b_e+=1; nb_b +=1
            elif i in e and pos == "w": nb_w_e+=1; nb_w +=1
            elif i in d and pos == "b": nb_b_d+=1; nb_b +=1
            elif i in d and pos == "w": nb_w_d+=1; nb_w +=1
            elif i in c and pos == "b": nb_b_c+=1; nb_b +=1
            elif i in c and pos == "w": nb_w_c+=1; nb_w +=1
            elif pos =="b": nb_b +=1
            elif pos =="w": nb_w +=1
        
        result = (nb_w-nb_b)+(nb_w_c-nb_b_c)*0,5+(nb_w_e-nb_b_e)*0,25+(nb_w_d-nb_b_d)*(-0,5)
        
        if self.player == "w":
            return result
        return -result

    def MakeChild(self):
        """
        this function creates sub-nodes(children) that are derived from the current gamestate using PGS_eval
        """
        if self.c_depth != self.m_depth:
            pgs = self.PGS_eval()
            for gs,mv in pgs:
                # creates a node at depth c_depth+1 whose board is one of the possible gamestates
                self.chlidren.append(node(self.c_depth+1,self.m_depth,gs,self.player,self.val,mv))
