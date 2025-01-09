# read the file and create a list with all answers and hints
def getAnswers():
    with open('answer.txt', 'r') as file:
        ans = file.read()

    list = ans.splitlines()
    res = {}
    # still need a setup for value
    for item in list:
        res.update({item : []})
    return res
# catch errors reading hints file, if theres no hints still runs
def getHints():
    hints = {}
    try:
        with open('../hints.txt','r') as file:
            hint = file.read()
            temp = hint.splitlines()
            for item in temp:
                # hints will be checked whether they are true or false. if they are true it will send the hint otherwise it will sent a blank spot where 
                # the user will see a hint could be
                hints.update({item : False})
    except:
        print('No Hints this time')
        return None
