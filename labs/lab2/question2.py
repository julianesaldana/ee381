import random

counter = 0  # will keep track of equal amount of boys and girls
for i in range(100000):  # do experiment 100000 times
    n = 10  # given by problem, change to 50
    children = 4 * n  # total number of children in a class
    boys = 0  # keep track of number of boys
    for j in range(children):  # adding children to a classroom n amount 4n amount of times
        rand = round(random.random())  # rand will equal 1 or 0
        if rand == 0:
            boys += 1  # boy is incremented if rand == 0
    if children / boys == 2:  # if there is half of boys, then there is equal amount of boys and girls
        counter += 1
print("Probability: %f" % (counter / 100000))
