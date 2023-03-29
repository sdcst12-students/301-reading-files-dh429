"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

filename = "task5.csv"
file = open(filename,"r")
data = file.read()

lineData = data.split("\n")
found = 0


symbol = input("Enter a stock symbol: ")

for i in lineData:
    stocks = i.split(",")
    if symbol in stocks[0]:
        found = found + 1
        if found == 1:
            first = stocks[1]

if found > 1:
    print(f"There are {found} stocks with that symbol")
elif stocks == 1:
    print(first)
else:
    print("No matches")

