# add player to player dictionary with 0 points, if player already exists return false
def addPlayer(input, players):
    if input in players:
        return False
    else:
        players[input] = 0
        return True
    

# Scoring --------------------------------------------------

# score for a player submitting a flag. Default score is 1.
def submitScore(flag,player,score=1, answers, players):
    print(flag)
    if flag in answers.keys():
        if player in answers[flag]:
            return False
        else:
            answers[flag].append(player)
            players[player] += score
            print(answers)
            print(players)
            return True
    else:
        return False
