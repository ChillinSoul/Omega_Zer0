from sys import maxsize
from unicodedata import name
from Utils.Node import node
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
            if beta<=alpha:    break                    # the best move has been found for the current player 
    
        #print(alpha,beta)
    return [best_move,best_child.move]






#ce que le server te donne
La_liste_du_prof = [[19,27,28,35,36,37,42,45],[18,20,21,34,38,43,44,49,11]]

if (len(La_liste_du_prof[0])+len(La_liste_du_prof[1])) == 4:
    notre_couleur = "b"
else:
    notre_couleur = "w"

La_liste_du_prof_m = [0 for _ in range(64)]
for i in La_liste_du_prof[0]:
    La_liste_du_prof_m[i] = "b"
for j in La_liste_du_prof[1]:
    La_liste_du_prof_m[j] = "w"

point_de_depart_du_jeu = node(0,4,La_liste_du_prof_m,notre_couleur)

#ce que tu donne au server 
la_reponce_de_l_IA = MinMax(point_de_depart_du_jeu)[1]
