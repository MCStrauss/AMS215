import random
import matplotlib.pyplot as plt
from Recorder import Recorder

# algorithm walkthrough
# 1.) write out all possible elemental reactions that can happen
# 2.) Each reaction has a probability associated with it, and the choice of the next event is weighted by it
# 3.) choose 2 random numbers
# 4.) First # is to randomly pick the next reaction that will occur
# 5.) second # is to pick when the next reaction will occur
# 6.) Adjust all the concentrations of the individual components to account for whatever reaction got chosen
# 7.) Iterate that to create a timeline for single chain of random events until some preset length of time has elapsed
# 8.) with a large list of chains, can combine the resulting states of the system

# PRODUCT
# E = ENZYME
# S = SUBSTRATE
# P = PRODUCT

# BASIC REACTION
# E + S -> ES
# ES -> E +S
# ES -> E +P


######## Start Values ########
tEnd = 500 # when to stop simulation
tStart = 0 #  when to end simulation
E = 100
S = 300
ES = 400
P = 300
record = Recorder(E, P, S, ES) #object used to record concentration
######################

while tStart < tEnd:

    nextReaction = random.choice([1, 2, 3]) # picks next reaction
    timeUntilNextReaction = random.uniform(0, 1) # picks when the next reaction will occur
    tStart += timeUntilNextReaction

    if nextReaction == 1:
        E -= 1; S-=1; ES +=1

    elif nextReaction == 2:
        E +=1; S +=1; ES -=1
    else:
        E+=1; P+=1; ES -= 1

    record(tStart, E, P, S, ES)

def main():

    plt.plot(record.time, record.EConc)
    plt.plot(record.time, record.PConc)
    plt.plot(record.time, record.SConc)
    plt.plot(record.time, record.ESConc)

    plt.xlabel('time')
    plt.ylabel('concentration')
    plt.savefig('simulationGillespie.png')
if __name__ == '__main__':
    main()