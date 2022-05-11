
from sys import maxsize
from time import time
from Utils.functions.helpers import *




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
        self.color = "b"
        self.opp   = "w"
        self.chlidren = []
        self.pgs=[]
        ######################### variable init


        ######################### function(s)
        self.MakeChild()# this line is what creates the entire tree.
        ######################### function(s)
    


    def PGS_eval(self,i):
        """
        given a specific gamestate, this fuction uses the rules of the game to find all the possible gamestates
        """
        
        if Legal(self.board,i,self.color,self.opp):
            if self.c_depth != self.m_depth:
                self.pgs.append((Board_update(self.board,i,self.color,self.opp),i))
            
            
        
    
    def Score_eval(self):
        """
        given a specific gamestate, this function will return the board score.
        """
        c=[0,7,56,63]
        d=[1,6,8,9,14,15,48,49,54,55,57,62]
        e=[2,3,4,5,16,23,24,31,32,39,40,47,58,59,60,61]
        nb_w   =0
        nb_b   =0

        for i,pos in enumerate(self.board):
            if   i in e and pos == "b": nb_b +=4
            elif i in e and pos == "w": nb_w +=4
            elif i in d and pos == "b": nb_b +=2
            elif i in d and pos == "w": nb_w +=2
            elif i in c and pos == "b": nb_b +=9
            elif i in c and pos == "w": nb_w +=9
            elif pos =="b": nb_b +=1
            elif pos =="w": nb_w +=1
        
        result = (nb_w-nb_b)
        
        if self.player == "w":
            return result
        return -result

    def MakeChild(self):
        """
        this function creates sub-nodes(children) that are derived from the current gamestate using PGS_eval
        """
        if self.player   == "b" and not self.c_depth%2:
            self.color = "b"
            self.opp   = "w"
        elif self.player == "b" and self.c_depth%2:
            self.color = "w"
            self.opp   = "b"
        elif self.player == "w" and not self.c_depth%2:
            self.color = "w"
            self.opp   = "b"
        else:
            self.color = "b"
            self.opp   = "w"

        if self.c_depth < self.m_depth:
            for i in range(64):
                self.PGS_eval(i)
            for gs,mv in self.pgs:
                # creates a node at depth c_depth+1 whose board is one of the possible gamestates
                self.chlidren.append(node(self.c_depth+1,self.m_depth,gs,self.player,self.val,mv))
    

