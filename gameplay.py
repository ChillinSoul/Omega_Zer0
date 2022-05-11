import json
import Utils.functions.helpers as helpers
import Utils.minmax as minmax
from Utils.Node import node as node

import copy


def Info(message,client):
    player =""
    t=0
    print(t)
    print(client)
    vie=message["lives"]
    state=message['state']
    print("Il te reste",vie,"vies")
    
    
    boardinfo= message['state']['board']
    print('board:',boardinfo)

    print('Chose:move or give up')

    
    answer=input()
    print(answer)
    if answer =='move' or answer== 'm':
        if t<1:
            
            if len(boardinfo[0]+boardinfo[1])==4:
                player='b'
                list_b=boardinfo[0]
                print('b:',list_b)
                opp='w'
                list_w=boardinfo[1]
                print('w:',list_w)
                
                lst = [0 for _ in range(64)]
                for i in list_b:
                    lst[i] = "b"
                for j in list_w:
                    lst[j] = "w"
                
                boardpawns=[boardinfo[0]+boardinfo[1]]
                bob = node(0,4,lst,"b")
                object1,bestmove=minmax.MinMax(bob)
                print(bestmove)
                move_answ=json.dumps({
                    "response": "move",
                    "move":bestmove,
                    "message": "Mouahah"})
                client.send(move_answ.encode())
                t=1
                return t,player
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
                bob = node(0,4,lst,player)
                boardpawns=[boardinfo[0]+boardinfo[1]]
                
                bestmove=minmax.MinMax(bob)
                move_answ=json.dumps({
                    "response": "move",
                    "move":bestmove,
                    "message": "Mouahah"})
                client.send(move_answ.encode())
                t=1
                return t,player

            
        
    if answer=="give up" or answer=="g":
            giveup=json.dumps({
            "response": "giveup",
                })
            client.send(giveup.encode())
           
    if answer!="g" or answer!="m":
            print('Try again:')

        
            





