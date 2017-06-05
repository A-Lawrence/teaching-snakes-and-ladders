# Version 4.1
# This version builds on the last:
# - Added far more language entries to the file to demonstrate use.

import random
import csv

FILE_MESSAGES = "nea_3_messages.csv"

messages = { "start" : "", "double" : "", "winner" : "" }
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

def whoWon():
    if players[1] >= 49:
        return 1

    if players[2] >= 49:
        return 2

    return 0

def loadMessages():
    file = open(FILE_MESSAGES, "r")
    reader = csv.reader(file)

    for row in reader:
        messages[row[0]] = row[1]

    file.close()

loadMessages()

print("=" * len(messages["start"]))
print(messages["start"])
print("=" * len(messages["start"]))
print("")

while players[1] < 49 and players[2] < 49:
    print(messages["turn"] % (turn))
    print(messages["currentposition"] % (players[turn]))
    input(messages["roll"])

    roll = rollDice()
    total = sum(roll)

    if isDouble(roll):
        print(messages["double"])
        total *= -1

    print(messages["rollresult"] % (roll[0], roll[1], total))

    advancePlayer(turn, total)

    print(messages["newposition"] % (players[turn]))

    nextTurn()

    print("")

print("=" * len(messages["winner"]))
print(messages["winner"] % (whoWon()))
print("=" * len(messages["winner"]))
