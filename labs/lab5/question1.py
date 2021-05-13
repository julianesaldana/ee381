import matplotlib.pyplot as plt
import numpy as np
import random
import statistics

# declaring the populationSize variable to a value
populationSize = 1000000
# setting the mew variable to a value
mew = 100
# setting the standard deviation variable
standardDeviation = 12
# assigning the sample size to a value
sampleSizeMax = 200
# creating the sample list
sampleList = list(range(1, sampleSizeMax + 1))
# getting a population value
population = np.random.normal(mew, standardDeviation, populationSize)

# initializing the arrays
meanSample = []
upperBoundOf95 = []
lowerBoundOf95 = []
upperBoundOf99 = []
lowerBoundOf99 = []
for i in range(1, len(sampleList)+1):
    # picking a sample of size n which is 1 - 200
    pickSample = random.sample(list(population), i)
    # calculating the mean of the sample that was picked
    meanSample.append(statistics.mean(pickSample))
    # calculating the lower and upper value of the 95% and 99%  confidence interval
    lowerBoundOf95Value = mew - (1.96 * (standardDeviation / np.sqrt(i)))
    upperBoundOf95Value = mew + (1.96 * (standardDeviation / np.sqrt(i)))
    lowerBoundOf99Value = mew - (2.58 * (standardDeviation / np.sqrt(i)))
    upperBoundOf99Value = mew + (2.58 * (standardDeviation / np.sqrt(i)))

    # adding those calculated values to their appropriate arrays
    lowerBoundOf95.append(lowerBoundOf95Value)
    upperBoundOf95.append(upperBoundOf95Value)

    lowerBoundOf99.append(lowerBoundOf99Value)
    upperBoundOf99.append(upperBoundOf99Value)

# plotting and displaying the graph for the 95% confidence interval
plt.plot(sampleList, meanSample, 'bx')
plt.axhline(y=100, color='k', linestyle='-')
plt.plot(sampleList, lowerBoundOf95, 'r--')
plt.plot(sampleList, upperBoundOf95, 'r--')
plt.xlabel("Sample size")
plt.ylabel("X_bar")
plt.title("Sample Means and 95% confidence intervals")
plt.show()

# plotting and displaying the graph for the 99% confidence interval
plt.plot(sampleList, meanSample, 'bx')
plt.axhline(y=100, color='k', linestyle='-')
plt.plot(sampleList, lowerBoundOf99, 'c--')
plt.plot(sampleList, upperBoundOf99, 'c--')
plt.xlabel("Sample size")
plt.ylabel("X_bar")
plt.title("Sample Means and 99% confidence intervals")
plt.show()
