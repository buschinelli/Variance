import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

def Var(array):
    mean = 0
    n = len(array)**3
    for k in range(0,len(array)):
        for i in range(0,len(array)):
            for j in range(0,len(array)):
                mean = mean + array[k,i,j]
    mean = mean/n

    summation = 0
    for k in range(0,len(array)):
        for i in range(0,len(array)):
            for j in range(0,len(array)):
                summation = summation + (x[k,i,j]-mean)**2

    var = summation/n
    return var

# test here


def Contour_plot(array,subarray):
    pixel_n = len(array)
    xlabel = np.arange(0,pixel_n)
    ylabel = np.arange(0,pixel_n)
    X, Y = np.meshgrid(xlabel,ylabel)
    Z = array[subarray]
    plt.contourf(X,Y,Z,20,cmap='RdGy')
    plt.xlabel('Pixel x location')
    plt.ylabel('Pixel y location')
    plt.xticks(np.arange(0,pixel_n,2))
    plt.yticks(np.arange(0,pixel_n,2))
    cb = plt.colorbar()
    cb.set_label('Field value')
    plt.show()


def Weight(array):
    n = len(array)
    for k in range(0,n):
        for i in range(0,n):
            for j in range(0,n):
                array[k,i,j] = (np.e**k) * array[k,i,j]

    return array
