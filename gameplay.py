import json
import Utils.functions.helpers as helpers
import Utils.minmax as minmax

import copy


def State(state):
    
   
    return state
    #bestmove=state
    #Meilleur move proposé par IA 
    #...
    #Answer(bestmove)

def Info(message,client):
    vie=message["lives"]
    state=message['state']
    print("Il te reste",vie,"vies")
    if "move" in message:
        print(message,"ok")
    
    State(state)
    bestmove=minmax.MinMax()
    print("yes",bestmove)
    
    input('Chose:move or give up')
    
    answer=str(input())
    if answer =='move':
            move_answ=json.dumps({
                "response": "move",
                "move":bestmove,
                "message": "Mouahah"})
            client.send(move_answ.encode())
            
            
        
    if answer=="give up":
            giveup=json.dumps({
            "response": "giveup",
                })
            client.send(giveup.encode())
           
    else:
            input('Try again:move or give up')

        
            





