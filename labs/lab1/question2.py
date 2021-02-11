import random
import numpy as np
import matplotlib.pyplot as plt

n = 10000
rolls = np.zeros((n, 1))
for i in range(n):
    dieValue = random.random()
    if 0 <= dieValue < 0.1:
        rolls[i, :] = 1  # colon could be a 0 instead for size 1
    elif 0.1 <= dieValue < 0.25:
        rolls[i, :] = 2
    elif 0.25 <= dieValue < 0.55:
        rolls[i, :] = 3
    elif 0.55 <= dieValue < 0.8:
        rolls[i, :] = 4
    elif 0.8 <= dieValue < 0.85:
        rolls[i, :] = 5
    else:
        rolls[i, :] = 6

b = range(1, 8)
sb = np.size(b)
h1, bin_edges = np.histogram(rolls, bins=b)
b1 = bin_edges[0:sb - 1]

fig1 = plt.figure(1)
plt.stem(b1, h1)
plt.title('Stem plot - Value of unfair die')
plt.xlabel('Unfair die roll result')
plt.ylabel('Number of occurrences')
fig1.savefig('unfair die.jpg')
