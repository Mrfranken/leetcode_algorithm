class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i, j = len(matrix) - 1, 0

        while i >= 0 and j < len(matrix[0]):
            current = matrix[i][j]
            if current == target:
                return True
            if target < current:
                i -= 1
            else:
                j += 1
        return False


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15],
              [2, 5, 8, 12, 19],
              [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    print(Solution().searchMatrix(matrix, target))
