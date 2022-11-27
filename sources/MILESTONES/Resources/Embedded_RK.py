# Embedded Runge Kutta Temporal Scheme
from numpy import zeros, matmul, size
from numpy.linalg import norm

def Embedded_RK(U, dt, F, t):

    RK_Method = "DOPRI54"
    tol = 1e-6

    V1 = RK(RK_Method, "First", U, t, dt, F) 
    V2 = RK(RK_Method, "Second", U, t, dt, F) 

    a, b, bs, c, q, Ne = Butcher_array(RK_Method)

    h = min(dt, Step_Size(V1-V2, tol, dt,  min(q)))

    N_n = int(dt/h)+1
    n_dt = dt/N_n

    V1 = U
    V2 = U

    for i in range(N_n):
        time = t + i*dt/int(N_n)
        V1 = V2
        V2 = RK(RK_Method, "First", V1, time, n_dt, F)

    U2 = V2

    ierr = 0

    return U2



def RK(name, tag, U1, t, dt, F):
    a, b, bs, c, q, Ne = Butcher_array(name)
    k = zeros([Ne, len(U1)])

    k[0,:] = F(U1, t + c[0]*dt)

    if tag=="First":
        
        for i in range(1,Ne):
            Up = U1
            for j in range(i):
                Up = Up + dt*a[i,j]*k[j,:]

            k[i,:] = F(Up, t + c[i]*dt)

        U2 = U1 + dt*matmul(b,k)

    elif tag == "Second":

        for i in range(1,Ne):
            Up = U1
            for j in range(i):
                Up = Up + dt*a[i,j]*k[j,:]

            k[i,:] = F(Up, t + c[i]*dt)

        U2 = U1 + dt*matmul(bs,k)

    return U2



def Step_Size(dU, tol, dt, q): #dU es el error estimado, tol el error máximo permitido y q el orden de dicho error
    normT = norm(dU)

    if normT > tol:
        step_size = dt*(tol/normT)**(1/(q+1))
    else:
        step_size = dt

    return step_size

def Butcher_array(name):
     if name == "HeunEuler21":
        q = [2,1]
        Ne = 2 

        a = zeros([Ne,Ne-1])
        b = zeros([Ne])
        bs = zeros([Ne])
        c = zeros([Ne])
      
        c = [ 0., 1. ]

        a[0,:] = [  0. ]
        a[1,:] = [  1. ]

        b[:]  = [ 1./2, 1./2 ]
        bs[:] = [ 1.,    0.  ]
   
     elif  name == "RK21":
        q = [2,1]
        Ne = 3 

        a = zeros([Ne,Ne-1])
        b = zeros([Ne])
        bs = zeros([Ne])
        c = zeros([Ne])
      
        c[:] = [ 0., 0.5, 1. ]

        a[0,:] = [  0., 0. ]
        a[1,:] = [  1./2, 0. ]
        a[2,:] = [  1./256,  255./256	]

        b[:]  = [ 1./256,	255./256,	0. ]
        bs[:] = [ 1./512,	255./256,	1./512 ]
      
     elif  name=="BogackiShampine":
        q = [3,2]
        Ne = 4 

        a = zeros([Ne,Ne-1])
        b = zeros([Ne])
        bs = zeros([Ne])
        c = zeros([Ne])
      
        c[:] = [ 0., 1./2, 3./4, 1. ]

        a[0,:] = [  0., 0., 0.            ]
        a[1,:] = [ 1./2, 0., 0.           ]
        a[2,:] = [ 0.,	3./4, 0.    	]
        a[3,:] = [ 2./9,	1./3,	4./9 	]

        b[:]  = [ 2./9,	1./3,	4./9,	0. ]
        bs[:] = [ 7./24,	1./4,	1./3,	1./8 ]
 
      
     elif name=="DOPRI54": 
        q = [5,4]
        Ne = 7 

        a = zeros([Ne,Ne-1])
        b = zeros([Ne])
        bs = zeros([Ne])
        c = zeros([Ne])
      
        c[:] = [ 0., 1./5, 3./10, 4./5, 8./9, 1., 1. ]

        a[0,:] = [          0.,           0.,           0.,         0.,           0.,     0. ]
        a[1,:] = [      1./5  ,           0.,           0.,         0.,           0.,     0. ]
        a[2,:]= [      3./40 ,        9./40,           0.,         0.,           0.,     0. ]
        a[3,:] = [     44./45 ,      -56./15,        32./9,         0.,           0.,     0. ]
        a[4,:] = [ 19372./6561, -25360./2187,  64448./6561,  -212./729,           0.,     0. ]
        a[5,:] = [  9017./3168,    -355./33 ,  46732./5247,    49./176, -5103./18656,     0. ]
        a[6,:]= [    35./384 ,           0.,    500./1113,   125./192, -2187./6784 , 11./84 ]

        b[:]  = [ 35./384   , 0.,   500./1113,  125./192,  -2187./6784  ,  11./84  ,     0.]
        bs[:] = [5179./57600, 0., 7571./16695,  393./640, -92097./339200, 187./2100, 1./40 ]  
    

     elif name=="CashKarp":
        q = [5,4] 
        Ne = 6 

        a = zeros([Ne,Ne-1])
        b = zeros([Ne])
        bs = zeros([Ne])
        c = zeros([Ne])

        c[:] = [ 0., 1./5, 3./10, 3./5, 1., 7./8 ]
      
        a[1,:] = [ 0.,          0.,       0.,         0.,            0. ] 
        a[2,:] = [ 1./5,        0.,       0.,         0.,            0. ] 
        a[3,:] = [ 3./40,       9./40,    0.,         0.,            0. ] 
        a[4,:] = [ 3./10,      -9./10,    6./5,       0.,            0. ] 
        a[5,:] = [ -11./54,     5./2,    -70./27,     35./27,        0. ] 
        a[6,:] = [ 1631./55296, 175./512, 575./13824, 44275./110592, 253./4096 ] 

        b[:]  = [    37./378, 0.,     250./621,     125./594,         0., 512./1771]
        bs[:] = [2825./27648, 0., 18575./48384, 13525./55296, 277./14336,     1./4 ]    
       
     return a, b, bs, c, q, Ne

