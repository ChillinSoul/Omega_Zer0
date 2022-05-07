from sys import maxsize
from classes.Node import node


def MinMax(node:node,alpha,beta):

    if (node.c_depth == node.m_depth) or (abs(node.val)==maxsize): return node.val
    
    best_move = maxsize*(-1)**(node.c_depth%2+1)
    

    for child in node.chlidren:
        value = MinMax(child,child.c_depth,child.m_depth)[0]
        if (abs(maxsize*(-1)**(node.c_depth%2+2)-value)<abs(maxsize*(-1)**(node.c_depth%2+2)-best_move)):
            best_move = value 
    
    
    return (best_move,child)