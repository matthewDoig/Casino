import random
cards = [1,2,3,4,5,6,7,8,9,10]
def Deal(cards):
    card = random.choices(cards, weights = [4/52, 4/52, 4/52, 4/52, 4/52, 4/52, 4/52, 4/52, 4/52, 16/52], k = 1)
    return(card)

def userscore(score, current):
    for x in range(0,len(score)):
        if score[x] == 1 and current + score[x] < 21:
            score[x] = int(input("1 or 11"))
        elif score[x] == 1 and current + score[x] > 21:
            score[x] = 1
        current = current + score[x]
    return(current)

def cpuscore(score, current):
    for x in range(0,len(score)):
        if score[x] == 1 and current + 11 < 21:
            score[x] = 11
        current = current + score[x]
    return(current)

def decision():
    if input("Hit or Stand") == "Hit":
        Hit = True
    else:
        Hit = False
    return Hit

def checkscore(playerscore, player2score):
    winner = False
    if player2score == 21 and playerscore == 21:
        print("Draw")
        winner = True
    elif playerscore == 21:
        print("Player 1 Wins!")
        winner = True
    elif player2score == 21:
        print("Player 2 Wins")
        winner = True
    elif playerscore > 21:
        print("Player 2 Wins!")
        winner = True
    elif player2score > 21:
        print("Player 1 Wins!")
        winner = True
    return(winner)

def finalscore(playerscore, player2score):
    winner = False
    if player2score > playerscore:
        print("Player 2 Wins")

player = Deal(cards) + Deal(cards)
playerscore = userscore(player, 0)
print("User Score = " + str(playerscore))
cpu = Deal(cards)
player2score = cpuscore(cpu, 0)
print("CPU Score = " + str(player2score))

if checkscore(playerscore, player2score) == True:
    exit()
Hit = True
while Hit == True:
    if decision() == True:
        Hit = True
        player = Deal(cards)
        playerscore = userscore(player, playerscore)
        print("Player 1 = " + str(playerscore))
        if checkscore(playerscore, player2score) == True:
            exit()
    else:
        Hit = False

while player2score < playerscore:
    cpu = Deal(cards)
    player2score = cpuscore(cpu, player2score)
    print("Player 2 = " + str(player2score))
    if checkscore(playerscore, player2score) == True:
        exit()
    if finalscore(playerscore, player2score) == True:
        exit()