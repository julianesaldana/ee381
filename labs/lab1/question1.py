import random
import numpy as np
import matplotlib.pyplot as plt

rollTracker = []
for j in range(100000):  # will do experiment 100000 times
    counter = 0  # resets counter
    for i in range(60):  # performs up to 60 dice rolls to land a 7
        firstDie = random.randint(1, 6)
        secondDie = random.randint(1, 6)
        counter += 1  # counts how many dice rolls it takes to land a seven
        if (firstDie + secondDie) == 7:
            rollTracker.append(counter)  # adds counter to array
            break

N = len(rollTracker)  # creating np array of zeroes, up to length of the total rolls
x = np.zeros((N, 1))
for i in range(N):
    x[i, :] = rollTracker[i]  # restoring numbers in the new array
bins = np.arange(1, 60, 0.5)  # goes from 0-60, bars are 0.5 wide
plt.hist(x, bins)  # creates histogram based on information from array
plt.show()
