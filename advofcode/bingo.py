import collections
import math 
import random
import ast
import numpy as np

def checkIfIn(x, data):
    s = []
    tmp = []
    for i in x:
        t = i.split(' ')
        for k in t:
            if k in data:
                tmp.append(True)
            else:
                tmp.append(False)
        s.append(tmp)
        tmp = []

    return s


def checkRows(data):
    for i in data:
        if False not in i:
            print(i)

def checkCols(data):
    for col in range(len(data)):
        print(data[col])

def main():
    f = open(r"./prova/file.txt", "r")
    BingoN = []
    a = []
    tmp = []
    for i in f: 
        if len(BingoN) == 0:
            if i != "\n":
                BingoN.append(i.replace("\n", ""))
        
        elif i != "\n":
            s = i.replace("\n", "")
            tmp.append(s)
        else:
            a.append(tmp)
            print(tmp)
            tmp = []

    for i in a:
        checkRows(checkIfIn(i, BingoN[0].split(',')))
        for t in checkCols(checkIfIn(i, BingoN[0].split(','))):
            print(t)
        print('======================')

    f.close()

