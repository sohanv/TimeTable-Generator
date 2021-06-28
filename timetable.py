import itertools as it
import random

days = int(input('enter number of working days - '))
n = int(input('enter number of subjects - '))
subjects = []
for i in range(n):
    subjects.append(input('enter subject - '))

perm = list(it.permutations(subjects))  # all possible arrangements of periods in a list
final = random.sample(perm,days)  # choosing 5 random arrangments (have to change depending on number of working days)
print(final)