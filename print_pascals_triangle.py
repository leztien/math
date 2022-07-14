"""
print Pascal's Triangle (recursive function)
"""


def recurse(n):
    #base case
    if n == 0:
        row = [1,]
        print(row)
        return row
    
    #recurseve case
    row = recurse(n-1)
    row = [1,] + [row[i] + row[i+1] for i in range(n-1)] + [1,]
    print(row, sum(row), sum(n * (+1 if i%2 else -1) for i,n in enumerate(row)))
    return row
    


recurse(n=7)
