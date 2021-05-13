import numpy as np
import matplotlib.pyplot as plt

# number of experiments to run
N = 100000
# declaring the battery value
nBattery = 24
# declaring the beta value
beta = 45
# assigning beta to mu_x and sig_x variables
mu_x = beta
sig_x = beta
# creating an array by using numpy
X = np.zeros((N, 1))
for k in range(0, N):
    x = np.random.exponential(beta, nBattery)
    w = np.sum(x)
    X[k] = w

# Create bins and histogram
nBins = 30  # Number of bins
edgeColor = 'w'  # Color separating bars in the bar graph
bins = [float(x) for x in np.linspace(0, 2000, nBins + 1)]
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


# displaying the PDF graph
f = gaussian(mu_x * nBattery, sig_x * np.sqrt(nBattery), b1)
plt.plot(b1, f, 'r')
plt.title("PDF of the lifetime of a carton of batteries and comparison with Gaussian")
plt.xlabel("Lifetime of the carton of batteries in days")
plt.ylabel("PDF")
plt.show()

# displaying the CDF graph
cdf = np.cumsum(h1 * barWidth)
plt.plot(b1, cdf, 'r')
plt.title("CDF graph of the lifetime of a carton of batteries")
plt.xlabel("Lifetime of the carton of batteries in days")
plt.ylabel("CDF")
plt.show()
