#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""
def sumOfValues():
    filename = 'task03.txt'
    file = open(filename,'r')
    data = file.read()
    fList = data.split('\n')
    templist = []
    allNum = []


    for i in fList:
        if i != "":
            i = int(i)
            templist.append(i)
        if i == "":
            allNum.append(sum(templist))
            templist = []
    
    allNum.sort()
    largest = allNum[-1]
    print(largest)

    



sumOfValues()