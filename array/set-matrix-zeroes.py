class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n=len(matrix[0])

        row_zero = [False] * m
        col_zero = [False] *n

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row_zero[i]=True
                    col_zero[j]=True
        
        for i in range(m):
            if row_zero[i]:
                for j in range(n):
                    matrix[i][j]=0
        for i in range(m):
            for j in range(n):
                if col_zero[j]:
                    matrix[i][j]=0