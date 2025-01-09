# add player to player dictionary, if player already exists return false
def addPlayer(input, players):
    if input in players:
        return False
    else:
        players[input] = 0
        return True
    
