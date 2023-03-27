"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

def pytriples():
    filename = 'task02a.txt'
    file = open(filename,'r')
    data = file.read()
    fList = data.split('\n')
    templist = []

    for i in fList:
        if i != "":
            templist.append(i)
            if len(templist) == 3:
                a = templist[0]
                b = templist[1]**2
                c = templist[2]**2
                if a + b == c:
                    print("cleared")
                templist = []
        elif i == "":
            print("bad")

    return

pytriples()