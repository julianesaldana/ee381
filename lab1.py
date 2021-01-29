import random
import numpy as np
import matplotlib.pyplot as plt

# creating numpy array
firstDie = np.zeros((100000, 1))
secondDie = np.zeros((100000, 1))

totalExperiments = 0
counter = 0
while totalExperiments < 100000:  # will do experiment n times
    for j in range(60):  # will only add experiments that add to 7 within 60 rolls
        counter += 1
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        if first + second == 7:
            firstDie[totalExperiments, :] = first
            secondDie[totalExperiments, :] = second
            totalExperiments += 1
            counter = 0
            break

count = firstDie + secondDie

x_axis = range(1, 61)
sb = np.size(x_axis)
h1, bin_edges = np.histogram(count, x_axis)
b1 = bin_edges[0:sb - 1]

#
fig1 = plt.figure(1)
plt.stem(b1, h1)
plt.title('Stem plot - Sum of two dice')
plt.xlabel('Number of tries it takes to roll 7 total')
plt.ylabel('Number of occurrences')
fig1.savefig('Sum of two dice.jpg')
