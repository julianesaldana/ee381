import numpy as np
import matplotlib.pyplot as plt

# number of experiments to run
N = 100000
# declaring the number of books
# nBooks = 1
# nBooks = 5
nBooks = 15
# declaring the values of a and b
a = 1
b = 3
# assigning the values of the variable mu_x and sig_x
mu_x = (a + b) / 2
sig_x = np.sqrt((b - a) ** 2 / 12)
# creating an array using lumpy
X = np.zeros((N, 1))
for k in range(0, N):
    x = np.random.uniform(a, b, nBooks)
    w = np.sum(x)
    X[k] = w

# Create bins and histogram
nBins = 30  # Number of bins
edgeColor = 'w'  # Color separating bars in the bar graph
bins=[float(x) for x in np.linspace(nBooks*a, nBooks*b, nBins+1)]
h1, bin_edges = np.histogram(X, nBins, density=True)
# Define points on the horizontal axis
be1 = bin_edges[0:np.size(bin_edges) - 1]
be2 = bin_edges[1:np.size(bin_edges)]
b1 = (be1 + be2) / 2
barWidth = b1[1] - b1[0]
# Width of bars in the bar graph
plt.close('all')
# PLOT THE BAR GRAPH
fig1 = plt.figure(1)
plt.bar(b1, h1, width=barWidth, edgecolor=edgeColor)


# PLOT THE GAUSSIAN FUNCTION
def gaussian(mu, sig, z):
    f = np.exp(-(z - mu) ** 2 / (2 * sig ** 2)) / (sig * np.sqrt(2 * np.pi))
    return f


f = gaussian(mu_x * nBooks, sig_x * np.sqrt(nBooks), b1)
plt.plot(b1, f, 'r')
plt.title("PDF of book stack height and comparison with Gaussian")
plt.xlabel("Book stack for height for n = " + str(nBooks) + " books")
plt.ylabel("PDF")
plt.show()
