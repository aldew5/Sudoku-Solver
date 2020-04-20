"""
BOX INDEXING ISN'T FUCKING GOD DAMN WORKING!!!
"""

import math

def get_poss(puzzle, ri, ci):
    """returns a list possible numbers for a given cell"""
    poss = [1,2,3,4,5,6,7,8,9]

    # check row
    for x in range(9):
        if puzzle[ri][x] in poss:
            poss.pop(poss.index(puzzle[ri][x]))
            
    # check column      
    for row in puzzle:
        if row[ci] in poss:
            poss.pop(poss.index(row[ci]))

    # set box index where a box is a 3x3 subsection
    # of the puzzle that must contain 1-9
    if ri < 3:
        bir = 0
    elif ri >= 3 and ri <= 5:
        bir = 1
    elif ri >= 6:
        bir = 2

    if ci < 3:
        bic = 0
    elif ci >= 3 and ci <= 5:
        bic = 1
    elif ci >= 6:
        bic = 2

    boxi = (bir, bic)

    # check against other numbers in the box
    for row in puzzle[boxi[0]*3: (boxi[0]*3) + 3]:
        for n in row[boxi[1]*3: (boxi[1] *3)  + 3]:
            if n in poss:
                poss.pop(poss.index(n))

    return poss


def find_empty(puzzle):
    for row in puzzle:
        for i in row:
            if i == 0:
                return (puzzle.index(row), row.index(i))
    return []

def print_puzzle(puzzle):
    for row in puzzle:
        print(*row)



def solve(puzzle):
    """takes in a 2D array representin the sodoku board
        and solves using backtracking"""

    # basecase (no empty cells)
    if len(find_empty(puzzle)) == 0:
        return True
    else:
        # get row and column indices of empty cell
        ri, ci = find_empty(puzzle)[0], find_empty(puzzle)[1]

    # try all possibilites
    for n in get_poss(puzzle, ri, ci):
        puzzle[ri][ci] = n

        # recursive call with the updated puzzle
        if solve(puzzle):
            return True
        # reset (line didn't work)
        else:
            puzzle[ri][ci] = 0

    return False




