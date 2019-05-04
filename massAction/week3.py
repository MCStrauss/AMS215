from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

"""
A DIFFERENTIAL EQUATION is a relation between a function and its
derivatives.

Differential equations form the language in which the basic laws of
science are expressed. The science tells us how the system at hand
changes "from one instant to the next." The challenge addressed by the
theory of differential equations is to take this short-term
information and obtain information about long-term overall behavior.
So the art and practice of differential equations involves the following
sequence of steps: one "models" a system (physical, chemical, biological,
economic, or even mathematical) by means of a differential equation;
one then attempts to gain information about solutions of this equation;
and one then translates this mathematical information back into the
scientific context.

STATE DEFINITIONS:

x2 = repressor (LacI)
x2* = inactivated repressor
x3 = IPTG
x4 = promoter
x4* = bound promoter
x6 = mRNA

MASS ACTION EQUATIONS
R = reaction reate
X2 + X4 ->(r1) <-(r2) x4* 
X2 + X3 -> (r3) <- (r4) X2*
X4 -> (r5) X4 + X6
X6 -> (r6) ø

"""

def differentials(state, t) -> list:
    r1 = .5; r2 = .1; r3 = .1; r4 = .7; r5 = .3; r6 = .2  # rates of reaction
    x2, x2Star, x3, x4, x4Star, x6 = state

    dx2dt = (-r1*x2*x4) + (r2 * x4Star) - (r2 * x2 * x3 ) + (r4 * x4Star)

    dx3dt = -(r5*x2*x3) + (r4*x2Star)

    dx4dt = -(r1 * x2 * x4) + (r2 * x4Star)

    dx2Stardt = (r3 * x2 * x3) - (r4 * x2Star)

    dx4Stardt = (r1*x2 * x4) - r2 * x4Star

    dx6dt = (r5 * x4) - (r6 * x6)

    return [dx2dt, dx3dt, dx4dt, dx2Stardt, dx4Stardt, dx6dt]

def QSSA(state, t) -> list:
    r1 = .7; r2 = 1; r3 = .7; r4 = 1; r5 = 4; r6 = 10  # rates of reaction
    x2, x2Star, x3, x4, x4Star, x6 = state

    # assume dx4dt as 0

    dx2dt = (-r1*x2*x4) + (r2 * x4Star) - (r2 * x2 * x3 ) + (r4 * x4Star)

    dx3dt = -(r5*x2*x3) + (r4*x2Star)

    #dx4dt = -(r1 * x2 * x4) + (r2 * x4Star)

    dx4dt = 0

    dx2Stardt = (r3 * x2 * x3) - (r4 * x2Star)

    dx4Stardt = (r1*x2 * x4) - r2 * x4Star

    dx6dt = (r5 * x4) - (r6 * x6)

    return [dx2dt, dx3dt, dx4dt, dx2Stardt, dx4Stardt, dx6dt]

def main():
    time = np.linspace(0, 100, 50) # 100 seconds split over 1000 time steps
    # args is odeint(function, y(0) right when we start, interval to calculate over
    funcs = [(differentials, 'differentials.png'), (QSSA, 'QSSA.png')]
    for func, name in funcs:
        y = odeint(func, [100, 100, 100, 10, 10, 1,], time)
        plt.plot(time,y)
        plt.savefig(name)
        plt.clf()


if __name__ == '__main__':
    main()

"""
#def dx_x6(x1, t):

 #   dx6 = r5 * x1
  #  return dx6


#def dx_x4(x4, t):
    # models
 #   dx4dt = r1 * x2 * x3  - (r2 * x5)

  #  return dx4dt

"""