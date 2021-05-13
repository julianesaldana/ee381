import numpy as np
import matplotlib.pyplot as plt
import math


def Main():
    # defining the array using numpy
    arrayX = np.arange(-6, 6, 0.01)

    # calling the calculate density function and getting the result from it
    calculateDensityFunction(arrayX)

    # calling the calculate distribution function and getting the result from it
    calculateDistributionFunction(arrayX)


# this function's purpose is to calculate the
# density by calling the density function to get the result
def calculateDensityFunction(arrayX):
    point1 = densityFunction(arrayX, 0, 1)
    plt.plot(arrayX, point1)
    point2 = densityFunction(arrayX, 0, math.pow(10, -1))
    plt.plot(arrayX, point2)
    point3 = densityFunction(arrayX, 0, math.pow(10, -2))
    plt.plot(arrayX, point3)
    point4 = densityFunction(arrayX, -3, 1)
    plt.plot(arrayX, point4)
    point5 = densityFunction(arrayX, -3, math.pow(10, -1))
    plt.plot(arrayX, point5)
    point6 = densityFunction(arrayX, -3, math.pow(10, -2))
    plt.plot(arrayX, point6)
    plt.title("Python Code PDF")
    plt.show()


# This function's purpose is to get the distribution
# function by calling the distribution function to get the result
def calculateDistributionFunction(arrayX):
    pointOneValues = []
    pointTwoValues = []
    pointThreeValues = []
    pointFourValues = []
    pointFiveValues = []
    pointSixValues = []

    for i in range(len(arrayX)):
        point1 = distributionFunction(arrayX[i], 0, 1)
        pointOneValues.append(point1)
        point2 = distributionFunction(arrayX[i], 0, math.pow(10, -1))
        pointTwoValues.append(point2)
        point3 = distributionFunction(arrayX[i], 0, math.pow(10, -2))
        pointThreeValues.append(point3)
        point4 = distributionFunction(arrayX[i], -3, 1)
        pointFourValues.append(point4)
        point5 = distributionFunction(arrayX[i], -3, math.pow(10, -1))
        pointFiveValues.append(point5)
        point6 = distributionFunction(arrayX[i], -3, math.pow(10, -2))
        pointSixValues.append(point6)

    # plotting the points and displaying the graph
    plt.plot(arrayX, pointOneValues)
    plt.plot(arrayX, pointTwoValues)
    plt.plot(arrayX, pointThreeValues)
    plt.plot(arrayX, pointFourValues)
    plt.plot(arrayX, pointFiveValues)
    plt.plot(arrayX, pointSixValues)
    plt.title("Python Code CDF")
    plt.show()


# This function is used to calculate the density function values and return the results
def densityFunction(arrayX, mew, standardDeviation):
    result = (1 / np.sqrt(2 * np.pi * standardDeviation)) * (np.e ** ((-(arrayX - mew) ** 2) / (2 * standardDeviation)))

    return result


# This function is used to calculate the distribution function values and return the result
def distributionFunction(arrayX, mew, standardDeviation):
    answer = (1 / 2) * (math.erf(((arrayX - mew) / np.sqrt(2 * standardDeviation)))) + (1 / 2)

    return answer


Main()
