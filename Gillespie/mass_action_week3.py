import math
import argparse

####### VARIABLES #######
# x1 = LACI
# x2 = IPTG
# x3  = PLAC
# x4  = mRNA
# x5 = LACI*
# x6 = PLAC*
# * = inactivated form
help_str = 'reaction constant for mass action'
parser = argparse.ArgumentParser(description = 'reaction rates')
parser.add_argument('-r', '--reaction', type = float, help = help_str, nargs= '+')
args = parser.parse_args()


# makes sure we only have 4 reaction coefficients
assert len(args.reaction) <=4 , 'we only have 4 reactions'

# setting default reaction rates
r1 = r2 = r3 = r4 = float()

if args.reaction:
    r1, r2, r3, r4 = args.reaction
else:
    r1, r2, r3, r4 = [1.0] * 4







