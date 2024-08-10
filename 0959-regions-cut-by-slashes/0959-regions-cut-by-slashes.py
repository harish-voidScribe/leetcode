from typing import List

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Helper function to find the root of a set
        def find_set(root_index):
            if parent[root_index] != root_index:
                parent[root_index] = find_set(parent[root_index])
            return parent[root_index]

        # Helper function to merge two sets
        def union_sets(set_a, set_b):
            root_a, root_b = find_set(set_a), find_set(set_b)
            if root_a != root_b:
                parent[root_a] = root_b
                nonlocal region_count
                region_count -= 1

        # The size of the grid
        n = len(grid)
        # Initial count of distinct regions
        region_count = n * n * 4
        # Initialize parent pointers for each cell * 4 for internal division
        parent = list(range(region_count))

        # Iterate over each cell in the grid
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                cell_index = i * n + j
                # If not in the bottom row, unite bottom and top of adjacent cells
                if i < n - 1:
                    union_sets(4 * cell_index + 2, 4 * (cell_index + n))
                # If not in the rightmost column, unite right and left of adjacent cells
                if j < n - 1:
                    union_sets(4 * cell_index + 1, 4 * (cell_index + 1) + 3)
              
                # Merge sets based on the presence of slashes
                if value == '/':
                    union_sets(4 * cell_index, 4 * cell_index + 3)
                    union_sets(4 * cell_index + 1, 4 * cell_index + 2)
                elif value == '\\':
                    union_sets(4 * cell_index, 4 * cell_index + 1)
                    union_sets(4 * cell_index + 2, 4 * cell_index + 3)
                else:
                    # No slashes means all 4 parts are connected
                    union_sets(4 * cell_index, 4 * cell_index + 1)
                    union_sets(4 * cell_index + 1, 4 * cell_index + 2)
                    union_sets(4 * cell_index + 2, 4 * cell_index + 3)
      
        # The number of regions is the number of distinct sets
        return region_count