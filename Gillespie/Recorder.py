from collections import namedtuple
#timeConc = namedtuple('timeConc', ['time', 'E', 'P', 'S', 'ES'])
##### SUPPORT FOR gillespie.py ##########
class Recorder:
    def __init__(self, E, P, S, ES):

        self.EConc = [E];  self.PConc = [P]; self.SConc = [S]
        self.time = [0];self.ESConc = [ES]

        self.concentrations = [self.time, self.EConc, self.PConc, self.SConc, self.ESConc]

    def __call__(self, time, E, P, S, ES):
        self.time.append(time)
        self.EConc.append(E)
        self.PConc.append(P)
        self.SConc.append(S)
        self.ESConc.append(ES)
