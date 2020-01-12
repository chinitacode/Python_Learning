from random import random
#Using Monte Carlo Simulation
def pi(TRIES):
    HITS = 0
    for i in range(TRIES):
        #Generate two random numbers between [-1,1] as the x-coordinate and y-coordinate of the shot
        x = -1 + 2*random()
        y = -1 + 2*random()
        # Check whether the point lies in the unit circle
        if x**2 + y**2 < 1:
            HITS += 1
    # The ratio hits / tries is approximately the same as the ratio
    # circle area / square area = pi / 4.
    return 4*(HITS/TRIES)
