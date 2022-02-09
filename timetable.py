import itertools as it
import random
from tabulate import tabulate
from image_gen import gen_img as img

def timetable_main(days,subject_n,subjects):

    perm = list(it.permutations(subjects))  # all possible arrangements of periods in a list
    if len(perm)<days:      # in case the number of permutations are less than number of days
        perm *= days

    days_of_the_week = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday"]   #list that stores days of the week
    head = ["Day"]
    for i in range(1,subject_n + 1):
        head.append(i)

    
    final = random.sample(perm,days) # choosing 5 random arrangements (depending on number of working days)
    for j in range(days):
        final[j] = (days_of_the_week[j],)+final[j]

    table = tabulate(final, headers= head, tablefmt="grid")     # putting it into table form
    img(table)

