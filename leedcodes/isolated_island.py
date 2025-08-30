
#changed by main
class Solution(object):
    def influence(self, grid, row, colunm):
        grid[row][colunm] = "2"
        length = len(grid[0])
        height = len(grid)
        if 0 <= row - 1 < height:
            if grid[row - 1][colunm] == "1":
                grid[row - 1][colunm] = "2"
                self.influence(grid, row - 1, colunm)
        if 0 <= row + 1 < height:
            if grid[row + 1][colunm] == "1":
                grid[row + 1][colunm] = "2"
                self.influence(grid, row + 1, colunm)
        if 0 <= colunm - 1 < length:
            if grid[row][colunm - 1] == "1":
                grid[row][colunm - 1] = "2"
                self.influence(grid, row, colunm - 1)
        if 0 <= colunm + 1 < length:
            if grid[row][colunm + 1] == "1":
                grid[row][colunm + 1] = "2"
                self.influence(grid, row, colunm + 1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        length = len(grid[0])
        height = len(grid)
        count = 0
        for num_line in range(height):
            for nums in range(length):
                if grid[num_line][nums] == "1":
                    count += 1
                    self.influence(grid, num_line, nums)
        return count




grid=[["1","1","1"],
      ["0","1","0"],
      ["1","1","1"]]
Item=Solution()
answer=Item.numIslands(grid)
print(answer)
