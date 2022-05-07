from sys import maxsize

class node(object):
    """
    Node class:
    the node represents a gamestate,
    it contains a current copy of the game, the current recursion depth (c_depth) and the maximum recurtion depth (m_depth).
    the children attribute contains the possible futur gamestates at the (c_depth +1) depth.
    
    """
    def __init__(self,c_depth:int,m_depth:int,board:list,val = 0,move = None):

        ######################### Unpack
        self.c_depth = c_depth
        self.m_depth = m_depth
        self.board = board 

        self.val  = val
        self.move = move
        ######################### Unpack


        ######################### variable init
        self.chlidren = []
        ######################### variable init


        ######################### function(s)
        self.MakeChild()# this line is what creates the entire tree.
        ######################### function(s)
    

    def Legal(self):
        """
        given a specific gamestate and a move, this function will return T/F depending if the move is legal.
        """
    def PGS_eval(self):
        """
        given a specific gamestate, this fuction uses the rules of the game to find all the possible gamestates
        """
        return True
        pgs=[]
        return pgs
    
    def Score_eval(self):
        """
        given a specific gamestate, this function will return the board score.
        """
        return 1


    def MakeChild(self):
        """
        this function creates sub-nodes(children) that are derived from the current gamestate using PGS_eval
        """
        if self.c_depth != self.m_depth:
            pgs = self.PGS_eval()
            for gs in pgs:
                # creates a node at depth c_depth+1 whose board is one of the possible gamestates
                self.chlidren.append(node(self.c_depth+1,self.m_depth,gs,self.val,self.move))
