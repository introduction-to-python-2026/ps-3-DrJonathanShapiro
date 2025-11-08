def approximate_pi(n_terms):
    pi = 0.0
    for i in range(n_terms):
        term = (-1) ** i / (2 * i + 1)
        pi += term
    pi *= 4
    return pi
