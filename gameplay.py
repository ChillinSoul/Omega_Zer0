import json
def Choices(state):
    print(state)
    #bestmove=state
    #Meilleur move proposé par IA 
    #...
    #Answer(bestmove)

def state(message):
    vie=message["lives"]
    print("Il te reste",vie,"vies")
    state=message["state"]
    
    Choices(state)

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
            break
        
        if answer=="give up":
            giveup=json.dumps({
            "response": "giveup",
                })
            client.send(giveup.encode())
            break
        else:
            input('Try again:move or give up')

        
            


