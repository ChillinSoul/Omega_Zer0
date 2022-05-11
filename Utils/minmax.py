from sys import maxsize
from Utils.Node import node

def MinMax(node:node,alpha = - maxsize,beta = maxsize):
    best_move = maxsize*(-1)**(node.c_depth%2+1)
    best_child = node
    
    if (node.c_depth == node.m_depth):
        
        return node.Score_eval(),node.move 
    
    

    for child in node.chlidren:
        value,_ = MinMax(child,alpha,beta)
        
        if (abs(maxsize*(-1)**(child.c_depth%2+1)-value)<abs(maxsize*(-1)**(child.c_depth%2+1)-best_move)):
            
            best_move,best_child = value,child 
            


            if node.c_depth%2: beta  = min(beta, value) # node.c_depth%2 is not 0 when the minimizing player is playing
            else :             alpha = max(alpha,value) # the maximizer playe is playing
            if beta<=alpha:    break                    # the best move has been found for the current player 
    
        #print(alpha,beta)
    return [best_move,best_child.move]

