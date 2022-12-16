import random
import numpy as np
import random
#remember that the inverse of an operator(%) is not equal so i need to check or use the correct data

def main():
    f = open(r"./prova/file.txt", "r")
    a = []
    tmp = []
    for i in f: 
        k = []
        t = (i.replace("\n", "").split(" "))
        for s in t:
            k.append(int(s)) 
        a.append(k)
    s = 0
    l = 0
    for i in a:

        for k in range(len(i)):
            for t in range(k+1, len(i)):
                if i[k] % i[t] == 0:
                    s +=  i[k] // i[t]
                    break 
                elif i[t] % i[k] == 0:
                    s +=  i[t] // i[k]
                    break 

    print(s)
    f.close()

