def Choices(state):
    #bestmob
    #Meilleur move proposé par IA 
    pass

def state(message):
    vie=message["lives"]
    print("Il te reste",vie,"vies")
    state=message["state"]
    print(state)
    Choices(state)
