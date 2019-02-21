UserScore = input('What is the score:')
try:
    UserScore = float(UserScore)
    #print('That is a number')
except:
    print('Thats not a valid number silly')
    print('Exiting now')
    quit()
if UserScore < 0:
    print('Scores cannot be less than 0')
    print('Exiting now')
    quit()
elif UserScore > 1:
    print('Scores cannot be greater than 0')
    print('Exiting now')
    quit()
elif UserScore >= .9:
    print('A')
elif UserScore >= .8:
    print('B')
elif UserScore >= .7:
    print('C')
elif UserScore >= .6:
    print('D')
elif UserScore < .6:
    print('F')
