class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = 0
        col = 0
        direction = 0
        result = []
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        visited = set()

        while len(result) < num_rows * num_cols:
            if (row, col) in visited:
                if direction == 0:
                    direction = 1
                    col -= 1
                    row += 1
                elif direction == 1:
                    direction = 2
                    row -= 1
                    col -= 1
                elif direction == 2:
                    direction = 3
                    row -= 1
                    col += 1
                else:
                    direction = 0
                    row += 1
                    col += 1
            result.append(matrix[row][col])
            visited.add((row, col))
            if direction == 0: # Right
                if col == num_cols - 1:
                    direction = 1
                    row += 1
                else:
                    col += 1
            elif direction == 1: # Down
                if row == num_rows - 1:
                    direction = 2
                    col -= 1
                else:
                    row += 1
            elif direction == 2: # Left
                if col == 0:
                    direction = 3
                    row -= 1
                else:
                    col -= 1
            else: # Up
                if row == 0:
                    direction = 0
                    col += 1
                else:
                    row -= 1
        
        return result