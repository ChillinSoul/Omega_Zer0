import json
import Utils.functions.helpers as helpers
import Utils.minmax as minmax
from Utils.Node import node as node

import copy

player =""
c=0
def Info(message,client):
    vie=message["lives"]
    state=message['state']
    print("Il te reste",vie,"vies")
    if "move" in message:
        print(message,"ok")

    input('Chose:move or give up')
    
    answer=str(input())
    if answer =='move' or answer== 'm':
        while c<1:
            boardinfo= message['state']['state'[3]]
            if len(boardinfo[0]+boardinfo[1])==4:
                player='b'
                list_b=boardinfo[0]
                opp='w'
                list_w=boardinfo[1]
                lst = [0 for _ in range(64)]
                for i in list_b:
                    lst[i] = "b"
                for j in list_w:
                    lst[j] = "w"
                
                boardpawns=[boardinfo[0]+boardinfo[1]]
                bestmove=minmax.MinMax(bob)
                move_answ=json.dumps({
                    "response": "move",
                    "move":bestmove,
                    "message": "Mouahah"})
                client.send(move_answ.encode())
                c=1
                break
            if len(boardinfo[0]+boardinfo[1])==5:
                if len(boardinfo[0])==3:
                    player='w'
                    list_w=boardinfo[1]
                    opp='b'
                    list_b=boardinfo[0]
                if len(boardinfo[1]==3):
                    player='w'
                    list_w=boardinfo[0]
                    opp='b'
                    list_b=boardinfo[1]
                    lst = [0 for _ in range(64)]
                for i in list_b:
                    lst[i] = "b"
                for j in list_w:
                    lst[j] = "w"
                bob = node(0,4,lst,"w")
                boardpawns=[boardinfo[0]+boardinfo[1]]
                bestmove=minmax.MinMax(bob)
                move_answ=json.dumps({
                    "response": "move",
                    "move":bestmove,
                    "message": "Mouahah"})
                client.send(move_answ.encode())
                c=1
                break

            boardinfo= message['state']['state'[3]]

            list_b=[19,27,28,35,36,37,42,45]
            list_w=[18,20,21,34,38,43,44,49,11]
            lst = [0 for _ in range(64)]
            for i in list_b:
                lst[i] = "b"
            for j in list_w:
                lst[j] = "w"
            bob = node(0,4,lst,"w")
            
            print(len(bob.chlidren))
            print(minmax.MinMax(bob))
            

            boardpawns=[boardinfo[0]+boardinfo[1]]
            bestmove=minmax.MinMax(bob)
            move_answ=json.dumps({
                    "response": "move",
                    "move":bestmove,
                    "message": "Mouahah"})
            client.send(move_answ.encode())
        
        
    if answer=="give up" or answer=="g":
            giveup=json.dumps({
            "response": "giveup",
                })
            client.send(giveup.encode())
           
    else:
            input('Try again:move or give up')

        
            





