import numpy as np

def Main():
    # declaring the radius value
    radius = 10
    # to keep track of the number of times the points are on the same semicircle
    count = 0
    # declaring the circumference of the circle
    circumference = 2 * np.pi * radius
    # declaring the value of the semicircle
    semi_circle = circumference / 2

    # the number of time to run this experiment
    experiment = 100000

    # this loop is looping through the
    # experiment 100,000 times
    for i in range(experiment):
        threePoints = []
        pointCount = 0

        # this while loops is selecting 3 random points
        # and checking to see if there is any duplicate
        # before being added to the variable threePoints
        while pointCount < 3:
            point = np.random.uniform(0, circumference)
            if point not in threePoints:
                threePoints.append(point)
                pointCount = pointCount + 1

        # sorting the array to be in ascending order
        threePoints.sort()

        # checking if the 3 points from the
        # variable threePoints are on the same semicircle
        # these conditions are checking if the line that split
        # the semicircle are diagonal, vertical, or horizontal
        if threePoints[2] - threePoints[0] <= semi_circle:
            count = count + 1
        else:
            if threePoints[2] - threePoints[0] > semi_circle:
                if threePoints[1] - threePoints[0] <= semi_circle:
                    if circumference - (threePoints[2] - threePoints[1]) <= semi_circle:
                        count = count + 1
                elif circumference - (threePoints[1] - threePoints[0]) <= semi_circle:
                        count = count + 1

    # display the result
    print(count / experiment)


Main()
