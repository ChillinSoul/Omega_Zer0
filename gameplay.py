import json
import helpers

import copy


def State(state):
    print("ETAT2", state)
    helpers.Score_eval( state)
    return state
    #bestmove=state
    #Meilleur move proposé par IA 
    #...
    #Answer(bestmove)

def Info(message):
    vie=message["lives"]
    state=message['state']
    print("Il te reste",vie,"vies")
    
    State(state)
    

def Answer(bestmove,client):
    input('Chose:move or give up')
    while True:
        answer=str(input())
        if answer =='move':
            move_answ=json.dumps({
                "response": "move",
                "move": bestmove,
                "message": "Mouahah"})
            client.send(move_answ.encode())
            newState = copy.deepcopy(state)
            break
        
        if answer=="give up":
            giveup=json.dumps({
            "response": "giveup",
                })
            client.send(giveup.encode())
            break
        else:
            input('Try again:move or give up')

        
            





