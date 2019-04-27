import argparse
import matplotlib.pyplot as plt
import random
from typing import List

####### VARIABLES #########
# x1 = LACI
# x2 = IPTG
# x3  = PLAC
# x4  = mRNA
# x5 = LACI*
# x6 = PLAC*
# * = inactivated form

######### PARSER ###############
parser = argparse.ArgumentParser(description = 'arguments to stimulate LACI transcription factor')
parser.add_argument('-r', '--reaction', type = float, help = 'reaction rate for mass action')
parser.add_argument('-f', '--finish', type = int, help = 'Finish time for reaction stimulation')
args = parser.parse_args()

# setting default reaction rates
r1 = 1.0; finish = 100

# start concentration for x1, x2, and x5
# x1 = 5; x2 = 8; x5 = 1

def get_args() -> None:
    if args.reaction:
        r1 = args.reaction
    if args.finish:
        finish = args.finish

def stimulate_original_mass_action(finish:int, rr:float, x1 = .25, x2 = .25, x5 = .5) -> List:
    # x1 mass reaction
    # dx1/dt = -r1[x1][x2] + r1[x5]
    start = 0
    change_x1 = []
    while start < finish:

        rR = bool(random.getrandbits(1))

        if rR:
            dx1 = -rr * x1 * x2
            x1 += dx1

        else:
            dx1 = rr * x5
            x1 += dx1

        change_x1.append((start, x1)) # change is a list with tuple of time and change in x1
        start += .1
    return change_x1

def stimulate_QSSA():
    #todo get QSSA working should be easy
    pass


def main():

    get_args() # grabs argparse args

    data = stimulate_original_mass_action(finish, r1)

    fig = plt.figure()  # set up plot

    plt.xlabel('time')
    plt.ylabel('X')

    for time, value in data:
        plt.scatter(time, value,
                s=1, c='black')

    plt.savefig("mass_action.png")  # save plot to disk
if __name__ == '__main__':
    main()