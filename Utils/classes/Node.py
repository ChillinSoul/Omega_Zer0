from sys import maxsize

class Node(object):
    """
    Node class:
    the node represents a gamestate,
    it contains a current copy of the game, the current recusion depth (c_depth) and the maximum recurtion depth (m_depth).
    the children attribute contains the possible futur gamestates at the c_depth +1 depth.
    alpha and beta are arguments for the alpha-beta prunig alorithm that layers on to of minimax.
    
    """
    def __init__(self,c_depth:int,m_depth:int,board:list,val = 0,alpha = maxsize,beta = -maxsize):

        ######################### Unpack
        self.c_depth = c_depth
        self.m_depth = m_depth
        self.board = board

        self.apha = alpha
        self.beta = beta 

        self.val  = val
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
        pgs=[]
        return pgs


    def MakeChild(self):
        """
        this function creates sub-nodes(children) that are derived from the current gamestate using PGS_eval
        """
        if self.c_depth != self.m_depth:
            pgs = self.PGS_eval()
            for gs in pgs:
                # creates a node at depth c_depth+1 whose board is one of the possible gamestates
                self.chlidren.append(Node(self.c_depth+1,self.m_depth,gs,self.val,self.alpha,self.beta))
