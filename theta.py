alpha, beta = .2, 2
a, b = .10, -4


def theta_buy(S):
    return alpha + beta * S


def theta_sell(S):
    return alpha + beta * S


