
#!/usr/bin/env python 
#   Author: Christopher Bull. 
#   Affiliation:  British Antarctic Survey
#                 Cambridge, UK
#   Contact: chbull@bas.ac.uk
#   www:     christopherbull.com.au
#   Date created: Sun, 13 Mar 2022 14:29:36
#   Machine created on: SB2Vbox
"""
Step 1: 1-D Linear Convection
"""
from cb2logger import *
import numpy                       #here we load numpy
from matplotlib import pyplot      #here we load matplotlib
import matplotlib.pyplot as plt
import time, sys                   #and load some utilities

if __name__ == "__main__": 
    LogStart('',fout=False)
    #Now let's define a few variables; we want to define an evenly spaced grid of points within a spatial domain that is 2 units of length wide, i.e., 𝑥𝑖∈(0,2). We'll define a variable nx, which will be the number of grid points we want and dx will be the distance between any pair of adjacent grid points. 

    nx = 41  # try changing this number from 41 to 81 and Run All ... what happens? 
    #CB: seems like '81' is the necessary amount of resolution required to not difuse the bump, 61 does better but not as good as 81

    dx = 2 / (nx-1)
    nt = 25    #nt is the number of timesteps we want to calculate
    dt = .025  #dt is the amount of time each timestep covers (delta t)
    c = 1      #assume wavespeed of c = 1

    #We also need to set up our initial conditions. The initial velocity 𝑢0 is given as 𝑢=2 in the interval 0.5≤𝑥≤1 and 𝑢=1 everywhere else in (0,2) (i.e., a hat function).
    u = numpy.ones(nx)      #numpy function ones()
    u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s


    pyplot.plot(numpy.linspace(0, 2, nx), u)
    #Why doesn't the hat function have perfectly straight sides? Think for a bit.

    #cb: b/c nx has a small number of points (goes to vertical as nx--> \infinity)
    #plt.show()


    un = numpy.ones(nx) #initialize a temporary array

    for n in range(nt):  #loop for values of n from 0 to nt, so it will run nt times
        un = u.copy() ##copy the existing values of u into un
        for i in range(1, nx): ## you can try commenting this line and...
        #for i in range(nx): ## ... uncommenting this line and see what happens!
            u[i] = un[i] - c * dt / dx * (un[i] - un[i-1])

    pyplot.plot(numpy.linspace(0, 2, nx), u)
    plt.show()

    lg.info('')
    localtime = time.asctime( time.localtime(time.time()) )
    lg.info("Local current time : "+ str(localtime))
    lg.info('SCRIPT ended')
