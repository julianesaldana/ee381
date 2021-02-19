import random

experiments = 100000  # number of times experiment will be run
counter = 0  # will keep track of how many times each experiment results in 4 people from the same party
for i in range(experiments):
    a = 0  # three parties, three variables
    b = 0
    c = 0

    rangeTotal = 1000  # keeping track of ranges, these are only starting ranges, they will be modified as for loop runs

    rangeOneEnd = 500  # range one start is always 1, no need to declare

    rangeTwoStart = 501
    rangeTwoEnd = 800

    rangeThreeStart = 801  # range three end is the same as rangeTotal, no need to declare

    for j in range(4):  # 4 people chose at random, so will loop 4 times
        rand = random.randint(1, rangeTotal)
        if 1 <= rand <= rangeOneEnd:  # range represents the probability of being in the party
            a += 1
            rangeOneEnd -= 1  # decreases every range if party a
            rangeTwoStart -= 1
            rangeTwoEnd -= 1
            rangeThreeStart -= 1
        elif rangeTwoStart <= rand <= rangeTwoEnd:
            b += 1
            rangeTwoEnd -= 1  # decreases ranges for b and c only
            rangeThreeStart -= 1
        elif rangeThreeStart <= rand <= rangeTotal:
            c += 1  # decreases range for c only at end of for loop

        rangeTotal -= 1  # reduces range total for every loop

    if a == 4 or b == 4 or c == 4:  # if all people supported the same group, counter will increment
        counter += 1

print("Probability: %f" % (counter / experiments))
