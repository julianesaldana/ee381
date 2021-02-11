import random


def createDeck():
    # Creates a deck and shuffles it, taken from my CECS277 Solitaire project with Professor Steve Gold
    suits = ['H', 'D', 'S', 'C']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    stack = []

    # creates deck
    for i in range(len(suits)):
        for j in range(len(ranks)):
            stack.append(ranks[j] + suits[i])

    # shuffles deck
    for i in range(52):
        cardPos = random.randint(0, 51)
        tempCard = stack[i]
        stack[i] = stack[cardPos]
        stack[cardPos] = tempCard

    # creates small deck of six cards, first six dealt from deck created above
    deck = []
    for i in range(6):
        deck.append(stack[i])

    return deck


def main():
    counter = 0  # four of a kind counter
    n = 100000  # will run experiment 100000 times

    for i in range(n):
        deck = createDeck()  # deck of 6 cards created
        ranks = {}  # dictionary will used to keep track of repeating numbers

        for j in range(len(deck)):  # length of 6
            if deck[j][0] not in ranks:  # if the number of the card isn't already in dictionary, it
                ranks[deck[j][0]] = 1  # adds only the RANK (not suit) of the card to dictionary and key value 1
            else:
                ranks[deck[j][0]] += 1  # if rank already in the dictionary, increments the key value by one

        for number in ranks:
            if ranks[number] == 4:
                counter += 1
    print("Number of 4-of-a-kinds that occurred: %s" % counter)
    print("Probability: %f" % (counter / n))


main()
