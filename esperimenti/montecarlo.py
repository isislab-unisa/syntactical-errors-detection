import numpy as np
import matplotlib.pyplot as plt


def montecarlo():

    counterIn, counterTotal = 0, 0
    xInPoints, yOutPoints, xOutPoints, yInPoints= [], [], [], []
    piValues = []
    np.random.seed()
    for i in range(1, 10**5):
        x = np.random.rand()
        y = np.random.rand()

        if x**2 + y**2 < 1:
            counterIn = counterIn + 1
            xInPoints.append(x)
            yInPoints.append(y)
        else:
            xOutPoints.append(x)
            yOutPoints.append(y)

        counterTotal = counterTotal +1
        piValues.append(4*(counterIn / counterTotal))

    plt.plot(piValues)
    plt.show()

    plt.scatter(x=xInPoints, y=yInPoints, c="red")
    plt.scatter(x=xOutPoints, y=yOutPoints, c="blue")
    plt.show()



montecarlo()
