import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []

with open('data-test-fundamentus.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=';')
    for row in plots:
        x.append(float(str(row[1]).replace(",", ".")))
        y.append(float(str(row[3]).replace(",", ".")))


# SIMPLE WAY WITH NUMPY
#x, y = np.loadtxt("data-test-fundamentus.csv", delimiter=";", unpack=True)

plt.plot(x, y, label="Loaded from test data")
plt.xlabel("price")
plt.ylabel("pvp")
plt.title("Stock prices")
plt.legend()
plt.show()