import random
import os

path = 'C:\\Users\\rexze\\Downloads\\riddle.txt'
file = open(path, 'r')
f = file.read()
one = f.split('\n\n')

def write_array(an_array, file):
    for index, row in enumerate(an_array) :
        row = f'{index+1}    {row} \n\n\n'
        with open(file, 'a') as f2:
            f2.write(row)

print(one)
for k in range(65):
    random.shuffle(one)
    c = [one[i] for i in range(10)]
    write_array(c, str(k) + '.txt')
    print(c)

