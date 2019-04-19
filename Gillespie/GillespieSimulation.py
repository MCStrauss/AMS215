import math
import random
import matplotlib.pyplot as plt

t = 0                                # time
n = 0                                # iteration
X = 1                                # number of molecules

Xmax = 50                            # maximum number of molecules
totalSimulations = 1000              # number of iterations to run
r0 = 0.01                            # decay rate
r1 = 0.02                            # production rate

simulation = list()                  # results list

while n < totalSimulations:          # main loop
    rT = random.uniform(0, 1)        # generate URN
    rR = bool(random.getrandbits(1)) # randomly select 0 or 1
    t = t + rT                       # increment time

    if rR == 0 and X > 0:            # decay
        X = X - r0 * X
    elif X < Xmax:                   # production
        X = X + r1 * X

    n = n + 1                        # increment iteration counter
    simulation.append((t, int(X)))   # insert results of this run into list

fig = plt.figure()                   # set up plot
plt.axis([0, 1000, 0, Xmax + 10])
plt.xlabel('time')
plt.ylabel('X')

for i in range(len(simulation)):     # plot data
    print(str(i), str(simulation[i][0]), str(simulation[i][1]))
    plt.scatter(i, simulation[i][1],
                s=1, c='black')

plt.savefig("gillespie.png")         # save plot to disk
