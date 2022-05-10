import json
import Utils.functions.helpers as helpers
import Utils.minmax as minmax

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
                boardpawns=[boardinfo[0]+boardinfo[1]]
                bestmove=minmax.MinMax(boardpawns,player)
                move_answ=json.dumps({
                    "response": "move",
                    "move":bestmove,
                    "message": "Mouahah"})
                client.send(move_answ.encode())
                c=1
                break
            if len(boardinfo[0]+boardinfo[1])==5:
                player='w'
                boardpawns=[boardinfo[0]+boardinfo[1]]
                bestmove=minmax.MinMax(boardpawns,player)
                move_answ=json.dumps({
                    "response": "move",
                    "move":bestmove,
                    "message": "Mouahah"})
                client.send(move_answ.encode())
                c=1
                break

            boardinfo= message['state']['state'[3]]
            boardpawns=[boardinfo[0]+boardinfo[1]]
            bestmove=minmax.MinMax(boardpawns,player)
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

        
            





