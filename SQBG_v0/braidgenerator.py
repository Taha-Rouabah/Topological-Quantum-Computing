# -*- coding: utf-8 -*-
"""
Created on Fri Mar 1st 2019

@author: N. Balaloui

This file contains functions generating all possible weaves of length L or less
"""


import time


def newSeq(x, length):
    """ Turns the weave into the next one """
    """ IT MODIFIES THE ARGUMENT 'x' ! """
    for i in range(length//2-1, -1, -1):
        if x[i] < 4:
            x[i] += 2 if x[i] != -2 else 4
            break
        elif x[i] == 0:
            x[i] = -4
            break
        else:
            x[i] = -4
    return x

def checkSeq(x, length):
    """ Returns true if the length of the weave 'x' is less than or equal to 'length' """
    s = 0
    for elem in x:
        s += abs(elem)

    return s <= length


def generatePosSeqList(length):
    """ Generates HALF of the possible weaves of a given length or less """
    posSeqList = []  # list that will contain the generated weaves
    curSeq = [0]*int(length//2)  # We devide by 2 as the sigmas have pair powers
    endSeq = [4]*int(length//2)


    while curSeq != endSeq:
        newSeq(curSeq, length) #transforms curSeq into the next one
        if checkSeq(curSeq, length): #we only keep the weaves of length 'length' or less
            posSeqList.append(curSeq.copy())

    return posSeqList


def generateSeqList(length):
    """ Generates ALL the possible weaves of a given length or less """
    seqList = generatePosSeqList(length) #first we generate the 'positive' weaves

    size = len(seqList)
    for i in range(0,size): #then we generate the rest of the weaves by multiplying
                            #the first half by -1
        seqList.append([x*(-1) for x in seqList[i]])

    return seqList

def timedGeneration(length):
    """ Same as generatePosSeqList(length), but with time information """
    start = time.time()
    res = generatePosSeqList(length)
    print(time.time() - start)
    return res
