import json


#import Utils.helpers as helpers
#import Utils.minmax as minmax
#from Utils.Node import node
from Utils.NodeAI import omegaZer0AI
from easyAI import Negamax,AI_Player


def Info(message,client):
    state= message['state']
    print(state)
    
    #------------------------------------minimax-node
    # state= message['state']
    # boardinfo= message['state']['board']
    # if state['current'] == 1:
    #     player= "w"
    # else:
    #     player = "b"
    # lst = [0 for _ in range(64)]
    # for i in boardinfo[0]:
    #     lst[i] = "b"
    # for j in boardinfo[1]:
    #     lst[j] = "w"
    # AI = node(0,4,lst,player)
    # object,bestmove=minmax.MinMax(AI)

    # if bestmove == None:
    #     t=0
    #     giveup=json.dumps({
    #     "response": "giveup",
    #     })
    #     client.send(giveup.encode())
    # else: 
    #     move_answ=json.dumps({
    #     "response": "move",
    #     "move":bestmove,
    #     "message": "Mouahah"})
    #     client.send(move_answ.encode())


    bestmove=None
    #------------------------------------negamax-NodeAI
    try:
        AI = omegaZer0AI([AI_Player(Negamax(4)),AI_Player(Negamax(4))],state)
        print(1)
        bestmove=AI.get_move()
        bestmove = bestmove[0]*8+bestmove[1]
        print(bestmove)
        

        bestmove=AI.get_move()
        bestmove = bestmove[0]*8+bestmove[1]
    except IndexError: #here to catch ne no moves left bug
        pass

        #hailmary
    if bestmove == None:
        try:

                AI = omegaZer0AI([AI_Player(Negamax(1)),AI_Player(Negamax(1))],state)
                bestmove=AI.get_move()
                bestmove = bestmove[0]*8+bestmove[1]

        
        
        except:
            giveup=json.dumps({
            "response": "giveup",
            })
            client.send(giveup.encode())
            pass   
    
    print(bestmove)
    move_answ=json.dumps({
    "response": "move",
    "move":bestmove,
    "message": "Mouahah"})
    client.send(move_answ.encode())
    

            


    
   








        

