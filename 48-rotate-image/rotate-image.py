class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #matrix = matrix[::-1]
        n = len(matrix[0])
        for i in range(n):
            for j in range(i+1, n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        for i in range(n):
            matrix[i] = matrix[i][::-1]

