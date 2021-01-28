import random
import numpy as np
import matplotlib.pyplot as plt

# total_rolls = 100000
# for i in range(total_rolls):
#     for i in range(60):
#         firstDie = random.randint(1, 6)
#         secondDie = random.randint(1, 6)

# total_rolls = 60
# firstDie = np.zeros((total_rolls, 1))
# secondDie = np.zeros((total_rolls, 1))
# for i in range(total_rolls):
#     firstDie[i, :] = round(random.randint(1, 6))
#     secondDie[i, :] = round(random.randint(1, 6))
#
# N = 100000
# x = np.zeros((N, 1))
# for i in range(N):
#     x[i, :] = pow((5 / 6), (i - 1)) * (1 / 6)
# bins = np.arange(1, 61, 1)
# plt.hist(x, bins)
# plt.show()

total_flips = 100000
heads = np.zeros((total_flips, 1))
for i in range(total_flips):
    heads[i, :] = round(random.random())
print("number of heads: ", sum(sum(heads)))
print("number of tails: ", sum(total_flips - sum(heads)))

N = 50000
x = np.zeros((N, 1))
for i in range(N):
    x[i, :] = random.random()
bins = np.arange(-1, 1, 0.1)
plt.hist(x, bins)
plt.show()
