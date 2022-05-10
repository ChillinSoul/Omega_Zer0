from sys import maxsize
from Node import node
from time import time

def MinMax(node:node,alpha = - maxsize,beta = maxsize):

    if (node.c_depth == node.m_depth) or (abs(node.val)==maxsize): return node.Score_eval(),node.move 
    
    best_move = maxsize*(-1)**(node.c_depth%2+1)
    best_child = None

    for child in node.chlidren:
        value,_ = MinMax(child,alpha,beta)
        if (abs(maxsize*(-1)**(node.c_depth%2+2)-value)<abs(maxsize*(-1)**(node.c_depth%2+2)-best_move)):
            best_move,best_child = value,child 
            

            if node.c_depth%2: beta  = min(beta, value) # node.c_depth%2 is not 0 when the minimizing player is playing
            else :             alpha = max(alpha,value) # the maximizer playe is playing
            if beta<=alpha:    break                       # the best move has been found for the current player 
    
    
    return [best_move,best_child.move]

start = time()
list_b=[28,35]
list_w=[27,36]
lst = [0 for _ in range(64)]
for i in list_b:
    lst[i] = "b"
for j in list_w:
    lst[j] = "w"
bob = node(0,4,lst,"w")
print(time()-start)
print(len(bob.chlidren))
print(MinMax(bob))