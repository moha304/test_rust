import collections

def main():
    f = open(r"C:\Users\moha\v1\project1\python-project-template\prova\file.txt", "r")
    a = []
    moves = []
    for i in f:
        if i != "\n":
            a.append(i.replace("\n", "").replace("[", "").replace("]", ""))
        else:
            break
            
    s = []
    c = 0
    for i in range(len(a) -1):
        s.append([])
        for t in a[i]:
            s[i].append(t)

    for t in s:
        c = 0
        start = 0
        end = 0
        for i in range(len(t) - 2):
            if c == 0:
                start = i
            if c < 3:
                if t[i] == " ":
                    c += 1
                else:
                    c = 0
            else:
                end = i
                t[start:end] = ""
                c = 0

    print(a)
    print(s)
    f.close()
