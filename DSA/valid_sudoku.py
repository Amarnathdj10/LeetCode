class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Create arrays of 9 sets to track seen numbers for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                    
                # Identify which 3x3 sub-box this cell belongs to (0 to 8)
                box_index = (r // 3) * 3 + (c // 3)
                
                # Check if the number already exists in the current row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False
                    
                # Otherwise, record the number in its respective sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)
                
        return True