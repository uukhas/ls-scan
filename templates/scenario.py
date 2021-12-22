# Author: Uladzimir Khasianevich
from random import random

class Scenario:

    model = 'MRSSM2'
    ndots = 100 # Optional parameter, it overrides the value, defined by -P

    # Parameter i is the number of the curent dot
    def __init__(self, i=0):
        self.input = dict(
            tan_b = 2.0+30*random(),
            susy_scale = 500,
            bmu = 1e6,
            mu_u = 400,
            mu_d = 400,
            lam_sd = 1.0,
            lam_su = -0.8,
            lam_td = -1.0,
            lam_tu = -1.2,
            mS2 = 1e6,
            mRu2 = 4e6,
            mRd2 = 4.9e6,
            mT2 = 9e6,
            moc2 = 1e6,
            MDBS = 600,
            MDWB = 500,
            MDGoc = 1500,
            mq2_11 = 1e6, mq2_22 = 1e6, mq2_33 = 1e6,
            mu2_11 = 1e6, mu2_22 = 1e6, mu2_33 = 1e6,
            md2_11 = 1e6, md2_22 = 1e6, md2_33 = 1e6,
            ml2_11 = 1e6, ml2_12 = 1e3, ml2_21 = 1e3, ml2_22 = 1e6, ml2_33 = 1e6,
            me2_11 = 1e6, me2_12 = 1e3, me2_21 = 1e3, me2_22 = 1e6, me2_33 = 1e6
        )
        self.names = [*self.input] + [
            'g_mu', 'br_mug'] # Put here the values, which you want to save
