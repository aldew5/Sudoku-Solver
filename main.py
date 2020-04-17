def get_poss(puzzle, ri, ci):
    """returns a list possible numbers for a given cell"""
    # check row
    poss = [1,2,3,4,5,6,7,8,9]
    for x in range(9):
        if puzzle[ri][x] != 0 and puzzle[ri][x] in poss:
            poss.pop(poss.index(puzzle[ri][x]))
            

    for row in puzzle:
        if row[ci] in poss:
            poss.pop(poss.index(row[ci]))

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
                        
                    
if __name__== "__main__":

    zero = [[0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]]

    puzzle = [[0,8,0,0,0,0,0,0,4],
            [0,2,0,1,9,0,7,0,0],
            [0,0,9,5,0,8,0,2,0],
            [3,9,0,8,0,0,4,6,0],
            [4,0,2,0,6,0,5,0,8],
            [0,6,8,0,0,2,0,1,7],
            [0,7,0,9,0,6,2,0,0],
            [0,0,6,0,8,1,0,7,0],
            [9,0,0,0,0,0,0,4,0]]

    if solve(puzzle):
        print_puzzle(puzzle)
    else:
        print("There are no valid solutions")
