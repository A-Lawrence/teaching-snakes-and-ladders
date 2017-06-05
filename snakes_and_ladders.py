# Version 2
# This version builds on the last:
# - makes a player move back the number of positions rolled if a double

import random

players = { 1 : 1, 2 : 1 }
turn = 1

def rollDice():
    return (random.randint(1, 6), random.randint(1, 6))

def isDouble(roll):
    return roll[0] == roll[1]

def nextTurn():
    global turn
    
    if turn == 1:
        turn = 2
    else:
        turn = 1

def advancePlayer(player, moves):
    global players
    
    newSpace = players[player] + moves

    if newSpace < 1:
        newSpace = 1
    elif newSpace > 49:
        newSpace = 49

    players[player] = newSpace

while players[1] < 49 and players[2] < 49:
    print("Player %d it's your turn!" % (turn))
    print("Your current position is %d" % (players[turn]))
    input("Press <ENTER> to roll!")

    roll = rollDice()
    total = sum(roll)

    if isDouble(roll):
        total *= -1

    print("Die A: %d, Die B: %d, Total = %d" % (roll[0], roll[1], total))

    advancePlayer(turn, total)

    print("Your new position is %d" % (players[turn]))

    nextTurn()

    print("")

input("End Of Game")
