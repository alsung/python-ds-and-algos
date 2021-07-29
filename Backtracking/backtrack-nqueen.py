# Backtracking exercise 

# The N-queens puzzle is a problem of placing N queens on an N x N chessboard
# such that no two queens can attack each other. One is asked to count the 
# number of solutions to place the N queens on the board. 

# If we place a queen at row 1 column 1, then we cross out all the cells that
# can be attacked by this queen. 

# In order to count number of possible solutions, follow steps:

# 1. Overall, iterate over each row in board (once we reach last row, we've 
#    explored all possible solutions).
# 2. At each iteration (we are located at certain row), we further iterate over
#    each column of the board, along the current row. At this second iteration, 
#    we can explore the possibility of placing a queen on a particular cell. 
# 3. Before, we place a queen on the cell with index (row, col), we need to check
#    if cell is under the attacking zone of the queens that have been placed on the
#    board before. Let's assume function called is_not_under_attack(row, col) can
#    do the check. 
# 4. Once the check passes, we can proceed to place a queen. We should also mark 
#    out the attacking zone of the newly-placed queen. Let's assume function called
#    place_queen(row, col) will do so. 
# 5. As an important behavior of backtracking, we should be able to abandon our previous 
#    decision at the moment we decide to move on to the next candidate. Let's assume 
#    function remove_queen(row, col) can help us revert decision along with changes in (4)

# Pseudocode:

def backtrack_nqueen(row=0, count=0):
    for col in range(n):
        # iterate through columns at each row
        if is_not_under_attack(row, col):
            # explore this partial candidate solution, and mark the attacking zone
            place_queen(row, col)
            if row+1 == n:
                # reached the bottom, i.e., we find a solution
                count += 1
            else:
                # move onto next row
                count = backtrack(row + 1, count)
            # backtrack, i.e., remove queen and remove attacking zone
            remove_queen(row, col)
    return count

# ---------------------------------------------------------------------------------------
# Backtracking Template:
# - overall the enumeration of candidates is done in two levels. 
#   1. at first level, function implemented as recursion. at each occurrence of recursion
#      the function is one step further to final solution. 
#   2. at second level, within recursion, we have an iteration that allows us to explore
#      all the candidates that are of the same progress to final solution
# - backtracking should happen at level of iteration within recursion
# - unlike brute force search, backtracking algos are often able to determine if a partial
#   solution is worth exploring further (i.e. is_valid(next_candidate)), which allows us 
#   to prune the search zones. AKA the constraint, e.g. attacking zone of queen in N-queen
# - there are two symmetric functions that allow us to mark the decision (place(candidate))
#   and revert the decision (remove(candidate))
# ---------------------------------------------------------------------------------------

def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)

# ---------------------------------------------------------------------------------------
# Robot Room Cleaner
# 
# Given a room that is represented as a grid of cells, where each cell contains a value
# that indicates whether it is an obstacle or not, we are asked to clean the room with a 
# robot cleaner which can turn in four direction and move one step at a time. 
# ---------------------------------------------------------------------------------------

# General Idea

# 1. One can model each step of the robot as a recursive function (backtrack())
# 2. At each step, technically the robot would have four candidates of direction to explore
#    e.g. robot located at (0,0). Since not each direction is available though, one should
#    check if cell in given direction is obstacle or it has been cleaned before, i.e,
#    is_valid(candidate). Greatly reduce number of possible paths to explore. 
# 3. Once robot decides to explore cell in certain direction, robot should mark its decision
#    (place(candidate)). Later, robot should be able to revert prev decision (remove(candidate))
#    by going back to cell and restore its original direction. 
# 4. Robot conducts cleaning step by step, in form of recursion of backtrack() function. The 
#    backtracking would be triggered by when robot reaches a point that is surrounded by either
#    obstacles or cleaned cells. At end of backtracking, robot would get back to starting point, 
#    and each cell in the ground would be traversed at least once. As result, room is cleaned at
#    the end. 

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot(object):
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell = (0, 0), d = 0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], \
                            cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()

