import json
import Utils.functions.helpers as helpers
import Utils.minmax as minmax
from Utils.Node import node as node

import copy

player=""
t=0
def Info(message,client):
   

    global player
    global t
    
    print('player:',player)
    
    vie=message["lives"]
    state=message['state']
    print("Il te reste",vie,"vies")
    
    
    boardinfo= message['state']['board']
    print('board:',boardinfo)

    print('Chose:move or give up:')

    
    #answer=input()
   
    list_b=boardinfo[0]
    list_w=boardinfo[1]
    if True:
        if t<1:
            
            if len(boardinfo[0]+boardinfo[1])==4:
                player='b'
   
                lst = [0 for _ in range(64)]
                for i in list_b:
                    lst[i] = "b"
                for j in list_w:
                    lst[j] = "w"
                boardpawns=[boardinfo[0]+boardinfo[1]]
                bob = node(0,4,lst,player)
                object,bestmove=minmax.MinMax(bob)
                print('bestmove:',bestmove)
                
                move_answ=json.dumps({
                    "response": "move",
                    "move":bestmove,
                    "message": "Mouahah"})
                client.send(move_answ.encode())
                t=1
                return t,player
            else:
                player ='w'
                lst = [0 for _ in range(64)]
                for i in list_b:
                    lst[i] = "b"
                for j in list_w:
                    lst[j] = "w"
                
                boardpawns=[boardinfo[0]+boardinfo[1]]
                bob = node(0,4,lst,player)
                object1,bestmove=minmax.MinMax(bob)
                print(bestmove)
                move_answ=json.dumps({
                    "response": "move",
                    "move":bestmove,
                    "message": "Mouahah"})
                client.send(move_answ.encode())
                t=1
                return t,player
                

        if t>=1:
                print(player)
               
                lst = [0 for _ in range(64)]
                for i in list_b:
                    lst[i] = "b"
                for j in list_w:
                    lst[j] = "w"
                bob = node(0,4,lst,player)
                object, bestmove=minmax.MinMax(bob)
                print('bestmove:',bestmove)
                print('object:',object)
                move_answ=json.dumps({
                    "response": "move",
                    "move":bestmove,
                    "message": "Mouahah"})

                client.send(move_answ.encode())
                return
                


            
        
    if answer=="give up" or answer=="g":
            giveup=json.dumps({
            "response": "giveup",
                })
            client.send(giveup.encode())
            return
            
           
    if answer!="g" or answer!="m":
            print('Try again:')
            return





        

