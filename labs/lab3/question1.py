import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def Main():
    # defining the array using numpy
    x = np.arange(-1, 12, 0.01)

    # declaring the variable for a and b
    a = 1
    b = 10

    # calling the probability density function and getting the result from it
    f = probability(x, a, b)
    # displaying the pdf graph
    plt.title("Python Code PDF")
    plt.plot(x, f)
    plt.show()

    # calling the cumulative distribution function and getting the result from it
    F = distribution(x, a, b)
    # displaying the cdf graph
    plt.title("Python Code CDF")
    plt.plot(x, F)
    plt.show()

    # calling the built-in function of stats.uniform.pdf to display the pdf graph
    plt.title("Built In Function PDF")
    plt.plot(x, stats.uniform.pdf(x, a, b - 1))
    plt.show()

    # calling the built-in function of stats.uniform.cdf to display the cdf graph
    plt.title("Built In Function CDF")
    plt.plot(x, stats.uniform.cdf(F))
    plt.show()


# this function is used to calculate the probability density function and return the result
def probability(x, a, b):
    # create a new array using numpy
    value = np.zeros((np.size(x), 1))
    # looping from 0 to the array size and checking the condition before storing the correct value
    for i in range(0, np.size(x)):
        if x[i] <= a or x[i] >= b:
            value[i] = 0

        elif x[i] > a and x[i] < b:
            value[i] = 1 / (b - a)

    return value


# this function is used to calculate the cumulative distribution function and return the result
def distribution(x, a, b):
    # create a new array using numpy
    result = np.zeros((np.size(x), 1))
    # looping from 0 to the array size and checking the condition before storing the correct value
    for i in range(0, np.size(x)):
        if x[i] <= a:
            result[i] = 0

        elif x[i] >= b:
            result[i] = 1

        elif x[i] > a and x[i] < b:
            result[i] = (x[i] - a) / (b - a)

    return result

Main()
