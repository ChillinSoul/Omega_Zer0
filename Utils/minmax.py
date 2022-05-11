from sys import maxsize
from Node import node
from time import time

def MinMax(node:node,alpha = - maxsize,beta = maxsize):
    best_move = maxsize*(-1)**(node.c_depth%2+1)
    best_child = node
    
    if (node.c_depth == node.m_depth) or (abs(node.val)==maxsize):
        #print(node.Score_eval())
        return node.Score_eval(),node.move 
    
    

    for child in node.chlidren:
        value,_ = MinMax(child,alpha,beta)
        
        if (abs(maxsize*(-1)**(child.c_depth%2+1)-value)<abs(maxsize*(-1)**(child.c_depth%2+1)-best_move)):
            
            best_move,best_child = value,child 
            


            if node.c_depth%2: beta  = min(beta, value) # node.c_depth%2 is not 0 when the minimizing player is playing
            else :             alpha = max(alpha,value) # the maximizer playe is playing
            if beta<=alpha:    print("");break                    # the best move has been found for the current player 
    
        #print(alpha,beta)
    return [best_move,best_child.move]

start = time()
list_b=[19,27,28,35,36,37,42,45]
list_w=[18,20,21,34,38,43,44,49,11]
lst = [0 for _ in range(64)]
for i in list_b:
    lst[i] = "b"
for j in list_w:
    lst[j] = "w"
bob = node(0,4,lst,"w")
print(time()-start)
print(len(bob.chlidren))
print(MinMax(bob))
print(time()-start)