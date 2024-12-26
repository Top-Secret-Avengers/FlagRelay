# add player to player dictionary, if player already exists return false
def addPlayer(input, dict):
    if input in dict:
        return False
    else:
        dict[input] = 0
        return True