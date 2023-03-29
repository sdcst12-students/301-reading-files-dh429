#!python3
# Advanced Dungeons and Dragons

"""
the file task04.txt contains a matrix of values
The row indicates the level of fighter. Row 1 is for a level 1 fighter, row 2 is for a level 2 fighter and so on

In each row, the numers indicate the target number needed out of 20 to land a hit on a specific Armor Class, starting with
10 on the left, followed by 9, then 8, all the way to -10 on the far right.

Create a function that reads the specific value for a specific level and an armor class, and prints the target number needed.

"""

def target(lvl,ac):
    filename = 'task04.txt'
    file = open(filename,'r')
    data = file.read()
    fList = data.split('\n')
    runLvl = 1
    
    for line in fList:
        lvlList = line.split(',')
        if runLvl == lvl:
            acList = line.split(' ')
            ac = 10 - ac
            diceRoll = acList[ac]
            diceRoll = int(diceRoll)
        runLvl = runLvl + 1
        
    return diceRoll


def tests():
    assert target(3,7) == 12
    assert target(9,-1) == 17
    assert target(13,-10) == 20

if __name__=="__main__":
    tests()