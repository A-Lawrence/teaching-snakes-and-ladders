# Snakes and Ladders

This is an example of a Snakes and Ladders solution for sample NEA #3 from OCR.  This is *not* the difinitive method of solving this task.  This *is* a possible solution, using only the techniques taught to *my* students at the point they'll start the real NEA.

## Version 1
- Simple player movement system
- Two counters
- When one hits 49, it stops

## Version 2
- Detect a double roll
- If it's a double, subtract the total score (rather than add)

## Version 3
- Store all important messages inside a list (for easy editing later)
 - This is akin to a language pack you'd often find in a piece of software
 
## Version 4
- Store all important messages in an external CSV
- Load all messages when the script runs

## Version 4.1
- Decided to store all messages displayed to the player in the CSV to show how it can be easily adapted

## Version 5
- Implement some kind of obstacle list
- Obstacles either have a negative or positive value
- Negative obstacles act like snakes (you go backwards)
- Positive obstacles act like ladders (you go forwards)

## Version 5.1
- Stored obstacles externally in a CSV
- Loaded obstacles when the script runs

## Version 6
- Introduce a really simple graphical version of the board
- Players are A and B
- Cells display either a `-` or `+` next to them for obstacles
