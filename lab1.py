import random
import numpy as np
import matplotlib.pyplot as plt

list_Prob = []
list_Obj = []
for i in range(60):
    x = pow((5 / 6), (i - 1)) * (1 / 6)
    list_Prob.insert(i + 1, x)

for j in range(60):
    list_Obj.insert(j, j + 1)

y_pos = np.arange(len(list_Obj))
performance = list_Prob

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, list_Obj)
plt.ylabel('P(X=x)')
plt.title('Probability Histogram')

plt.show()
