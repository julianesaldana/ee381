import random

total_flips = 1000000
heads = 0
count = 0
coin = 0

for i in range(total_flips):  # do experiment 100000 times
    heads = 0  # resets number of heads
    for j in range(100):  # flip 100 times
        coin = round(random.random())
        if coin == 0:
            heads += 1
    if heads == 35:  # increment counter every time there are 35/100 heads
        count += 1

print("Probability that 35 heads showed up out of 100, out of 100000 experiments: %f" % (count / total_flips))
