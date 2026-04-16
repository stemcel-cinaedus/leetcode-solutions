class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r, z = 0, len(matrix[0]) - 1, 0 
        while z < len(matrix):
            if matrix[z][0] <= target and matrix[z][r] >= target:
                while l <= r:
                    mid = (l + r) // 2
                    if matrix[z][mid] == target:
                        return True
                    elif matrix[z][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False
            else:
                z += 1
        return False
