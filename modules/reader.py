# read the file and create a list with all answers and hints
def getAnswers():
    with open('../answer.txt', 'r') as file:
        ans = file.read()

    

    return ans.splitlines()
# catch errors reading hints file, if theres no hints still runs
def getHints():
    hints = None
    try:
        with open('../hints.txt','r') as file:
            hint = file.read()
            hints = hint.splitlines()
    except:
        print('No Hints this time')
    
    return hints
# with split answer key add to a answer array until you get to the hint array
