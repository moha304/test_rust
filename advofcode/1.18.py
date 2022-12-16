import collections

def main():
    f = open(r"C:\Users\moha\v1\project1\python-project-template\prova\file.txt", "r")
    points = 0
    e = []

    for x in f:
        e.append(points)
        points += int(x)
    
    print([item for item, count in collections.Counter(e).items() if count > 1])
    f.close()




