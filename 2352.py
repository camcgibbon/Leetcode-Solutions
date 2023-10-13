# Equal Row and Column Pairs

'''Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

'''

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        total = 0
        columns = {}
        for i in range(len(grid)):
            columns[i] = []
        for row in grid:
            for i, num in enumerate(row):
                columns[i].append(num)
        for row in grid:
            for key in columns:
                if row == columns[key]:
                    total += 1
        return total