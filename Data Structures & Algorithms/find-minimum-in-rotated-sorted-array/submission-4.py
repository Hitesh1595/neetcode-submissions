class Solution:
    def findMin(self, arr: List[int]) -> int:

        left, right = 0 , len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[right] < arr[mid]:
                left = mid + 1
            else:
                right = mid

        return arr[left]

            

        