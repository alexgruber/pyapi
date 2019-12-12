
import numpy as np
import pandas as pd

class API(object):

    def __init__(self, gamma = 0.85, Q = None):

        # initialize model parameters
        self.gamma = gamma

        # initialize forcing error
        self.Q = Q

        # initialize state vector and background error
        self.x = 0
        self.P = 0

    def step(self, f, err=0):

        # model prediction + perturbation
        self.x = self.x * self.gamma + f + err

        # if forcing error is provided: error propagation (ASSUMES ADDITIVE ERROR!!)
        if self.Q is not None:
            self.P = self.gamma**2 * self.P + self.Q

            return self.x, self.P
        else:
            return self.x


