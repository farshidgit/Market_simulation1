from __future__ import division

a, b = 120, 1
alpha, beta = 120, -1

def theta_buy(S):  # decreasing function of price
    return alpha + beta * S


def theta_sell(S):  # increasing function of price
    return a + b * S

"""Experiment:
S_e = equilibrium price, where theta_buy(S_e) = theta_sell(S_e)
then a - alpha = (beta-b)S_e. If S_e = S_0, beta = -1/b

"""
