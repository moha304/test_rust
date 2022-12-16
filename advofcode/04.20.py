import collections


def compare(tmp, li):
    for i in li:
        if i not in tmp:
            return 0
    
    print(tmp)
    return 1

def main():
    f = open(r"C:\Users\moha\v1\project1\python-project-template\prova\file.txt", "r")
    p = 0
    pass_data = []
    tmp = []
    for x in f:
        if x != "\n" :
            tmp.append(x.replace("\n", ""))
        else :
            a = ""
            for i in tmp:
                a += i
            pass_data.append(a)
            tmp = []
            
    for i in pass_data:
        t = []
        li = ['hgt', 'eyr', 'pid', 'ecl', 'byr', 'hcl', 'iyr']
        data = (i.split(" "))

        for i in data:
            t.append(i.split(":")[0])

        p += compare(t, li)

    print(p)
    f.close()
