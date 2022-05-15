import json

import Utils.helpers as helpers
import Utils.minmax as minmax
from Utils.Node import node as node


def Info(message,client):
    state= message['state']
    
    
    boardinfo= message['state']['board']
    if state['current'] == 1:
        player= "w"
    else:
        player = "b"

    
   



    
    
    



    lst = [0 for _ in range(64)]

    for i in boardinfo[0]:
        lst[i] = "b"
    for j in boardinfo[1]:
        lst[j] = "w"
    
    AI = node(0,4,lst,player)
    object,bestmove=minmax.MinMax(AI)

    if bestmove == None:
        t=0
        giveup=json.dumps({
        "response": "giveup",
        })
        client.send(giveup.encode())
    else: 

        move_answ=json.dumps({
        "response": "move",
        "move":bestmove,
        "message": "Mouahah"})
        client.send(move_answ.encode())
    









        

