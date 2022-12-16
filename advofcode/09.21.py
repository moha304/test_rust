import collections

def main():
    f = open(r"C:\Users\moha\v1\project1\python-project-template\prova\file.txt", "r")
    a = []
    c = 0
    for i in f: 
        if i != "\n":
            i = i.replace("\n", "")
            a.append(i)
        else :
            break
        c+=1
        
    print(a)
    f.close()


