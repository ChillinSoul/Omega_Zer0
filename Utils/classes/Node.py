
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
        if self.player == "b" and not self.c_depth%2:
            color = "b"
        elif self.player == "b" and self.cdeph%2:
            color ="w"
        elif self.player == "w" and not self.c_depth%2:
            color ="w"
        else:
            color = "b"

        pgs = []
        for i in range (64):
            if Legal(self.board,i,color):
                pgs.append((Board_update(self.board,i,color),i))
        return pgs
    
    def Score_eval(self):
        """
        given a specific gamestate, this function will return the board score.
        """
        #(nb_w-nb_b)+(nb_w_c-nb_b_c)*0,5+(nb_w_e-nb_b_e)*0,25+(nb_w_d-nb_b_d)*(-0,5) si on et blanc, l'inverse si on est noir
        return 1

    def MakeChild(self):
        """
        this function creates sub-nodes(children) that are derived from the current gamestate using PGS_eval
        """
        if self.c_depth != self.m_depth:
            pgs = self.PGS_eval()
            for gs,mv in pgs:
                # creates a node at depth c_depth+1 whose board is one of the possible gamestates
                self.chlidren.append(node(self.c_depth+1,self.m_depth,gs,self.player,self.val,mv))
