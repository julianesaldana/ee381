import random


def createDeck():
    # Creates a deck and shuffles it, taken from my CECS277 Solitaire project with Professor Steve Gold
    suits = ['H', 'D', 'S', 'C']
    ranks = ['A', '2', ' 3', '4', ' 5', '6', '7', '8', ' 9', '10', 'J', 'Q', 'K']
    temp = []

    # creates deck
    for i in range(len(suits)):
        for j in range(len(ranks)):
            temp.append(ranks[j] + suits[i])

    # shuffles deck
    for i in range(52):
        cardPos = random.randint(0, 51)
        tempCard = temp[i]
        temp[i] = temp[cardPos]
        temp[cardPos] = tempCard

    # creates small deck of six cards, first five dealt from deck created above
    deck = []
    for i in range(6):
        deck.append(deal(temp))

    return deck


# function created to deal cards, utilized in function above
def deal(deck):
    temp = deck[0]
    deck.pop(0)
    return temp


def main():
    counter = 0
    n = 20000000
    for i in range(n):
        deck = createDeck()
        if (deck[0] == deck[1] and deck[0] == deck[2] and deck[0] == deck[3]) or (deck[1] == deck[2] and deck[1] == deck[3] and deck[1] == deck[4]) or (deck[2] == deck[3] and deck[2] == deck[4] and deck[2] == deck[5]):
            counter += 1
    print("Number of 4-of-a-kinds that occurred: %s" % counter)
    print("Probability: %f" % (counter/n))


main()
