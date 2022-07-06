class Solution:
   def solve(self, matrix, r, c, target):
      def dfs(i, j):
         if (
            i >= 0
            and i < len(matrix)
            and j >= 0
            and j < len(matrix[0])
            and (i, j) not in seen
            and matrix[i][j] == oldcolor
         ):
            seen.add((i, j))
            matrix[i][j] = target
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i - 1, j)
      seen = set()
      oldcolor = matrix[r][c]
      dfs(r, c)
      return matrix
ob = Solution()
matrix = [ ["l", "o", "s"], ["s", "l", "n"], ["h", "o", "m"] ]
r = 0
c = 0
target = "g"
print(ob.solve(matrix, r, c, target))