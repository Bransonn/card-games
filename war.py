# Imported so the lists can be shuffled
import random

# Creating Decks with values 1-10. The values are used as cards
edeck = [1,2,3,4,5,6,7,8,9,10]
deck = [1,2,3,4,5,6,7,8,9,10]
# The empty 'hands' recieve cards through a pop() from their respective decks
hand = []
ehand = []
# Each turn, one of these numbers goes up by one, by the end, a winner is determined
playerWins = 0
enemyWins = 0

# This function shuffles both players decks, and sets the starting hand of each player
def getHand():
    random.shuffle(deck)
    random.shuffle(edeck)
    print "------------------------------------------------------------------------------"
    print "Welcome to the Game of War!\nHow to Play:\nYou and an oppenent will draw a hand. Each turn you will each draw a card\nand then choose a card to play.  The goal of the game is to choose a card\nwith a larger value than your oppenent."
    print "\nDrawing Hand...\n"
    for x in range (0,3):
        hand.append(deck.pop())
        ehand.append(edeck.pop())
# If the decks still have cards, then they are able to draw more
def drawCard():
    if deck:
        hand.append(deck.pop())
        ehand.append(edeck.pop())
# This is redundent, just made the logic easier for me to follow
def turn():
    print "Drawing Card..."
    drawCard()
# Lists all the cards, and the respective value in the list
def handPosition():
    nextNum = 0
    print "------------------------------------------------------------------------------"
    print "Your Hand:"
    print "------------------------------------------------------------------------------"
    for cards in hand:
        print "Card",nextNum,"Value",cards,"|",
        nextNum += 1

    print "\n------------------------------------------------------------------------------"
    choice = input("What would you like to play?\n> ")
    return hand.pop(choice)
# Similar to the users function 'handPosition', although the enemy will determine the largest card and play it
def enemyPlay():
    largestCard = 0
    listRemoval = 0
    for cards in ehand:
        if cards > largestCard:
            largestCard = cards
            cardKill = listRemoval
            listRemoval += 1
    return ehand.pop(cardKill)
# Compares both players cards, decides a winner
def war(player,enemy):
    print "Enemy Card:",enemy,"\nPlayer Card:",player,

    if player < enemy:
        print "Player Loses!"
        return 1
    elif player > enemy:
        print "Player Wins!"
        return 2
    else:
        print "Draw!"
        return 3
# Draws cards, looks neater
def setup():
    getHand()
# Game Logic
# For loop determines how many turns, in this case 10.
# Each player goes through their respective card choosing functions
# and the war function determines a winner.  A tally is kept of each
# victory, and compared at the end.
setup()
for turns in range(0,10):
    turn()
    choice = handPosition()
    echoice = enemyPlay()
    winner = war(choice,echoice)

    if winner == 2:
        playerWins += 1
    elif winner == 1:
        enemyWins += 1

if playerWins > enemyWins:
    print "\nGame Over! Player Wins!"
else:
    print "\nGame Over! Enemy Wins!"
