# -*- coding: utf-8 -*-
"""
Created on Sun Mar 3rd 2019

@author: N. Belaloui
"""


from numpy import *

""" BEGINNING INITIALIZATION """
""" Here we initialize the const. phi and the 2 sigma matrices (Braid Group generators)"""
phi = (1. + sqrt(5.))/2.

""" -----   s1 weave moves ----- """

s1 = matrix('{}, 0; 0, {}'.format(exp(-(4/5)*pi*1j), exp((3/5)*pi*1j)))

s1_list = [0,0,0,0]

s1_list[0] = linalg.inv(s1 @ s1 @ s1 @ s1) # sigma1 ^ -4
s1_list[1] = linalg.inv(s1 @ s1) # sigma1 ^ -2
s1_list[2] = s1 @ s1 # sigma1 ^ +2
s1_list[3] = s1 @ s1 @ s1 @ s1 # sigma1 ^ +4


""" -----   s2 weave moves ----- """

s2 = matrix('{}, {}; {}, {}'.format( exp((4/5)*pi*1j)/phi, exp(-(3/5)*pi*1j)/sqrt(phi),
            exp(-(3/5)*pi*1j)/sqrt(phi), -1./phi))

s2_list = [0,0,0,0]

s2_list[0] = linalg.inv(s2 @ s2 @ s2 @ s2) # sigma2 ^ -4
s2_list[1] = linalg.inv(s2 @ s2) # sigma2 ^ -4
s2_list[2] = s2 @ s2 # sigma2 ^ +2
s2_list[3] = s2 @ s2 @ s2 @ s2 # sigma2 ^ +4

""" END OF INITIALIZATION """
""" ----------------------------------------------------------------------- """

def weaveMatrix(weave, s):    # starts with sigma_s / s=1,2
    """ Computes the matrix corresponding to the weave """

    result = matrix('1, 0; 0, 1')
    s_index = s

    for i in range(len(weave)-1,-1,-1): # Multiplying the sigmas together
        if weave[i] == 0: # A 0 exponent means we reached the end of the weave
            break
        if s_index == 1:
            result = s1_list[(weave[i]+4-2*int(weave[i]>0))//2] @ result # Multiplying the next sigma
            s_index = 2 # changing the next sigma (1 -> 2)
        else:
            result = s2_list[(weave[i]+4-2*int(weave[i]>0))//2] @ result # Multiplying the next sigma
            s_index = 1 # changing the next sigma (2 -> 1)

    return result


def squareMod(x):
    """ Computes the square of the module of the complexe number 'x' """
    return x.real**2 + x.imag**2

# def weaveDist(WU_):
#     """ Tells us how far is the operator W from the operator U
#     Or, how far is the product W * U_hermit_adjoint from the identity form """
#     return squareMod(WU_[0,0]-WU_[1,1]) + squareMod(WU_[0,1]) + squareMod(WU_[1,0])

def traceNorm(W, U): # = linalg.norm(W - U) / sqrt(2) (see Field & Simula p23)
    """ The error metric used in Bonesteel et al.'s papers """
    return sqrt(2 - abs(trace(W @ U.getH())))

