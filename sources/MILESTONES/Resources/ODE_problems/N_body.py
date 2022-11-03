from numpy import zeros, reshape
from numpy.linalg import norm


def F_N_body(U,t):
    (Nb, Nc) = (2, 3) # N_bodies, N_coordinates
    Us = reshape(U, (Nb, Nc, 2)) # Position and velocity

    r = reshape(Us[:, :, 0], (Nb, Nc)) # Position
    v = reshape(Us[:, :, 1], (Nb, Nc)) # Velocity

    F = zeros(len(U))
    Fs = reshape(F, (Nb, Nc, 2))

    drdt = reshape(Fs[:, :, 0], (Nb, Nc)) # Velocity
    dvdt = reshape(Fs[:, :, 1], (Nb, Nc)) # Acceleration

    dvdt[:,:] = 0

    for i in range(Nb):
        
        drdt[i,:] = v[i,:]

        for j in range(Nb):

            if j != i:

                d = r[j, :] - r[i, :]
                dvdt[i,:] = dvdt[i,:] + d[:]/(norm(d)**3)

    return F
