# read the file and create a list with all answers and hints

with open('answer.txt', 'r') as file:
    ans = file.read()

try:
    with open('hint.txt','r') as file:
        hint = file.read()
        hints = hint.splitlines()
    # print(hints)
except:
    print('No Hints this time')


answers = ans.splitlines()

# with split answer key add to a answer array until you get to the hint array
