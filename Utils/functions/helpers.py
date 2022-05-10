
from copy import deepcopy


t = -8
r = +1
d = +8
l = -1
tl = t+l
dl = d+l
dr = d+r
tr = t+r

directions = [t,r,d,l,tl,dl,dr,tr]



def inbound(move:int, dir:int):
    
    if 0<=move+dir and move+dir <64:
        if   move%8 == 0 and (dir ==-1 or dir ==-9 or dir ==  7):
            return False
        elif move%8 == 7 and (dir == 1 or dir == 9 or dir == -7):
            return False
        else: 
            return True
    return False

def Board_update(board:list,move:int,player:str,opp:str):
    """
    updates the board for a given move
    """

    n_board = deepcopy(board)
    for dir in directions:
            i =1
            temp=[]
            while inbound(move,dir*(i)):
                if board[move+dir*(i)] == opp:
                    temp.append(move+dir*(i))
                    i+=1
                elif board[move+dir*(i)] == player and i>1:
                    for disc in temp:
                        n_board[disc] = player
                    break
                else:
                    break
    return n_board


def Legal(board:list,move:int,player:str,opp:str):
    """
    given a specific gamestate and a move, this function will return T/F depending if the move is legal.
    """
    
    if board[move] == 0 or board[move] == "":
        for dir in directions:
            
            i =1
            while inbound(move,dir*(i)):
                
                if board[move+dir*(i)] == opp:
                    i+=1
                elif board[move+dir*(i)] == player and i>1:
                    
                    return True
                else:
                    
                    break
    return False




if __name__ == '__main__':
	print(inbound(4,-2))
    

