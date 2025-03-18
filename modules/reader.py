# read the file and create a list with all answers and hints
def getAnswers():
    with open('answer.txt', 'r') as file:
        ans = file.read()

    list = ans.splitlines()
    res = {}
    # still need a setup for value
    for item in list:
        res.update({item : []})
    print(res)
    return res
# catch errors reading hints file, if theres no hints still runs
def getHints():
    try:
        with open('hints.txt','r') as file:
            hint = file.read()
            temp = hint.splitlines()
            
            return temp
    except:
        print('No Hints this time')
        return None
    return None