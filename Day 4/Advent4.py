lines = [i.replace("\n", "") for i in open("input4.txt", "r")]

numsdrawn = lines.pop(0).split(",") # get the numbers lines.pop(0)

boards = []
nboard = []
for i in range(len(lines)): #pair every number with a 0
    nboard.append([[0, int(lines[i][j:j+2])] for j in range(0, len(lines[i]), 3)]) if len(lines[i]) != 0 else None
    if i == len(lines) - 1 or len(lines[i]) == 0:
        boards.append(nboard)
        nboard = []

def searchBingo():
    winners = []
    won = []
    for num in numsdrawn:
        for i in range(len(boards)): # boards
            for j in boards[i]: # rows
                if i in won:
                    continue
                isWon = [False, 0]
    
                for k in j: # colums
                    if k[1] == int(num):
                        k[0] = 1 #mark number
    
                if sum([a[0] for a in j]) == len(j): #check row for win
                    isWon = [True, num]
                else: #check colum for win
                    for a in range(5):
                        col = []
                        for k in boards[i]:
                            col.append(k[a])
                        
                        if sum([a[0] for a in col]) == len(j):
                            isWon = [True, num]
    
                if isWon[0] == True:
                    winners.append([boards[i], int(isWon[1])])
                    won.append(i)

    return winners

wintables = searchBingo()
firstwon = wintables[0]
lastwon = wintables[-1]
part1=firstwon[1] * sum(sum(a[1] if a[0] == 0 else 0 for a in i) for i in firstwon[0])
part2=lastwon[1] * sum(sum(a[1] if a[0] == 0 else 0 for a in i) for i in lastwon[0])
print("part 1: ", part1 )
print("part 2: ", part2 )