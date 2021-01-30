import random
import numpy as np
import matplotlib.pyplot as plt

N = 100000
d1 = np.zeros(N, 1)
d2 = np.zeros(N, 1)
rolls = np.zeros(N, 1)
count = 0
for i in range(N):
    while count < 60:
        d1[1:] = random.randInt(1, 6)
        d2[2:] = random.randInt(1, 6)
        sum = d1[i] + d2[i]
        if sum == 7:
            rolls[i] = count
            break
count += 1



# list_Prob = []
# list_Obj = []
# for i in range(60):
#     x = pow((5 / 6), (i - 1)) * (1 / 6)
#     list_Prob.insert(i + 1, x)
#
# for j in range(60):
#     list_Obj.insert(j, j + 1)
#
# y_pos = np.arange(len(list_Obj))
# performance = list_Prob
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, list_Obj)
# plt.ylabel('P(X=x)')
# plt.title('Probability Histogram')
#
# plt.show()
