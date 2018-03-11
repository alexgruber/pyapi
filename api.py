
import numpy as np
import pandas as pd

class API(object):

    def __init__(self, gamma = 0.85, Q = None):


        # initialize model parameters
        self.gamma = gamma

        # initialize forcing error
        self.Q = Q

        # initialize state vector and background error
        self.x = pd.Series(0., index=('sm',))
        self.P = pd.Series(0., index=('sm',))

    def step(self, f):

        # model prediction
        self.x['sm'] = self.x['sm'] * self.gamma + f['precip']

        # if forcing error is provided: error propagation (ASSUMES ADDITIVE ERROR!!)
        if self.Q is not None:
            self.P['sm'] = self.gamma**2 * self.P['sm'] + self.Q['precip']

            return self.x, self.P
        else:
            return self.x


