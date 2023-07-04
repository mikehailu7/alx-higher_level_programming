#!/usr/bin/python3
# Author: mikiasHailu
# Fun: Advanced

""" this is a backtracking program """

from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    for m in range(n):
        a.append([m, None])

    def already_exists(y):
        """This function will check that a queen does not already exist in that y value"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """THis function will determines if you want ot reject the solution"""
        if (already_exists(y)):
            return False
        m = 0
        while(m < x):
            if abs(a[m][1] - y) == abs(m - x):
                return False
            m = m + 1
        return True

    def clear_a(x):
        """ THis function will erase the answer if there is error."""
        for m in range(x, n):
            a[m][1] = None

    def nqueens(x):
        """This function will find the solution """
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == n - 1): 
                    print(a)
                else:
                    nqueens(x + 1)
    nqueens(0)
