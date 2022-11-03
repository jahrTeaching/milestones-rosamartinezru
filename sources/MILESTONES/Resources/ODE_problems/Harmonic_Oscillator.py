from numpy import array

## Harmonic Oscillator

def F_oscillator(U,t):
    a = 1
    return array([U[1], -a*U[0]])
