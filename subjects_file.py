import csv

def enter(subs):
    f = open("subjects_file.csv","w")
    w = csv.writer(f)
    w.writerow(subs)
    f.close()

def export():
    f = open("subjects_file.csv","r")
    r = csv.reader(f)
    subs = []
    for i in r:
        for j in i:
            subs.append(j)
    return subs
