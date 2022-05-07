from sys import maxsize
from classes import Node


def MinMax(node:Node,c_depth:int,m_depth:int):
    if (c_depth == m_depth) or (abs(node.val)==maxsize): return node.val
    
    best_move = maxsize*(-1)**(c_depth%2+1)
    

    for child in node.chlidren:
        value = MinMax(child,c_depth+1,m_depth)[0]
        if (abs(maxsize*(-1)**(c_depth%2+2)-value)<abs(maxsize*(-1)**(c_depth%2+2)-best_move)):
            best_move = value 
    
    
    return (best_move,child)