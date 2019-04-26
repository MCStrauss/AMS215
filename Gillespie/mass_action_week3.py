import math
import argparse
import matplotlib.pyplot as plt
import random

####### VARIABLES #######
# x1 = LACI
# x2 = IPTG
# x3  = PLAC
# x4  = mRNA
# x5 = LACI*
# x6 = PLAC*
# * = inactivated form
parser = argparse.ArgumentParser(description = 'arguments to stimulate LACI transcription factor')
parser.add_argument('-r', '--reaction', type = float, help = 'reaction rate for mass action')
parser.add_argument('-f', '--finish', type = int, help = 'Finish time for reaction stimulation')
args = parser.parse_args()

# setting default reaction rates
r1 = 1.0; finish = 100

# start concentration for x1, x2, and x5
# x1 = 5; x2 = 8; x5 = 1

def get_args():
    if args.reaction:
        r1 = args.reaction
    if args.finish:
        finish = args.finish

def stimulate(finish, rr, x1 = 5, x2 = 8, x5 = 1):
    # x1 mass reaction
    # dx1/dt = -r1[x1][x2] + r1[x5]

    start = 0
    change_x1 = []
    while start < finish:

        rR = bool(random.getrandbits(1))

        if rR:

            #x1 -= 1; x2 -= 1
            #x5 += 1
            dx1 = -rr * x1 * x2
            x1 += dx1

        else:

            #x1 +=1 ; x2 += 1
            #x5 -= 1

            dx1 = rr * x5
            x1 += dx1



        change_x1.append((start, x1)) # change is a list with tuple of time and change in x1
        start += 1

    return change_x1



def main():

    get_args() # grabs argparse args

    data = stimulate(finish, r1)

    fig = plt.figure()  # set up plot

    #plt.axis([0, finish, -10, 10]) #x-min, x-max, y-min, y-max
    plt.xlabel('time')
    plt.ylabel('X')

    for time in range(finish):
        print(time, data[time][1])
        plt.scatter(time, data[time][1],
                s=1, c='black')

    plt.savefig("mass_action.png")  # save plot to disk












if __name__ == '__main__':
    main()