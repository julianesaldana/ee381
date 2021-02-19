import random

counter = 0
for i in range(100000):
    first = random.randint(1, 20)
    cont = True
    for j in range(3):
        rest = random.randint(1, 20)
        if rest == first:
            continue
        else:
            cont = False
            break
    if cont:
        counter += 1
print("Probability: %f" % (counter / 100000))
