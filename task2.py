"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

def pytriples():
    filename = 'task02c.txt'
    file = open(filename,'r')
    data = file.read()
    fList = data.split('\n')
    templist = []
    found = 0
    hyp = 0
    sides = 0

    for i in fList:
        if i != "":
            templist.append(i)
            if len(templist) == 3:
                a = templist[0]
                a = int(a)
                a = a**2
                b = templist[1]
                b = int(b)
                b = b**2
                c = templist[2]
                c = int(c)
                c = c**2
                if (a >= b) and (a >= c):
                    hyp = a
                    sides = b + c
                elif (b >= a) and (b >= c):
                    hyp = b
                    sides = a + c
                elif (c >= a) and (c >= b):
                    hyp = c
                    sides = a + b

                if sides == hyp:
                    found = found + 1
                elif sides != hyp:
                    templist = []
                    continue

                templist = []
        elif i == "":
            continue
    print(found)

    return found

pytriples()