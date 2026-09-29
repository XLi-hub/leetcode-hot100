class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat = [[0] * n for _ in range (n)]
        count = 1
        start_index = 0
        while count < n*n:
            for j in range(start_index,n-start_index-1):
                mat[start_index][j] = count
                count += 1
            for i in range(start_index,n-start_index-1):
                mat[i][n-1-start_index] = count
                count += 1
            for j in range(n-1-start_index,start_index,-1):
                mat[n-1-start_index][j] = count
                count += 1
            for i in range(n-1-start_index,start_index,-1):
                mat[i][start_index] = count
                count += 1
            start_index += 1
        if n % 2:
            mat[(n-1)//2][(n-1)//2] = n*n
        return mat