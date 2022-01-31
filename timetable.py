import itertools as it
import random
from tabulate import tabulate
from image_gen import gen_img as img

def timetable_main(days,subject_n,subjects):
    #subjects = []
    #for i in range(n):
    #    subjects.append(input('enter subject - '))

    perm = list(it.permutations(subjects))  # all possible arrangements of periods in a list
    if len(perm)<days:
        perm *= days

    days_of_the_week = ["Monday", "Tuesday", "Wednesday","Thursday","Friday"]
    head = ["Day"]
    for i in range(1,subject_n + 1):
        head.append(i)

    
    final = random.sample(perm,days) # choosing 5 random arrangments (depending on number of working days)
    for j in range(days):
        final[j] = (days_of_the_week[j],)+final[j]

    table = tabulate(final, headers= head, tablefmt="grid")
    img(table)

# days = int(input('enter number of working days - '))
# n = int(input('enter number of subjects - '))

#timetable_main(days,n)
