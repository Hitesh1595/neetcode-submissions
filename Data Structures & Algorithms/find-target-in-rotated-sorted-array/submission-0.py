class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left , right = 0 , len(arr) - 1
        while left <= right:
            mid = (left + right)//2

            if arr[mid] == target:
                return mid

            elif arr[left] <= arr[mid]:
                # left side
                if arr[left] <= target < arr[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid -1
                # right side
        return -1

