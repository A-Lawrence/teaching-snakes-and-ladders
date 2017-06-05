# Version 1
# This version gets us started with the NEA:
# - allows 2 players to play the game
# - allows the players to take turns two 6 sided dice and move
# - displays the result of the move (not visually)

import random

players = { 1 : 0, 2 : 0 }
turn = 1

def rollDice():
    return (random.randint(1, 6), random.randint(1, 6))

def nextTurn():
    global turn
    
    if turn == 1:
        turn = 2
    else:
        turn = 1

def advancePlayer(player, moves):
    global players
    
    newSpace = players[player] + moves

    players[player] = min([newSpace, 49])

while players[1] < 49 and players[2] < 49:
    print("Player %d it's your turn!" % (turn))
    print("Your current position is %d" % (players[turn]))
    input("Press <ENTER> to roll!")

    roll = rollDice()
    total = sum(roll)

    print("Die A: %d, Die B: %d, Total = %d" % (roll[0], roll[1], total))

    advancePlayer(turn, total)

    print("Your new position is %d" % (players[turn]))

    nextTurn()

    print("")

input("End Of Game")
