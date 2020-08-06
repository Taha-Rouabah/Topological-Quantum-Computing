# -*- coding: utf-8 -*-
"""
Created on Thu Mar 7th 2019

@author: N. Belaloui

This file contains the script which looks for the weave that approximates best
the operator U, from a library of weaves either contained in a file or
generated once in this script (set fromFile = True or False).
"""

import time
import pickle #used to read and write files
from numpy import *
from weavescalculator import *
from braidgenerator import *

# Get the weaves from a file if True, generate them if False.
fromFile = False
weaves = None

# Max length of the weaves (set value if fromFile = False)
LENGTH = 14

start = time.time()

# We declare the hermitian adjoint of U
U_ = matrix('0, 1; 1, 0')/sqrt(2)

# Getting the weaves
if fromFile:
    # We load the weaves from an external file
    with open("20_sigmas.data", "rb") as filehandle:
        weaves = pickle.load(filehandle)
else:
    # Generating all weaves of length L <= LENGTH
    weaves = generateSeqList(LENGTH)

bestDist = 2 # We initialize the best distance variable with a big value (ex: 2)


for i in range(0,len(weaves)):

    W = weaveMatrix(weaves[i], 1) # Computing the weave stating with sigma_1
    # curDist = weaveDist(W @ U_) # Computing the weave-gate distance
    curDist = traceNorm(W, U_)
    if curDist < bestDist:
        bestDist = curDist # Updating the new best distance
        bestWeaveIndex = i # Updating the new best weave index
        bestS = 1 # Specifying with which sigma we start the weave
        print('\n-------------------\n', W)
        print('Last best dist =', traceNorm(W, U_))
        print("Progress = {}%".format((i*100)//len(weaves)))

    W = weaveMatrix(weaves[i], 2) # Computing the weave stating with sigma_2
    # curDist = weaveDist(W @ U_) # Computing the weave-gate distance
    curDist = traceNorm(W, U_)
    if curDist < bestDist:
        bestDist = curDist # same...
        bestWeaveIndex = i # same...
        bestS = 2 # same...
        print('\n-------------------\n', W)
        print('Last best dist =', traceNorm(W, U_))
        print("Progress = {}%".format((i*100)//len(weaves)))

#Printing the final results
print('\n-------------------\n')
print('L =', sum([abs(_) for _ in weaves[bestWeaveIndex]]))
print('W =', weaveMatrix(weaves[bestWeaveIndex], bestS))
print('Starting sigma =', bestS)
print('Best distance =', bestDist)
print('Index in weaves list =', bestWeaveIndex)
print("time : {}".format(time.time() - start))
