import collections
            

def checkIn(a, b):
    for i in b:
        if i not in a:
            return False
    return True


def main():
    f = open(r"C:\Users\moha\v1\project1\python-project-template\prova\file.txt", "r")
    a = [[]]
    c = 0
    s = 0
    for i in f: 
        if i != "\n":
            i = i.replace("\n", "")
            a[c].append(i)
        else :
            a.append([])
            c+=1

    for i in a:
        for t in i:
            if (checkIn(t, i)):
                s += len(t)
                print(s)

    print(s)
    f.close()


