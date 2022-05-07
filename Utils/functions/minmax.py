from sys import maxsize
from classes.Node import node


def MinMax(node:node,alpha = - maxsize,beta = maxsize):

    if (node.c_depth == node.m_depth) or (abs(node.val)==maxsize): return node.Score_eval(),node.move 
    
    best_move = maxsize*(-1)**(node.c_depth%2+1)
    

    for child in node.chlidren:
        value = MinMax(child,child.c_depth,child.m_depth,alpha,beta)[0]
        if (abs(maxsize*(-1)**(node.c_depth%2+2)-value)<abs(maxsize*(-1)**(node.c_depth%2+2)-best_move)):
            best_move,_ = value 

            if node.c_depth%2: beta  = min(beta, value) # node.c_depth%2 is not 0 when the minimizing player is playing
            else :             alpha = max(alpha,value) # the maximizer playe is playing
            if beta<=alpha:    break                    # the best move has been found for the current player 
    
    
    return (best_move,child.move)