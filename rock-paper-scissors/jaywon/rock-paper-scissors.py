def score(res):
    opp = res[0:1]
    me = res[2:3]
    #A=Rock, B=Paper, C=Scissors;
    #X=Rock, Y=Paper, Z=Scissors;

    if opp=='A' and me=='X':
        return 1+3
    elif opp=='A' and me=='Y':
        return 2+6
    elif opp=='A' and me=='Z':
        return 3+0
    elif opp=='B' and me=='X':
        return 1+0
    elif opp=='B' and me=='Y':
        return 2+3
    elif opp=='B' and me=='Z':
        return 3+6
    elif opp=='C' and me=='X':
        return 1+6
    elif opp=='C' and me=='Y':
        return 2+0
    else:
        return 3+3

file = open('/Users/JayWon1/Desktop/CSE437Repos/puzzles/rock-paper-scissors/jaywon/input.txt', 'r')

lines = file.readlines()
#print(lines)

sum = 0

for i in lines:
    sum += score(i)

print("Score is: " + str(sum))