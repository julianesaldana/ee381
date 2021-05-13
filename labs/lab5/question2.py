import numpy as np
import random
import statistics

# declaring the experiment variable to a value
experiment = 10000
# setting mew to a value
mew = 100
# setting standard deviation to a value
standardDeviation = 12
# declaring the populationSize variable to a value
populationSize = 1000000
# getting a population value
population = np.random.normal(mew, standardDeviation, populationSize)
# calculating the population mean
populationMean = statistics.mean(population)

# creating the count variables for the lower and upper bound of the normal distribution and student's t distribution
count95z = 0
count99z = 0

count95t = 0
count99t = 0


# creating the sample sizes
n = 5
# n = 40
# n = 120

# setting the appropriate student's t distribution value when n = 5
t95ValueForVEquals4 = 2.78
t99ValueForVEquals4 = 4.60

# setting the appropriate student's t distribution value when n = 40
t95ValueForVEquals39 = 2.0227
t99ValueForVEquals39 = 2.7079

# setting the appropriate student's t distribution value when n = 120
t95ValueForVEquals119 = 1.9801
t99ValueForVEquals119 = 2.6178

for i in range(experiment):
    # picking a sample from the population
    pickSample = random.sample(list(population), n)
    # calculating the sample's mean value
    meanSample = statistics.mean(pickSample)
    # calculating the sample's standard deviation value
    standardDeviationSample = statistics.stdev(pickSample)

    # calculating the 95% and 99% confidence interval of the normal distribution
    lowerBound95zValue = meanSample - (1.96 * (standardDeviationSample / np.sqrt(n)))
    upperBound95zValue = meanSample + (1.96 * (standardDeviationSample / np.sqrt(n)))

    lowerBound99zValue = meanSample - (2.58 * (standardDeviationSample / np.sqrt(n)))
    upperBound99zValue = meanSample + (2.58 * (standardDeviationSample / np.sqrt(n)))

    # checking what value n is to calculate the right 95% and 99% confidence interval for the student's t distribution
    if n == 5:
        # calculating the 95% and 99% confidence interval of the student's t distribution when v = n - 1 = 5 - 1 = 4
        lowerBound95tValue = meanSample - (t95ValueForVEquals4 * (standardDeviationSample / np.sqrt(n)))
        upperBound95tValue = meanSample + (t95ValueForVEquals4 * (standardDeviationSample / np.sqrt(n)))

        lowerBound99tValue = meanSample - (t99ValueForVEquals4 * (standardDeviationSample / np.sqrt(n)))
        upperBound99tValue = meanSample + (t99ValueForVEquals4 * (standardDeviationSample / np.sqrt(n)))

    elif n == 40:
        # calculating the 95% and 99% confidence interval of the student's t distribution when v = n - 1 = 40 - 1 = 39
        lowerBound95tValue = meanSample - (t95ValueForVEquals39 * (standardDeviationSample / np.sqrt(n)))
        upperBound95tValue = meanSample + (t95ValueForVEquals39 * (standardDeviationSample / np.sqrt(n)))

        lowerBound99tValue = meanSample - (t99ValueForVEquals39 * (standardDeviationSample / np.sqrt(n)))
        upperBound99tValue = meanSample + (t99ValueForVEquals39 * (standardDeviationSample / np.sqrt(n)))

    elif n == 120:
        # calculating the 95% and 99% confidence interval of the student's t distribution when v = n - 1 = 120 - 1 = 119
        lowerBound95tValue = meanSample - (t95ValueForVEquals119 * (standardDeviationSample / np.sqrt(n)))
        upperBound95tValue = meanSample + (t95ValueForVEquals119 * (standardDeviationSample / np.sqrt(n)))

        lowerBound99tValue = meanSample - (t99ValueForVEquals119 * (standardDeviationSample / np.sqrt(n)))
        upperBound99tValue = meanSample + (t99ValueForVEquals119 * (standardDeviationSample / np.sqrt(n)))

    # checking if the population mean is in between any of the lower and upper bound
    if lowerBound95zValue < populationMean < upperBound95zValue:
        count95z = count95z + 1

    if lowerBound99zValue < populationMean < upperBound99zValue:
        count99z = count99z + 1

    if lowerBound95tValue < populationMean < upperBound95tValue:
        count95t = count95t + 1

    if lowerBound99tValue < populationMean < upperBound99tValue:
        count99t = count99t + 1

# displaying the result
print("n =", n)
print("95% Confidence using normal distribution:", (count95z / experiment))
print("99% Confidence using normal distribution:", (count99z / experiment))
print("95% Confidence using student's t distribution:", (count95t / experiment))
print("99% Confidence using student's t distribution:", (count99t / experiment))
