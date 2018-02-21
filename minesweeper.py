#!/usr/bin/env python3

def main():
    """
    main function call
    """
    testgrid()

def testgrid():

    #g = grid(x=16,y=30,m=99)
    g = grid(x=3,y=3,m=2)
    

class cell:
    """
    a cell can have one ov the following visible states:
    - unclicked (closed)
    - flagged
    - uncovered (showing number) (open)
    - triggered (used as part of the lose screen
    - triggered flagged
    
    in addition, a cell will have the following hidden states
    - location (x,y) as an integer pair (tuple)
    - mined
    - numbers of neighboring mines
    """
    pass

class grid:
    """
    the grid owns the cells and can return cells from locations.
    it also holds the cells.
    it also creates the grid and assigns mines.
    """
if __name__== "__main__":
    main()
