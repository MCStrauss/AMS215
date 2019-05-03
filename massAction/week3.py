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

"""

r1 = 2; r2 = 2; r3 = 2  # rates of reaction

x1 = 10; x2 = 10; x3 = 10; x5 = 5; x4 =   # concentrations of repressor protein

def dx_x2(x2, t) -> float:
    # dx2/dt = dx3/dt
    # IPTG  and inactivated repressor protein respectively
    # models IPTG (x3) attatching to repressor protein (x2) and going to inactivated form (x5)
    dx2dt = -r1 * x2 * x3 + r2 * x5
    return dx2dt


def dx_x5(x5, t):
    # models concentratino of inactives repressor protein (x5)
    # dependent on x2 (repressor protein) x3 (IPTG)
    # decay of deactivated repressor proetin (x5)
    #decay
    dx5dt = (r1 * x2 * x3) - (r2 * x5 )

    return dx5dt

def mRNA():
    pass


funcs = [(dx_x2,'Graph_dx3_dx2.png'),
         (dx_x5, 'Graph_dx5'), ]

def main():
    time = np.linspace(0, 100, 1000) # 100 seconds split over 1000 time steps
    # args is odeint(function, y(0) right when we start, interval to calculate over

    for func, name in funcs:
        y = odeint(func, 5, time)
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